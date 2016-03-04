#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------

"""
This module defines the main application classes for the investigator.

This module defines the following classes:
- Investigator
- Skill
- Inventory

"""

#-------------------------------------------------------------------------------
# Standard modules
#-------------------------------------------------------------------------------

import logging
from random   import randint
from textwrap import wrap

#from __future__ import print_function

#-------------------------------------------------------------------------------
# Application modules
#-------------------------------------------------------------------------------

from module.COLORS import *
from module.debug  import *

#-------------------------------------------------------------------------------
# Investigator container
#-------------------------------------------------------------------------------

class Investigator:
    """
    Class gathering all the informations about an investigator
    """
    def __init__(self, elt):
        """
        Initializes all the information about an investigator
        """
        self.name          = elt.get('name')
        self.init_location = elt.find('home').text
        self.location      = None
        self.occupation    = elt.find('occupation').text
        self.expansion     = elt.find('expansion').text
        self.description   = elt.find('description').text
        self.focus         = int(elt.find('focus').text)
        self.sanity_max    = int(elt.find('sanity').text)
        self.stamina_max   = int(elt.find('stamina').text)

        self.sanity, self.stamina = self.sanity_max, self.stamina_max
        self.blessed, self.cursed, self.account = False, False, False

        self.skill       = {}
        for _iel in elt.findall("skill"):
            self.skill[_iel.get('name')] = Skill(_iel)

        self.skill_line = [(self.skill["speed"], self.skill["sneak"]),
                           (self.skill["fight"], self.skill["will"]),
                           (self.skill["lore"], self.skill["luck"])]

        self.inventory = Inventory(elt.find('inventory'))

#        images_folder = __xml__ + "/images/investigators/"
#        self.image       = images_folder + "default.png"
#        if elt.find('image') is not None:
#            self.image   = images_folder + elt.find('image').text

    def attribute_player(self, number):
        start(function())
        player_name = "[Player" + str(number) + "] "
        self.player = _(players_color[number - 1] + player_name + RESET)
        logging.info(self.player + self.name + ' is entering the game!')
        end(function())


    def setup_inventory(self, common_items_deck):
        start(function())
        for _iel in range(0, self.inventory.common_items_nb):
            new_possession = common_items_deck.draw_card()
            logging.info(self.player + self.name + ' draws a new common item: '
                        + BOLD_BLACK + new_possession.name + RESET)
            print(new_possession)
            self.inventory.common_items.append(new_possession)
        end(function())


    def move_to(self, location):
        start(function())
        if hasattr(self, 'location'):
            self.location.leaving_investigator(self.player + self.name)
        self.location = location
        location.incoming_investigator(self.player + self.name)
        end(function())


    def upkeep(self):
        """
        """
        start(function())
        # Blessing/curse
        if self.blessed or self.cursed:
            dice_roll = randint(1, 6)
            _str = self.name + " is upkeeping the "
            _str += ("blessing:" if self.blessed else "curse:")
            logging.info(_str)
            _str = "Dice result: " + str(dice_roll) + " | " + self.name + " is"
            if dice_roll == 1:
                self.blessed = False
                _str += " no longer "
            else : 
                _str += " still "
            _str += "blessed." if self.blessed else "cursed."
            logging.info(_str)

        # Account
        if self.account:
            self.inventory.money += 2
            dice_roll = randint(1, 6)
            logging.info(self.name + " won 2$ and is upkeeping the account:")
            _str = "Dice result: " + str(dice_roll) + " | " + self.name + " is"
            if dice_roll == 1:
                self.account = False
                _str += " no longer"
            _str += " keeping the account."
            logging.info(_str)
        end(function())

    # Skills
    # ------------

    def initialize_skill(self, place):
        """
        Initializes the skills of the investigator line by line
        """
        start(function())
        for _iel in range(0, 3):
            self.move_skill_to_the_right(_iel, place[_iel] - 1)
        end(function())


    def move_skill_to_the_right(self, line, value):
        """
        Moves the skills'pill of the investigator to the right
        """
        start(function())
        self.skill_line[line][0].move_to_the_right(value)
        self.skill_line[line][1].move_to_the_right(value)
        end(function())


    def move_skill_to_the_left(self, line, value):
        """
        Moves the skills'pill of the investigator to the left
        """
        start(function())
        self.skill_line[line][0].move_to_the_left(value)
        self.skill_line[line][1].move_to_the_left(value)
        end(function())


    # Sanity
    # ------------

    def increase_sanity(self, value = 1):
        """
        Increases (if possible) the sanity of the investigator
        """
        start(function())
        if self.sanity < self.sanity_max:
            self.sanity += value
            self.sanity = min(self.sanity, self.sanity_max)
            logging.info("Sanity gain (" + str(value) + ") | "\
                        + "new " + self.name + "'s sanity: "\
                        + str(self.sanity) + "/" + str(self.sanity_max))
        else:
            logging.info("Sanity gain (" + str(value) + ") | "\
                        + self.name + "'s sanity already to the max ("\
                        + str(self.sanity_max) + ")")
        end(function())


    def decrease_sanity(self, value = 1):
        """
        Decreases the sanity of the investigator
        """
        start(function())
        if self.sanity > 0:
            self.sanity -= value
            self.sanity = max(self.sanity, 0)
            logging.info("Sanity loss (" + str(value) + ") | "\
                        + "new " + self.name + "'s sanity: "\
                        + str(self.sanity) + "/" + str(self.sanity_max))
        if self.sanity == 0:
            self.become_crazy()
        end(function())


    def become_crazy(self):
        start(function())
        self.location = "Arkham Asylum"
        logging.info(self.name + " becomes crazy")
        logging.info(self.name + " is going to the " + self.location)
        logging.warning("the function 'become_crazy' is not implemented")
        end(function())


    # Stamina
    # -------------

    def increase_stamina(self, value = 1):
        """
        Increases (if possible) the stamina of the investigator
        """
        start(function())
        if self.stamina < self.stamina_max:
            self.stamina += value
            self.stamina = min(self.stamina, self.stamina_max)
            logging.info("Stamina gain (" + str(value) + ") | "\
                        + "new " + self.name + "'s stamina: "\
                        + str(self.stamina) + "/" + str(self.stamina_max))
        else:
            logging.info("Stamina gain (" + str(value) + ") | "\
                        + self.name + "'s stamina already to the max ("\
                         + str(self.stamina_max) + ")")
        end(function())


    def decrease_stamina(self, value = 1):
        """
        Decreases the stamina of the investigator
        """
        start(function())
        if self.stamina > 0:
            self.stamina -= value
            self.stamina = max(self.stamina, 0)
            logging.info("Stamina loss (" + str(value) + ") | "\
                        + "new " + self.name + "'s sanity: "\
                        + str(self.stamina) + "/" + str(self.stamina_max))
        if self.stamina == 0:
            self.fall_unconscious()
        end(function())


    def fall_unconscious(self):
        start(function())
        self.location = "St. Mary's Hospital"
        logging.info(self.name + " falls unconscious")
        logging.info(self.name + " is going to the " + self.location)
        logging.warning("the function 'fall_unconscious' is not implemented")
        end(function())


    # Displaying info in text
    # -----------------------

    def __str__(self):
        """
        Displays (in the shell) all the characteristics of the investigator
        """
        start(function())
        _str = "="*40 + "\n"
        _str += self.name + "\n(" + self.occupation + ")\n" + _str

        description_split = self.description.split('| ')
        for i in range(len(description_split)):
            for line in wrap(description_split[i], 40):
                _str += line + "\n"
        _str += "-"*40 + "\n"

        _str += "Sanity:  " + str(self.sanity) + "/" + str(self.sanity_max)
        _str += "\nStamina: " + str(self.stamina) + "/" + str(self.stamina_max)
        if self.blessed:
            _str += "\n... and is blessed!\n"
        if self.cursed:
            _str += "\n... and is cursed!\n"
        _str += "\n\n(Focus: " + str(self.focus) + ")\n"
        
        for __i, _iel in enumerate(["speed", "sneak", "fight",
                                    "will", "lore", "luck"]):
            if __i % 2 == 0:
                _str += "-"*40 + "\n"
            _str += self.skill[_iel].__str__()
        _str += "-"*40 + "\n\n" 
        _str += self.inventory.__str__()
        _str += "\n(Actual location: " + self.location.name + ")\n"
        _str +=  "="*40 + "\n\n"
        end(function())

        return _str


