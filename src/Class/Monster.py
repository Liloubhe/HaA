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
# Global
#-------------------------------------------------------------------------------

MOVEMENT = {"normal"     : BOLD_BLACK,
            "flying"     : BOLD_BLUE,
            "stationary" : BOLD_YELLOW,
            "unique"     : BOLD_GREEN,
            "fast"       : BOLD_RED,
            "stalker"    : BOLD_PURPLE,
            "aquatic"    : BOLD_CYAN}
            

#-------------------------------------------------------------------------------
# Monster container
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
        self.expansion       = elt.find("expansion").text
        self.count           = int(elt.find("count").text)
        print(_("We put ") + str(self.count)\
                + _(" card") + ("s" if self.count > 1  else "") \
                +" '" + self.name +  _("' on the bag."))
        
        self.location        = None
        self.abilities       = []
        for _spec in elt.findall("specifications"):
            self.movemement = _spec.get("movemement")
            self.symbole    = SYMBOLS.get(_spec.get("dimension"), "-")
            self.color      = MOVEMENT.get(self.movemement, BOLD_GREY)
        
        self.description     = None
        if elt.find("description") is not None:
            self.description = str(elt.find("description").text)
        for _ability in elt.findall("abilities"):
            name = _ability.get("name")
            if _ability.get("value"):
                name +=  " [" + str(_ability.get("value")) + "]"
            self.abilities.append(name)

        self.awareness = int(elt.find("awareness").text)
        for _stat in elt.findall("combat_stat"):
            self.toughness     = int(_stat.find("toughness").text)
            self.horror_rating, self.horror_damage = "-", "-"
            self.combat_rating, self.combat_damage = "-", "-"
            if _stat.find("horror") is not None:
                if _stat.find("horror").get("rating"):
                    self.horror_rating = int(_stat.find("horror").get("rating"))
                if _stat.find("horror").get("damage"):
                    self.horror_damage = int(_stat.find("horror").get("damage"))
                    
            if _stat.find("combat") is not None:
                if _stat.find("combat").get("rating"):
                    self.combat_rating = int(_stat.find("combat").get("rating"))
                if _stat.find("combat").get("damage"):
                    self.combat_damage = int(_stat.find("combat").get("damage"))
        print(self)
    
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
        for _iel in self.abilities:
            _str += indent(_iel)
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
                            + " "*8 + str(self.toughness) + RED\
                            + " "*8 + str(self.combat_rating)\
                            + " "*8 + str(self.combat_damage) + RESET)
        _str += indent("-"*45 + "\n")
        return _str

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
