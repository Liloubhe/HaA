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

from main import __xml__
from module.debug       import *
from Class.Investigator import Investigator
from Class.CommonItem   import CommonItem

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
        self.remaining_cards, self.discarding_cards = [], []

        cut = xml_file.find('_list')-len(xml_file)-1
        for _elt in root.findall(xml_file[:cut]):
            for exp in expansion_list:
                if _elt.find('expansion').text == exp:
                    if xml_file.find("investigator") > -1:
                        self.remaining_cards.append(Investigator(_elt))
                    elif xml_file.find("common_item") > -1:
                        new_item = CommonItem(_elt)
                        for _iel in range(0, new_item.count):
                            self.remaining_cards.append(new_item)
        shuffle(self.remaining_cards)
        self.cards_number = len(self.remaining_cards)

    def pick_card(self):
        """
        Picks the first card of the deck (and remove it from the deck)
        """
        card = self.remaining_cards.pop(0)
        return card

    def discard_card(self, card):
        """
        Discards the card on the discard deck
        """
        self.discarding_cards.append(card)

    def mix(self):
        """
        Mixes the discard deck with the remaining cards
        """
        for _iel in self.discarding_cards:
            self.remaining_cards.append(_iel)
        self.discarding_cards = []
        shuffle(self.remaining_cards)

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
