from __future__ import annotations
from random import choice, randint, sample
import os.path

import scripts.cat.appearance_utility as util
from scripts.utility import *
from scripts.game_structure.game_essentials import *



class Cat():

    def __init__(self):

        # Private attributes
        self._moons = 0
        
        # Public attributes

        self.age = "adult"
        self.pelt = SingleColour("WHITE", "short")
        self.tint = "none"
        self.eye_colour = "BLUE"
        self.eye_colour2 = None
        self.scars = []
        self.scar_slot_list = [
            None,
            None,
            None,
            None
        ]
        self.dead = False
        self.df = False
        self.tortiebase = "single"
        self.pattern = "ONE"
        self.tortiepattern = "single"
        self.tortiecolour = "GINGER"
        self.white_patches = None
        self.points = None
        self.vitiligo = None
        self.white_patches_tint = "none"
        self.accessory = None
        self.shading = False
        self.cat_sprites = {
            "newborn": 20,
            "kitten": 0,
            "adolescent": 3,
            "adult": 8,
            "senior": 12,
        }
        self.paralyzed = False
        self.not_working = False
        self.current_poses = {
            "newborn": "1",
            "kitten": "1",
            "adolescent": "1",
            "adult": "3",
            "senior": "1",
        }
        self.platform = "None"

        # Helpers:
        self.stored_eye_color_2 = "BLUE"

        self.opacity = 100
        self.reverse = False
        self.skin = "BLACK"

        # Used only for export
        self.ID = "2"
        self.gender = "female"
        self.gender_align = "female"
        self.status = "warrior"
        self.skill = "???"
        self.trait = "troublesome"
        self.backstory = "clan_founder"
        self.moons = 0

        # Sprite sizes
        self.sprite = None

    def randomize_looks(self, just_pattern=False):

        if not just_pattern:
            self.age = choice(["newborn", "kitten", "adult", "adolescent", "senior"])
            util.randomize_sprite(self)
            util.randomize_scars(self)
            util.randomize_accessories(self)
            util.randomize_platform(self)
            lineart = choice(["Star", "Normal", "DF"])
            if lineart == "Star":
                self.dead = True
                self.df = False
            elif lineart == "Normal":
                self.dead = False
                self.df = False
            elif lineart == "DF":
                self.dead = True
                self.df = True

            self.shading = choice([True, False])
        
        util.randomize_pelt(self, change_fur_length=not just_pattern)
        util.randomize_eyes(self)
        util.randomize_white_patches(self)
        util.randomize_pattern(self)
        util.randomize_tint(self)

    def generate_large_image(self):
        return

    def generate_save_file(self):
        """Generates a basic save file dictionary with all the looks-based info filled in. """
        pelt_name = self.pelt.name
        if pelt_name == "SingleColour" and self.white_patches:
            pelt_name = "TwoColour"
        if pelt_name == "Tortie" and self.white_patches:
            pelt_name = "Calico"

        save = {
            "ID": self.ID,
            "name_prefix": "Prefix",
            "name_suffix": "Suffix",
            "gender": self.gender,
            "gender_align": self.gender_align,
            "birth_cooldown": 0,
            "status": self.status,
            "backstory": self.backstory,
            "age": self.age,
            "moons": self.moons,
            "trait": "wise",
            "parent1": None,
            "parent2": None,
            "mentor": None,
            "former_mentor": [],
            "patrol_with_mentor": 0,
            "mentor_influence": [],
            "mate": None,
            "dead": False,
            "died_by": [],
            "paralyzed": self.paralyzed,
            "no_kits": False,
            "exiled": False,
            "pelt_name": pelt_name,
            "pelt_color": self.pelt.colour,
            "pelt_white": bool(self.white_patches),
            "pelt_length": self.pelt.length,
            "spirit_kitten": self.age_sprites["kitten"],
            "spirit_adolescent": self.age_sprites["adolescent"],
            "spirit_young_adult": self.age_sprites["adult"],
            "spirit_adult": self.age_sprites["adult"],
            "spirit_senior_adult": self.age_sprites["adult"],
            "spirit_elder": self.age_sprites["elder"],
            "spirit_dead": None,
            "eye_colour": self.eye_colour,
            "eye_colour2": self.eye_colour2,
            "reverse": self.reverse,
            "white_patches": self.white_patches,
            "vitiligo": self.vitiligo,
            "points": self.points,
            "white_patches_tint": self.white_patches_tint,
            "pattern": self.pattern if self.pelt.name == "Tortie" else None,
            "tortie_base": self.tortiebase if self.pelt.name == "Tortie" else None,
            "tortie_color": self.tortiecolour if self.pelt.name == "Tortie" else None,
            "tortie_pattern": self.tortiepattern if self.pelt.name == "Tortie" else None,
            "skin": self.skin,
            "tint": self.tint,
            "skill": self.skill,
            "scars": [x for x in self.scar_slot_list if x],
            "accessory": self.accessory,
            "experience": 0,
            "dead_moons": 0,
            "current_apprentice": [],
            "former_apprentices": [],
            "possible_scar": None,
            "scar_event": [],
            "df": False,
            "outside": False,
            "corruption": 0,
            "life_givers": [],
            "known_life_givers": [],
            "virtues": [],
            "retired": False,
            "faded_offspring": [],
            "opacity": 100,
            "prevent_fading": False
        }

        return save

# ---------------------------------------------------------------------------- #
#                               END OF CAT CLASS                               #
# ---------------------------------------------------------------------------- #
