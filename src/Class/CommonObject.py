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
#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from main import __function__, ___dbg___

#-------------------------------------------------------------------------------
# Common Object container
#-------------------------------------------------------------------------------

class CommonObject:
    """
    Class gathering all the informations about a common object
    """
    def __init__(self, elt):
        """
        Initializes all the information about a common object
        """
        self.name        = elt.get('name')
        self.expansion   = elt.find('expansion').text
        self.cost        = int(elt.find('cost').text)
        self.hands       = 0
        if elt.find('hands') is not None:
            self.hands       = int(elt.find('hands').text)


        images_folder = __xml__ + "/images/common_objects/"
        self.image       = images_folder + "default.png"
        if elt.find('image') is not None:
            self.image   = images_folder + elt.find('image').text

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

