#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__  = "LB"
__appname__ = 'HaA'

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import sys, logging, os, inspect

__src__ = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
__xml__ = __src__ + "/../data/xml/"

#from __future__ import print_function
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from setup         import *
from module.COLORS import *
from module.debug  import *

try:
    import i18n.i18n as i18n
    _ = i18n.language.gettext
except (ImportError, AttributeError):
    import gettext
    gettext.install(__appname__)

#-------------------------------------------------------------------------------
# Main program
#-------------------------------------------------------------------------------

def launch_game():
    start(function())

    players, locations_list, common_items_deck, monsters_deck = main_setup()

    end(function())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    launch_game()
