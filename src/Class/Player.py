#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the player.

This module defines the following classes:
- Player

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
#from __future__ import print_function


#-------------------------------------------------------------------------------
# Player container
#-------------------------------------------------------------------------------

class Player:
    """
    Class gathering all the informations about a player
    """
    def __init__(self, number, investigator):
        """
        Initializes all the information about the player
        """
        self.name         = "[Player" + str(number) + "] "
        self.number       = int(number)
        self.investigator = investigator
        logging.info(self.name + investigator.name + ' is entering the game!')


#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

