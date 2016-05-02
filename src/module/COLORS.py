#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

BLACK       = '\033[0;30m'
RED         = '\033[0;31m'
GREEN       = '\033[0;32m'
YELLOW      = '\033[0;33m'
BLUE        = '\033[0;34m'
PURPLE      = '\033[0;35m'
CYAN        = '\033[0;36m'
GREY        = '\033[0;37m'

BOLD_GREY   = '\033[1;30m'
BOLD_RED    = '\033[1;31m'
BOLD_GREEN  = '\033[1;32m'
BOLD_YELLOW = '\033[1;33m'
BOLD_BLUE   = '\033[1;34m'
BOLD_PURPLE = '\033[1;35m'
BOLD_CYAN   = '\033[1;36m'
BOLD_WHITE  = '\033[1;37m'
BOLD_BLACK  = '\033[1;38m'

HIGHT_BOLD_RED    = '\033[1;41m'
HIGHT_BOLD_GREEN  = '\033[1;42m'
HIGHT_BOLD_YELLOW = '\033[1;43m'
HIGHT_BOLD_BLUE   = '\033[1;44m'
HIGHT_BOLD_PURPLE = '\033[1;45m'
HIGHT_BOLD_CYAN   = '\033[1;46m'
HIGHT_BOLD_GREY   = '\033[1;47m'
HIGHT_BOLD_WHITE  = '\033[1;48m'


RESET = "\033[0m"

players_color = [BOLD_GREEN, BOLD_BLUE, BOLD_RED, BOLD_YELLOW,
                 BOLD_PURPLE, BOLD_CYAN, BOLD_GREY]

TRIANGLE = u"\u25B2".encode("utf-8")
MOON     = u"\u263E".encode("utf-8")
SLASH    = u"\u005C".encode("utf-8")
CIRCLE   = u"\u25CF".encode("utf-8")
PLUS     = u"\u002B".encode("utf-8")
SQUARE   = u"\u25A0".encode("utf-8")
HEXAGON  = u"\u2B22".encode("utf-8")
DIAMOND  = u"\u2666".encode("utf-8")
STAR     = u"\u2736".encode("utf-8")
SYMBOLS  = {"triangle" : TRIANGLE,
            "moon"     : MOON,
            "slash"    : SLASH,
            "circle"   : CIRCLE,
            "plus"     : PLUS,
            "square"   : SQUARE,
            "hexagon"  : HEXAGON,
            "diamond"  : DIAMOND,
            "star"     : STAR}