#!/usr/bin/env python
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from xml.etree.ElementTree import parse
#from __future__ import print_function
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from main import __xml__
from module.COLORS  import RESET
from module.TUI     import *
from module.debug   import *
from Class.Deck     import Deck
from Class.Location import Location

try:
    import i18n.i18n as i18n
    _ = i18n.language.gettext
except (ImportError, AttributeError):
    import gettext
    gettext.install(__appname__)

#-------------------------------------------------------------------------------

available_expansions = []
available_expansions.append(_("The King in Yellow"))
available_expansions.append(_("Kingsport"))
available_expansions.append(_("Black Goat of the Woods"))
available_expansions.append(_("The lurker at the Threshold"))

#-------------------------------------------------------------------------------

def choose_expansion(available_expansions):
    """
    TUI that allows the players to choose with which expansions they want to 
    play for this game
    """
    start(function())

    final_expansion_list = []
    final_expansion_list.append(_("Core game"))
    _str = _("You choose to play with:\n")
    _str += "- " + final_expansion_list[0]

    for _iel, exp in enumerate(available_expansions):
        _input = input(_(">> Do you want to play with: ") + exp + _("? [Y/n] "))
        if _input.lower() == "y" or _input.lower() == "yes"\
        or _input.lower() == "o" or _input.lower() == "oui"\
        or _input =="":
            _str += "\n- " + exp
            final_expansion_list.append(exp)
    _str += "\n"

    logging.info(_str)

    end(function())
    return final_expansion_list


#-------------------------------------------------------------------------------

def setup_locations(expansions):
    """
    """
    start(function())
    _xml_file = __xml__ + _("locations_list") + ".xml"
    tree = parse(_xml_file)
    root = tree.getroot()
    locations = []

    for _elt in root:
        for exp in expansions:
            if _elt.find('expansion').text == exp:
                locations.append(Location(_elt))
    end(function())
    return locations


#-------------------------------------------------------------------------------

def choose_investigators(expansion, nb_players):
    """
    TUI that allows the player to choose with which investigator they want to 
    play for this game
    """
    start(function())

    players = []
    names_already_used = []
    investigators_list = Deck(_("investigators_list"), expansion)

    _str  = "-"*TERM_WIDTH + "\n"
    _str += _("There are ") +str(investigators_list.cards_number)\
          + _(" investigators implemented in these expansions:\n")
    for _list, _elt in enumerate(investigators_list.remaining_cards):
        _str += indent(_elt.name, " | " + str(_list) + "/ ")

    players = dict()
    for _iel in range(1, int(nb_players) + 1):
        already_used = False
        while not already_used:
            print(_str)
            player_number = players_color[_iel - 1] + "[Player" + str(_iel)\
                                                    + "]" + RESET
            name = input(player_number + _(" >> choose investigator ") + "n° ")
            if name in names_already_used:
                print(_("This investigator is already taken. ")\
                        + _("Choose another one."))
            elif int(name) > investigators_list.cards_number - 1:
                print(_("Wrong number! Choose a number between 0 and ")\
                     + str(investigators_list.cards_number - 1) + ".")
            else:
                new_player = investigators_list.remaining_cards[int(name)]
                new_player.attribute_player(_iel)
                new_player.setup_inventory(common_items_deck)
                players[_iel] = new_player
                names_already_used.append(name)
                already_used = True
                for _loc in locations_list:
                    if _loc.name == new_player.init_location:
                        new_player.move_to(_loc)

    end(function())
    return players


#-------------------------------------------------------------------------------

def choose_new_investigator(expansion, players, number):
    """
    TUI that allows the player to choose a new investigator during the game
    """
    start(function())

    names_already_used = []
    investigators_list = Deck(_("investigators_list"), expansion)
    logging.info(players[number].player + "has to choose a new investigator.")

    _str += _("There are ") +str(investigators_list.cards_number)\
          + _(" investigators implemented in these expansions:\n")
    for _iel, _elt in enumerate(investigators_list.remaining_cards):
        print(str(_iel) + ": " + _elt.name)

    _str = _("And these investigators are already taken: ")
    for _elt in players.values():
        _str += _elt.name +", "
        names_already_used.append(_elt.name)
    print(_str)

    already_used = False
    while not already_used:
        name = input(">> " + players[number].player\
                    + _("choose investigator ") + "n° ")
        if int(name) > investigators_list.cards_number - 1:
            print(_("Wrong number! Choose a number between 0 and ")\
                 + str(investigators_list.cards_number - 1) + ".")
        else:
            new_name = investigators_list.remaining_cards[int(name)].name
            if new_name in names_already_used:
                print(_("This investigator is already taken. ")\
                        + _("Choose another one."))
            else:
                del players[number]
                new_player = investigators_list.remaining_cards[int(name)]
                new_player.attribute_player(number)
                new_player.setup_inventory(common_items_deck)
                players[number] = new_player
                already_used    = True
                for _loc in locations_list:
                    if _loc.name == new_player.init_location:
                        new_player.move_to(_loc)

    end(function())
    return players

#-------------------------------------------------------------------------------
# Main program driving the setup
#-------------------------------------------------------------------------------

def main_setup():
    start(function())
    logging.info(_("Starting the game !!!"))

    # General game setup: expansions
    chosen_expansions = choose_expansion(available_expansions)

    # General game setup: locations
    global locations_list
    locations_list = setup_locations(chosen_expansions)

    # General game setup: common items
    global common_items_deck
    common_items_deck = Deck(_("common_items_list"), chosen_expansions)

    # General game setup: monsters
    global monsters_deck
    monsters_deck = Deck(_("monsters_list"), chosen_expansions)

    # General game setup: numbers of players
    nb_players = input(_(">> How many are you (choose between 2 and 7)? "))
    logging.info(_("You are ") + str(nb_players) + _(" players") + ".\n")

    players = choose_investigators(chosen_expansions, nb_players)

    return players, locations_list, common_items_deck, monsters_deck

    end(function())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
