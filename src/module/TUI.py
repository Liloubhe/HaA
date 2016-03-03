#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

import os
from module.COLORS import *
from textwrap import wrap

try:
    TERM_HIGHT, TERM_WIDTH = os.popen('stty size', 'r').read().split()
    TERM_HIGHT, TERM_WIDTH = int(TERM_HIGHT), int(TERM_WIDTH)
except:
    TERM_HIGHT, TERM_WIDTH = 40, 80

def indent(msg, idt = " | ", color = RESET):
    """
    Provide indented message in a wanted color

    Input:
        msg           : message
        idt           : type of indentation
        color         : the wanted color

    Output:
        formatted_msg : indented message in a wanted color
    """
    formatted_msg = []
    msg           = msg.split(" | ")
    width         = TERM_WIDTH - len(idt)
    for _iel in range(0, len(msg)):
        for line in wrap(msg[_iel], width = width):
            tmp_line = " ".join(wrap(line, initial_indent = idt))
            formatted_msg.append(tmp_line + "\n")

    return color + "".join(formatted_msg) + RESET
