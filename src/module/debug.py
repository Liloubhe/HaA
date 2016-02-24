#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__  = "LB"
__appname__ = 'HaA'

#-------------------------------------------------------------------------------

import sys, logging
from module.COLORS import *
from module.TUI    import TERM_WIDTH

try:
    import i18n.i18n as i18n
    _ = i18n.language.gettext
except (ImportError, AttributeError):
    import gettext
    gettext.install(__appname__)

#-------------------------------------------------------------------------------
# Log config
#-------------------------------------------------------------------------------

__dbg__ = False
if __dbg__:
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level=logging.DEBUG)
else:
    format_date = HIGHT_BOLD_GREY + '%d/%m/%Y %I:%M:%S %p' + RESET
#    format_log  = '%(asctime)s | %(message)s'
    format_log  = '%(message)s'
    logging.basicConfig(format= format_log,
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
