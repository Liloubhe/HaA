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

#from main import __function__, ___dbg___

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
        self.expansion    = elt.find('expansion').text
        self.neighborhood = elt.find('neighborhood').text
        self.neighbors    = []
        for neighbor in elt.findall('neighbor'):
            self.neighbors.append(neighbor.get('name'))

        self.aquatic  = True if elt.find('aquatic') is not None else False
        if elt.find('unstable') is not None:
            self.unstable, self.clue_tokens = True, 1
        else:
            self.unstable, self.clue_tokens = False, 0

        # Is there something in this place?
        self.investigators = []
        self.monsters      = []
        self.portal        = []

    def display(self, verbosity = 1):
        """
        Displays (in the shell) all the characteristics about the location
        """
        _str = self.name + "\n" + "=" * len(self.name) + "\n"
        if self.unstable:
            _str += "--> unstable location\n"
        if self.aquatic:
            _str += "--> aquatic location\n"

        _str += "- clue token(s):   " + str(self.clue_tokens) + "\n"
        _str += "- investigator(s): "
        if len(self.investigators) >0:
            _str += ', '.join(self.investigators)
        else:
            _str += "None\n"
        _str += "- monster(s):      "
        if len(self.monsters) >0:
            _str += ', '.join(self.monsters)
        else:
            _str += "None\n"
        _str += "- portal:          "
        if len(self.portal) >0:
            _str += ', '.join(self.portal)
        else:
            _str += "None\n"

        if verbosity > 1:
            _str += "\nLocations accessibles from here:\n" + "-"*32 + "\n"
            for _iel, neighbor in enumerate(self.neighbors):
                if len(self.neighbors) > 1:
                    _str += " | " + str(_iel + 1) + ": " + neighbor + "\n"
                else:
                    _str += " | " + neighbor + "\n"

        print(_str)

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    _xml_file = "../../data/xml/locations_list.xml"
    tree = parse(_xml_file)
    root = tree.getroot()
    for _elt in root:
        where = Location(_elt)
        where.display()
