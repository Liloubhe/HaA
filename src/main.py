#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "LB"

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

from setup import *

#-------------------------------------------------------------------------------
# Log config
#-------------------------------------------------------------------------------

__dbg__ = False
if __dbg__:
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s | %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        level=logging.INFO)

def __function__():
    return sys._getframe(1).f_code.co_name

#-------------------------------------------------------------------------------
# Main program
#-------------------------------------------------------------------------------

def launch_game():
    logging.debug("[START] " + __function__())

    players, locations_list, common_items_deck = main_setup()

    logging.debug("[END] " + __function__())

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    launch_game()
