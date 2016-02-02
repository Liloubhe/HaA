#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

from lxml import etree
#from __future__ import print_function


def create_xml_investigator():
    expansion_list = ["Jeu de base",
                      "Le roi en Jaune"]
    home_list      = ["The Bank of Arkham",
                      "The Asylum",
                      "The Hospital"]

    input_name        = raw_input("name? ")
    input_expansion  = choice(expansion_list, "expansion")
    input_occupation = raw_input("occupation? ")
    input_home       = choice(home_list, "Home")
    input_sanity     = raw_input("sanity max? ")
    input_stamina    = raw_input("stamina max? ")
    input_focus      = raw_input("focus? ")
    input_speed_min  = raw_input("speed min? ")
    input_sneak_max  = raw_input("sneak max? ")
    input_fight_min  = raw_input("fight min? ")
    input_will_max   = raw_input("will max? ")
    input_lore_min   = raw_input("lore min? ")
    input_luck_max   = raw_input("luck max? ")

    investigator = etree.Element("investigator")
    investigator.set("name", input_name)
    expansion        = etree.SubElement(investigator, "expansion")
    expansion.text   = input_expansion
    occupation       = etree.SubElement(investigator, "occupation")
    occupation.text  = input_occupation
    home             = etree.SubElement(investigator, "home")
    home.text        = input_home
    sanity           = etree.SubElement(investigator, "sanity")
    sanity.text      = input_sanity
    stamina          = etree.SubElement(investigator, "stamina")
    stamina.text     = input_stamina
    focus            = etree.SubElement(investigator, "focus")
    focus.text       = input_focus

    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "speed")
    speed_min        = etree.SubElement(skill, "min")
    speed_min.text   = input_speed_min
    speed_max        = etree.SubElement(skill, "max")
    speed_max.text   = str(int(input_speed_min) + 3)
    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "sneak")
    sneak_min        = etree.SubElement(skill, "min")
    sneak_min.text   = str(int(input_sneak_max) - 3)
    sneak_max        = etree.SubElement(skill, "max")
    sneak_max.text   = input_sneak_max
    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "fight")
    fight_min        = etree.SubElement(skill, "min")
    fight_min.text   = input_fight_min
    fight_max        = etree.SubElement(skill, "max")
    fight_max.text   = str(int(input_fight_min) + 3)
    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "will")
    will_min         = etree.SubElement(skill, "min")
    will_min.text    = str(int(input_will_max) - 3)
    will_max         = etree.SubElement(skill, "max")
    will_max.text    = input_will_max
    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "lore")
    lore_min         = etree.SubElement(skill, "min")
    lore_min.text    = input_lore_min
    lore_max         = etree.SubElement(skill, "max")
    lore_max.text    = str(int(input_lore_min) + 3)
    skill            = etree.SubElement(investigator, "skill")
    skill.set("name", "luck")
    luck_min         = etree.SubElement(skill, "min")
    luck_min.text    = str(int(input_luck_max) - 3)
    luck_max         = etree.SubElement(skill, "max")
    luck_max.text    = input_luck_max

    inventory        = etree.SubElement(investigator, "inventory")

    investigator_xml = etree.tostring(investigator, pretty_print=True) + "\n"

    return investigator_xml

def choice(choice_list, name):
    _str = name + "? Choose between:\n"
    for _iel, _choice in enumerate(choice_list):
        _str += str(_iel) + ": " + _choice + "\n"
    input_choice  = choice_list[int(raw_input(_str))]

    return input_choice

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------

if __name__ == "__main__":
    print(create_xml_investigator())
