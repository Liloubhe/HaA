#!/usr/bin/env python
# -*- coding: utf-8 -*-


#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from xml.etree.ElementTree import parse
#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from main import __function__, __xml__
from Class.Deck     import Deck
from Class.Location import Location
from Class.Player   import Player

#-------------------------------------------------------------------------------
global locations_list
#-------------------------------------------------------------------------------

def choose_expansion(available_expansions):
    """
    TUI that allows the players to choose with which expansions they want to 
    play for this game
    """
    logging.debug("[START] " + __function__())

    final_expansion_list = []
    final_expansion_list.append("Jeu de base")
    _str = "You choose to play with the expansion(s):\n"
    _str += "- " + final_expansion_list[0]

    for _iel, exp in enumerate(available_expansions):
        _input = raw_input(">> Do you want to play with: " + exp + "? [Y/n] ")
        if _input.lower() == "y" or _input.lower() == "yes" or _input =="":
            _str += "\n- " + exp
            final_expansion_list.append(exp)
    _str += "\n"

    logging.info(_str)

    logging.debug("[END] " + __function__())
    return final_expansion_list


#-------------------------------------------------------------------------------

def setup_locations(expansions):
    """
    """
    _xml_file = __xml__ + "locations_list.xml"
    tree = parse(_xml_file)
    root = tree.getroot()
    locations_list = []

    for _elt in root:
        for exp in expansions:
            if _elt.find('expansion').text == exp:
                locations_list.append(Location(_elt))
    return locations_list


#-------------------------------------------------------------------------------

def choose_investigators(expansion, nb_players):
    """
    TUI that allows the player to choose with which investigator they want to 
    play for this game
    """
    logging.debug("[START] " + __function__())

    players = []
    names_already_used = []
    investigators_list = Deck("investigators_list", expansion)

    print("There are " +str(investigators_list.cards_number) +
          " investigators implemented in these expansions:")
    for _iel, _elt in enumerate(investigators_list.remaining_cards):
        print(str(_iel) + ": " + _elt.name)

    for _iel in range(0, int(nb_players)):
        already_used = False
        while not already_used:
            name = raw_input(">> [Player" + str(_iel + 1)\
                            + "] choose investigator " + "n° ")
            if name in names_already_used:
                print("This investigator is already taken. Choose another one.")
            elif int(name) > investigators_list.cards_number - 1:
                print("Wrong number! Choose a number between 0 and "\
                     + str(investigators_list.cards_number - 1) + ".")
            else:
                players.append(Player(_iel + 1, 
                               investigators_list.remaining_cards[int(name)]))
                names_already_used.append(name)
                already_used = True

    logging.debug("[END] " + __function__())
    return players


#-------------------------------------------------------------------------------

def choose_new_investigator(expansion, players, number):
    """
    TUI that allows the player to choose a new investigator during the game
    """
    logging.debug("[START] " + __function__())

    names_already_used = []
    investigators_list = Deck("investigators_list", expansion)
    logging.info(players[number - 1].name + "has to choose a new investigator.")

    print("There are " +str(investigators_list.cards_number) +
          " investigators implemented in these expansions:")
    for _iel, _elt in enumerate(investigators_list.remaining_cards):
        print(str(_iel) + ": " + _elt.name)

    _str = "And these investigators are already taken: "
    for _elt in players:
        _str += _elt.investigator.name +", "
        names_already_used.append(_elt.investigator.name)
    print(_str)

    already_used = False
    while not already_used:
        name = raw_input(">> " + players[number - 1].name\
                        + "choose investigator " + "n° ")
        if int(name) > investigators_list.cards_number - 1:
            print("Wrong number! Choose a number between 0 and "\
                 + str(investigators_list.cards_number - 1) + ".")
        else:
            new_name = investigators_list.remaining_cards[int(name)].name
            if new_name in names_already_used:
                print("This investigator is already taken. Choose another one.")
            else:
                players[number - 1] = Player(number, 
                                  investigators_list.remaining_cards[int(name)])
                already_used    = True

    logging.debug("[END] " + __function__())
    return players

#-------------------------------------------------------------------------------
# Main program driving the setup
#-------------------------------------------------------------------------------

def main_setup():
    logging.debug("[START] " + __function__())
    logging.info("Starting the game !!!")

    # General game setup: expansions
    available_expansions = []
    available_expansions.append("Le roi en Jaune")
    chosen_expansions = choose_expansion(available_expansions)

    # General game setup: locations
    locations_list = setup_locations(chosen_expansions)

    # General game setup: numbers of players
    nb_players = raw_input(">> How many are you (choose between 2 and 7)? ")
    logging.info("You are " + str(nb_players) + " players\n")

    players = choose_investigators(chosen_expansions, nb_players)

    logging.debug("[END] " + __function__())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
