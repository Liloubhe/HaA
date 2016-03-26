#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the monster.

This module defines the following classes:
- Monster

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from random   import randint
from textwrap import wrap

#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from module.COLORS import *
from module.TUI    import *

#-------------------------------------------------------------------------------
# Investigator container
#-------------------------------------------------------------------------------

class Monster:
    """
    Class gathering all the informations about a monster
    """
    def __init__(self, elt):
        """
        Initializes all the information about a monster
        """
        self.name            = elt.get("name")
        print("On met les " + self.name + " dans la tasse.")
        self.expansion       = elt.find("expansion").text
        self.count           = int(elt.find("count").text)
        self.location        = None
        for _spec in elt.findall("specifications"):
            self.movemement  = _spec.get("movemement")
            self.dimension   = _spec.get("dimension")
            if self.dimension == "triangle":
                self.symbole = u"\u25B2".encode("utf-8")
            elif self.dimension == "moon":
                self.symbole = u"\u263E".encode("utf-8")

        if self.movemement == "normal":
            self.color = BOLD_BLACK
        elif self.movemement == "flying":
            self.color = BOLD_BLUE
        self.description     = None
        if elt.find("description") is not None:
            self.description = str(elt.find("description").text)
        if elt.find("abilities") is not None:
            self.abilities = elt.find("abilities").get("name")

        self.awareness = int(elt.find("awareness").text)
        for _stat in elt.findall("combat_stat"):
            self.toughness     = int(_stat.find("toughness").text)
            # bug
            self.horror_rating = int(_stat.find("horror").get("rating"))
            self.horror_damage = int(_stat.find("horror").get("damage"))
            self.combat_rating = int(_stat.find("combat").get("rating"))
            self.combat_damage = int(_stat.find("combat").get("damage"))

    # Displaying info in text
    # -----------------------

    def __str__(self):
        """
        Displays (in the shell) all the characteristics of the monster
        """
        _str = indent(self.name, color = self.color)
        _str += indent("-"*len(self.name))
        _str += indent("( " + self.movemement + " - "+ self.symbole + " )")
        _str += indent("Awareness: " + str(self.awareness))
        if self.abilities is not None:
            _str += indent(self.abilities)
        if self.description is not None:
            _str += indent("-"*45 + "\n")
            _str += indent(self.description)
        _str += indent("-"*45 + "\n")
        _str += indent(BOLD_BLACK + " "*15 + "Combat Stats" + RESET)
        _str += indent("-"*45 + "\n")
        _str += indent(BLUE + "     Horror" + RESET + "      Toughness"\
                      + RED + "       Combat" + RESET)
        _str += indent(BLUE + "Rating   Damage             "\
                      + RED + "Rating   Damage")
        _str += indent(BLUE + " "   + str(self.horror_rating)\
                            + " "*8 + str(self.horror_damage) + RESET\
                            + " "*8 + str(self.awareness) + RED\
                            + " "*8 + str(self.combat_rating)\
                            + " "*8 + str(self.combat_damage) + RESET)
        _str += indent("-"*45 + "\n")
        return _str

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
