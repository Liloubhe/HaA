#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

import sys, logging
from module.COLORS import *

#-------------------------------------------------------------------------------
# Log config
#-------------------------------------------------------------------------------

__dbg__ = False
if __dbg__:
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
else:
    format_date = HIGHT_BOLD_GREY + '%d/%m/%Y %I:%M:%S %p' + RESET
    logging.basicConfig(format='%(asctime)s | %(message)s',
                        datefmt=format_date,
                        level=logging.INFO)

#-------------------------------------------------------------------------------
# Log functions
#-------------------------------------------------------------------------------

def function():
    return sys._getframe(1).f_code.co_name

def start(function):
    msg = HIGHT_BOLD_YELLOW + _("[START] ") + function + RESET
    return logging.debug(msg)

def end(function):
    msg = HIGHT_BOLD_GREEN + _("[END] ") + function + RESET
    return logging.debug(msg)
