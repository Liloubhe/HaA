#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the locations.

This module defines the following classes:
- Location

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from random import randint
from xml.etree.ElementTree import parse

#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from module.COLORS import BOLD_BLACK, RESET

#-------------------------------------------------------------------------------
# Investigator container
#-------------------------------------------------------------------------------

class Location:
    """
    Class gathering all the informations about a location
    """
    def __init__(self, elt):
        """
        Initializes all the information about a location
        """
        self.name         = elt.get('name')
        self.name_colored = BOLD_BLACK + self.name + RESET
        self.expansion    = elt.find('expansion').text
        self.neighborhood = elt.find('neighborhood').text
        self.neighbors    = []
        for neighbor in elt.findall('neighbor'):
            self.neighbors.append(neighbor.get('name'))

        self.aquatic      = elt.get('aquatic', default=False)
        self.unstable     = elt.get('unstable', default=False)
        self.clue_tokens  = 1 if self.unstable else 0

        self.investigators, self.monsters, self.portal = [], [], []
        print(self)

    def incoming_investigator(self, investigator_name):
        logging.info(investigator_name + " arrives in: " + self.name_colored)
        self.investigators.append(investigator_name)

    def leaving_investigator(self, investigator_name):
        logging.info(investigator_name + " is leaving: " + self.name_colored)
        self.investigators.remove(investigator_name)

    def __str__(self):
        """
        Displays (in the shell) all the characteristics about the location
        """
        _str = self.name + "\n" + "=" * len(self.name) + "\n"
        if self.unstable:
            _str += "(unstable location)\n"
        if self.aquatic:
            _str += "(aquatic location)\n"

        _str += "- clue token(s)   : " + str(self.clue_tokens)
        _str += "\n- investigator(s) : "
        if len(self.investigators) >0:
            _str += ', '.join(self.investigators)
        else:
            _str += "None"
        _str += "\n- monster(s)      : "
        if len(self.monsters) >0:
            _str += ', '.join(self.monsters)
        else:
            _str += "None"
        _str += "\n- portal          : "
        if len(self.portal) >0:
            _str += ', '.join(self.portal)
        else:
            _str += "None"

        _str += "\n\nLocations accessibles from here:\n" + "-"*32 + "\n"
        for _iel, neighbor in enumerate(self.neighbors):
            if len(self.neighbors) > 1:
                _str += " | " + str(_iel + 1) + ": " + neighbor + "\n"
            else:
                _str += " | " + neighbor + "\n"

        return _str

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    _xml_file = "../../data/xml/locations_list.xml"
    tree = parse(_xml_file)
    root = tree.getroot()
    for _elt in root:
        where = Location(_elt)
        print(where)
