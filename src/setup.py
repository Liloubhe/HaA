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

from Class.Investigator import Investigator
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

def setup_investigators_list(expansion):
    logging.debug("[START] " + __function__())

    xml_file = __xml__ + "investigators_list.xml"
    tree = parse(xml_file)
    root = tree.getroot()
    investigators_list = {}
    _iel = 0
    for _elt in root.findall("investigator"):
        for exp in expansion:
            if _elt.find('expansion').text == exp:
                _iel += 1
                investigators_list[_iel] = _elt

    logging.debug("[END] " + __function__())

    return investigators_list

#-------------------------------------------------------------------------------

def choose_investigators(investigators_list, nb_players):
    logging.debug("[START] " + __function__())

    print("There are " +str(len(investigators_list)) +
          " investigators implemented in these expansions:")
    for _iel, _elt in investigators_list.items():
        print(str(_iel) + ": " + _elt.get('name'))

    players = []
    for _iel in range(0, int(nb_players)):
        name = raw_input(">> (Enter a number between 1 and "+\
                           str(len(investigators_list)) +") Player" +\
                           str(_iel + 1) + " choose investigator " + "n° ")
        for _prev in range(0, _iel):
            if players[_prev].name == investigators_list[int(name)].get('name'):
                print("try again") # TODO test d'erreur
        
        players.append(Investigator(investigators_list[int(name)], _iel + 1))

    logging.debug("[END] " + __function__())

#-------------------------------------------------------------------------------
# Main program driving the setup
#-------------------------------------------------------------------------------

def main_setup():
    logging.debug("[START] " + __function__())
    logging.info("Starting the game !!!")

    # General game setup: expansions
    available_expansion = []
    available_expansion.append("Le roi en Jaune")
    chosen_expansions = choose_expansion(available_expansion)

    # General game setup: numbers of players
    nb_players = raw_input(">> How many are you (choose between 2 and 7)? ")
    logging.info("You are " + str(nb_players) + " players\n")

    available_investigators = setup_investigators_list(chosen_expansions)
    choose_investigators(available_investigators, nb_players)

    logging.debug("[END] " + __function__())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

