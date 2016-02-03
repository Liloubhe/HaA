﻿#!/usr/bin/env python
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

from Class.Deck import Deck
from Class.Player import Player
#from Class.Investigator import Investigator
from main import __function__, __xml__

#-------------------------------------------------------------------------------

def choose_expansion(available_expansions):
    logging.debug("[START] " + __function__())

    final_expansion_list = []
    final_expansion_list.append("Jeu de base")
    _str = "You choose to play with the expansion(s):\n"
    _str += "- " + final_expansion_list[0]

    for _iel, exp in enumerate(available_expansions):
        _input = raw_input(">> Do you want to play with: " + exp + "? (Y/N) ")
        if _input.lower() == "y" or _input.lower() == "yes":
            _str += "\n- " + exp
            final_expansion_list.append(exp)
    _str += "\n"

    logging.info(_str)
    logging.debug("[END] " + __function__())

    return final_expansion_list


#-------------------------------------------------------------------------------

def choose_investigators(expansion, nb_players):
    logging.debug("[START] " + __function__())

    investigators_list = Deck("investigators_list", expansion)
    print("There are " +str(investigators_list.cards_numbers) +
          " investigators implemented in these expansions:")
    for _iel, _elt in enumerate(investigators_list.remaining_cards):
        print(str(_iel) + ": " + _elt.name)

    players = []
    for _iel in range(0, int(nb_players)):
        name = raw_input(">> (Enter a number between 1 and "+\
                           str(investigators_list.cards_numbers) +") Player" +\
                           str(_iel + 1) + " choose investigator " + "n° ")
        
        players.append(Player(_iel + 1,
                              investigators_list.remaining_cards[int(name)]))

    logging.debug("[END] " + __function__())

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

    # General game setup: numbers of players
    nb_players = raw_input(">> How many are you (choose between 2 and 7)? ")
    logging.info("You are " + str(nb_players) + " players\n")

    choose_investigators(chosen_expansions, nb_players)

    logging.debug("[END] " + __function__())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
