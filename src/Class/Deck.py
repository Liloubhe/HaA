#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the decks.

This module defines the following classes:
- Deck

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

from random import shuffle
from xml.etree.ElementTree import parse
#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from main import __function__, __xml__
from Class.Investigator import Investigator

#-------------------------------------------------------------------------------
# Deck container
#-------------------------------------------------------------------------------

class Deck:
    """
    Class gathering all the informations about a deck
    """
    def __init__(self, xml_file, expansion_list):
        """
        Initializes all the information about the deck
        """
        _xml_file = __xml__ + xml_file + ".xml"
        tree = parse(_xml_file)
        root = tree.getroot()
        self.remaining_cards  = []
        
        for _elt in root.findall(xml_file[:-6]):
            for exp in expansion_list:
                if _elt.find('expansion').text == exp:
                    if xml_file[:-6] == "investigator":
                        self.remaining_cards.append(Investigator(_elt))
        shuffle(self.remaining_cards)
        self.discarding_cards = []
        self.cards_numbers = len(self.remaining_cards)

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
