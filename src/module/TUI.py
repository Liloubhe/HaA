#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

import os
from module.COLORS import *
from textwrap import wrap

TERM_HIGHT, TERM_WIDTH = os.popen('stty size', 'r').read().split()

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
    indent_width  = int(TERM_WIDTH) - len(idt)
    for line in wrap(msg, width = indent_width):
        tmp_line = "".join(wrap(line, initial_indent = idt))
        formatted_msg.append(tmp_line + "\n")

    return color + "".join(formatted_msg) + RESET