#-------------------------------------------------------------------------------
# Skill container
#-------------------------------------------------------------------------------

class Skill:
    """
    Class gathering all the informations about a particular skill of an
    investigator
    """
    def __init__(self, _skill):
        """
        Initializes the class
        """
        self.name  = _skill.get("name")
        self.place = 0
        _min, _max = int(_skill.get('min')), int(_skill.get('max'))
        if self.name == "sneak" or self.name == "will" or self.name == "luck":
            self.range = list(reversed(range(_min, _max +1)))
        else: 
            self.range = range(_min, _max + 1)

        # TODO : à lier plus précisément avec self.place
        self.value = self.range[self.place]


    def __str__(self):
        """
        Creates a string containing the investigator's skill information
        """
        start(function())
        _str = self.name + (" "*6 if len(self.name) < 5 else " "*5)
        for _nb, _iel in enumerate(self.range):
            if   _nb == self.place:
                _str += "   [ "
            elif _nb == self.place + 1:
                _str += " ]   "
            else:
                _str += "     "
            _str += str(_iel)
        _str += "  ]\n" if self.place == 3 else "\n"
        end(function())

        return _str


    def move_to_the_right(self, value):
        """
        Moves the skill's pill of the investigator to the right
        """
        start(function())
        self.place += value
        self.place = min(self.place, 3)
        self.value = self.range[self.place]
        end(function())


    def move_to_the_left(self, value):
        """
        Moves the skill's pill of the investigator to the left
        """
        start(function())
        self.place -= value
        self.place = max(0, self.place)
        self.value = self.range[self.place]
        end(function())

#-------------------------------------------------------------------------------
# Inventory container
#-------------------------------------------------------------------------------

class Inventory:
    """
    Class gathering all the informations about the inventory of an investigator
    """
    def __init__(self, elt):
        """
        Initializes the class
        """
        self.money       = 0
        self.clue_tokens = 0
        if elt.find('money') is not None:
            self.money       = int(elt.find('money').text)
        if elt.find('clue_tokens') is not None:
            self.clue_tokens = int(elt.find('clue_tokens').text)

        self.common_items, self.common_items_nb = [], 0
        if elt.find("common_items") is not None:
            self.common_items_nb = int(elt.find('common_items').text)


    def __str__(self):
        """
        Creates a string containing the investigator's inventory information
        """
        start(function())
        _str  = "Inventory:\n" + "-"*10 + "\n"
        _str += "Money       : " + str(self.money)       + "$\n"
        _str += "Clue tokens : " + str(self.clue_tokens) + "\n"
        _str += "Common items: " + str(self.common_items_nb) + "\n"
        for _iel in self.common_items:
            _str += _iel.__str__()
        end(function())

        return _str

#-------------------------------------------------------------------------------
# End
#-------------------------------------------------------------------------------
