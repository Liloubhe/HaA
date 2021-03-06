#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the common object.

This module defines the following classes:
- 

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from textwrap import wrap
#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from module.COLORS import *
#from module.debug  import *
from module.TUI import *

#-------------------------------------------------------------------------------
# Common Object container
#-------------------------------------------------------------------------------

class CommonItem:
    """
    Class gathering all the informations about a common item
    """
    def __init__(self, elt):
        """
        Initializes all the information about a common item
        """
        self.name        = elt.get('name')
        self.expansion   = elt.find('expansion').text
        self.count       = int(elt.find('count').text)
        self.cost        = int(elt.find('cost').text)
        self.hands       = 0
        self.type, self.bonus, self.description = None, None, None
        if elt.find('description') is not None:
            self.description = str(elt.find('description').text)
        if elt.find('type') is not None:
            self.type        = elt.find('type').get('name')
            if elt.find('type').find('hands') is not None:
                self.hands   = int(elt.find('type').find('hands').text)
        if elt.find('bonus') is not None:
            self.bonus       = elt.find('bonus').text

#        images_folder = __xml__ + "/images/common_objects/"
#        self.image       = images_folder + "default.png"
#        if elt.find('image') is not None:
#            self.image   = images_folder + elt.find('image').text

    # Displaying info in text
    # -----------------------

    def __str__(self):
        """
        Displays (in the shell) all the characteristics of the common item
        """
        _str = indent(self.name, color = BOLD_BLACK)
        _str += indent("-"*len(self.name))
        _str += indent("Cost: " + str(self.cost) + "$")
        
        if self.type is not None:
            _str += indent("Type: " + self.type)
        if self.hands > 0:
            _str += indent("Require " + str(self.hands) + " hand"\
                           + ("s" if self.hands > 1 else ""))
        if self.description is not None:
            _str += indent(self.description)
        if self.bonus is not None:
            _str += indent("Bonus: " + self.bonus)
        
        return _str
#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
