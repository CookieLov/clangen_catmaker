import random
from .pelts import *
from scripts.cat.sprites import Sprites

# ---------------------------------------------------------------------------- #
#                               utility functions                              #
# ---------------------------------------------------------------------------- #

def plural_acc_names(accessory, plural, singular):
    acc_display = accessory.lower()
    if acc_display == 'maple leaf':
        if plural:
            acc_display = 'maple leaves'
        if singular:
            acc_display = 'maple leaf'
    elif acc_display == 'holly':
        if plural:
            acc_display = 'holly berries'
        if singular:
            acc_display = 'holly berry'
    elif acc_display == 'blue berries':
        if plural:
            acc_display = 'blueberries'
        if singular:
            acc_display = 'blueberry'
    elif acc_display == 'forget me nots':
        if plural:
            acc_display = 'forget me nots'
        if singular:
            acc_display = 'forget me not flower'
    elif acc_display == 'rye stalk':
        if plural:
            acc_display = 'rye stalks'
        if singular:
            acc_display = 'rye stalk'
    elif acc_display == 'laurel':
        if plural:
            acc_display = 'laurel'
        if singular:
            acc_display = 'laurel plant'
    elif acc_display == 'bluebells':
        if plural:
            acc_display = 'bluebells'
        if singular:
            acc_display = 'bluebell flower'
    elif acc_display == 'nettle':
        if plural:
            acc_display = 'nettles'
        if singular:
            acc_display = 'nettle'
    elif acc_display == 'poppy':
        if plural:
            acc_display = 'poppies'
        if singular:
            acc_display = 'poppy flower'
    elif acc_display == 'lavender':
        if plural:
            acc_display = 'lavender'
        if singular:
            acc_display = 'lavender flower'
    elif acc_display == 'herbs':
        if plural:
            acc_display = 'herbs'
        if singular:
            acc_display = 'herb'
    elif acc_display == 'petals':
        if plural:
            acc_display = 'petals'
        if singular:
            acc_display = 'petal'
    elif acc_display == 'dry herbs':
        if plural:
            acc_display = 'dry herbs'
        if singular:
            acc_display = 'dry herb'
    elif acc_display == 'oak leaves':
        if plural:
            acc_display = 'oak leaves'
        if singular:
            acc_display = 'oak leaf'
    elif acc_display == 'catmint':
        if plural:
            acc_display = 'catnip'
        if singular:
            acc_display = 'catnip sprig'
    elif acc_display == 'maple seed':
        if plural:
            acc_display = 'maple seeds'
        if singular:
            acc_display = 'maple seed'
    elif acc_display == 'juniper':
        if plural:
            acc_display = 'juniper berries'
        if singular:
            acc_display = 'juniper berry'
    elif acc_display == 'red feathers':
        if plural:
            acc_display = 'cardinal feathers'
        if singular:
            acc_display = 'cardinal feather'
    elif acc_display == 'blue feathers':
        if plural:
            acc_display = 'crow feathers'
        if singular:
            acc_display = 'crow feather'
    elif acc_display == 'jay feathers':
        if plural:
            acc_display = 'jay feathers'
        if singular:
            acc_display = 'jay feather'
    elif acc_display == 'moth wings':
        if plural:
            acc_display = 'moth wings'
        if singular:
            acc_display = 'moth wing'
    elif acc_display == 'cicada wings':
        if plural:
            acc_display = 'cicada wings'
        if singular:
            acc_display = 'cicada wing'

    if plural is True and singular is False:
        return acc_display
    elif singular is True and plural is False:
        return acc_display

# ---------------------------------------------------------------------------- #
#                                init functions                                #
# ---------------------------------------------------------------------------- #


def init_eyes(cat):
    cat.eye_colour2 = None

    cat.eye_colour = choice(eye_colours)

    hit = randint(0, 6)
    if hit == 0:
        cat.eye_colour2 = choice(eye_colours)

def randomize_pelt(cat):
    # ------------------------------------------------------------------------------------------------------------#
    #   PELT
    # ------------------------------------------------------------------------------------------------------------#

    # Determine pelt.
    chosen_pelt = choice(
        random.choices(pelt_categories, weights=(35, 20, 30, 15, 0), k=1)[0]
    )

    # Tortie chance
    tortie_chance_f = 3  # There is a default chance for female tortie
    tortie_chance_m = 13
    if cat.gender == "female":
        torbie = random.getrandbits(tortie_chance_f) == 1
    else:
        torbie = random.getrandbits(tortie_chance_m) == 1

    chosen_tortie_base = None
    if torbie:
        # If it is tortie, the chosen pelt above becomes the base pelt.
        chosen_tortie_base = chosen_pelt
        if chosen_tortie_base in ["SingleColour"]:
            chosen_tortie_base = "Single"
        chosen_tortie_base = chosen_tortie_base.lower()
        chosen_pelt = random.choice(torties)

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT COLOUR
    # ------------------------------------------------------------------------------------------------------------#

    chosen_pelt_color = choice(
        random.choices(colour_categories, k=1)[0]
    )

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT LENGTH
    # ------------------------------------------------------------------------------------------------------------#


    chosen_pelt_length = random.choice(["long", "short"])

    # ------------------------------------------------------------------------------------------------------------#
    #   PELT WHITE
    # ------------------------------------------------------------------------------------------------------------#


    chosen_white = random.randint(1, 100) <= 40

    # Adjustments to pelt chosen based on if the pelt has white in it or not.

    cat.pelt = choose_pelt(chosen_pelt_color, chosen_white, chosen_pelt, chosen_pelt_length)
    cat.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.

def init_pelt(cat):
    randomize_pelt(cat)


def init_sprite(cat):
    if cat.pelt is None:
        init_pelt(cat)
    cat.age_sprites = {
        'kitten': randint(0, 2),
        'adolescent': randint(3, 5),
        'elder': randint(3, 5)
    }
    cat.reverse = choice([True, False])
    # skin chances
    cat.skin = choice(skin_sprites)
            
    if cat.pelt is not None:
        if cat.pelt.length != 'long':
            cat.age_sprites['adult'] = randint(6, 8)
        else:
            cat.age_sprites['adult'] = randint(0, 2)


def init_scars(cat):

    cat.scar_slot_list = [
        None,
        None,
        None,
        None,
    ]

    scar_number = random.choices([0,1,2,3,4], weights=[40, 30, 30, 20, 10], k=1)[0]

    i = 0
    all_scars = scars1+scars2+scars3
    while True:
        if i >= scar_number:
            break
        if all_scars:
            add_scar = choice(all_scars)
            cat.scar_slot_list[i] = add_scar
            all_scars.remove(add_scar)
        i += 1


    if 'NOTAIL' in cat.scars and 'HALFTAIL' in cat.scars:
        cat.scars.remove('HALFTAIL')


def init_accessories(cat):
    acc_display_choice = randint(0, 35)
    if cat.age in ['kitten', 'adolescent']:
        acc_display_choice = randint(0, 15)
    elif cat.age in ['young adult', 'adult']:    
        acc_display_choice = randint(0, 50)
    if acc_display_choice == 1:
        cat.acc_display = choice([
            choice(plant_accessories),
            choice(wild_accessories)
        ])
    else:
        cat.acc_display = None


def init_pattern(cat):

    if cat.pelt.name in torties:
        cat.tortiecolour = cat.pelt.colour
        if cat.tortiebase is None:
            cat.tortiebase = choice(tortiebases)
        if cat.tortiebase == 'tabby':
            cat.tortiepattern = 'tortietabby'
        elif cat.tortiebase == 'bengal':
            cat.tortiepattern = 'tortiebengal'
        elif cat.tortiebase == 'marbled':
            cat.tortiepattern = 'tortiemarbled'
        elif cat.tortiebase == 'ticked':
            cat.tortiepattern = 'tortieticked'
        elif cat.tortiebase == 'rosette':
            cat.tortiepattern = 'tortierosette'
        elif cat.tortiebase == 'smoke':
            cat.tortiepattern = 'tortiesmoke'
        elif cat.tortiebase == 'speckled':
            cat.tortiepattern = 'tortiespeckled'
        elif cat.tortiebase == 'mackerel':
            cat.tortiepattern = 'tortiemackerel'
        elif cat.tortiebase == 'classic':
            cat.tortiepattern = 'tortieclassic'
        elif cat.tortiebase == 'sokoke':
            cat.tortiepattern = 'tortiesokoke'
        elif cat.tortiebase == 'agouti':
            cat.tortiepattern = 'tortieagouti'
            cat.tortie_patches_pattern = 'tortieagouti'
        else:
            cat.tortiepattern = choice(['tortietabby', 'tortiemackerel', 'tortieclassic'])

    else:
        cat.tortiebase = None
        cat.tortiepattern = None
        cat.tortiecolour = None

    if cat.pelt.name in torties and cat.pelt.colour is not None:
        if cat.pelt.colour in black_colours:
            cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
                                    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR'])
        elif cat.pelt.colour in brown_colours:
            cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
                                  "DARKONE", "DARKTWO", "DARKTHREE", "DARKFOUR"])
        elif cat.pelt.colour in white_colours:
            cat.pattern = choice(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR'])
        elif cat.pelt.colour in ['DARKGINGER', "GINGER"]:
            cat.pattern = choice(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE',
                                  'CREAMFOUR'])
        elif cat.pelt.colour in ["CREAM", "GOLDEN", "PALEGINGER"]:
            cat.pattern = choice(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR'])
        else:
            cat.pattern = "GOLDONE"
    else:
        cat.pattern = None


def white_patches_inheritance(cat, parents: tuple):

    par_whitepatches = set()
    for p in parents:
        if p and p.white_patches:
            par_whitepatches.add(p.white_patches)

    if not parents:
        print("Error - no parents. Randomizing white patches.")
        randomize_white_patches(cat)
        return

    # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
    if par_whitepatches and not randint(0, 10):
        cat.white_patches = choice(list(par_whitepatches))
        return

    vit_chance = not randint(0, 40)
    if vit_chance:
        cat.white_patches = choice(vit)
        return

    white_list = [little_white, mid_white, high_white, mostly_white, point_markings, ['FULLWHITE']]

    weights = [0, 0, 0, 0, 0, 0]  # Same order as white_list
    for p_ in par_whitepatches:
        if p_ in little_white:
            add_weights = (40, 20, 15, 5, 0, 0)
        elif p_ in mid_white:
            add_weights = (10, 40, 15, 10, 0, 0)
        elif p_ in high_white:
            add_weights = (15, 20, 40, 10, 0, 1)
        elif p_ in mostly_white:
            add_weights = (5, 15, 20, 40, 0, 5)
        elif p_ in point_markings:
            add_weights = (10, 10, 10, 10, 65, 5)
        elif p_ == "FULLWHITE":
            add_weights = (0, 5, 15, 40, 0, 10)
        else:
            add_weights = (0, 0, 0, 0, 0, 0)

        for x in range(0, len(weights)):
            weights[x] += add_weights[x]


    # If all the weights are still 0, that means none of the parents have white patches.
    if not any(weights):
        if not all(parents):  # If any of the parents are None (unknown), use the following distribution:
            weights = [20, 10, 10, 5, 5, 0]
        else:
            # Otherwise, all parents are known and don't have any white patches. Focus distribution on little_white.
            weights = [50, 5, 0, 0, 0, 0]

    # Adjust weights for torties, since they can't have anything greater than mid_white:
    if cat.pelt.name == "Tortie":
        weights = weights[:2] + [0, 0, 0, 0]
        # Another check to make sure not all the values are zero. This should never happen, but better
        # safe then sorry.
        if not any(weights):
            weights = [2, 1, 0, 0, 0, 0]


    chosen_white_patches = choice(
        random.choices(white_list, weights=weights, k=1)[0]
    )

    cat.white_patches = chosen_white_patches

def randomize_white_patches(cat):
    vit_chance = not randint(0, 40)
    if vit_chance:
        cat.white_patches = choice(vit)
        return

    # Adjust weights for torties, since they can't have anything greater than mid_white:
    if cat.pelt.name == "Tortie":
        weights = (2, 1, 0, 0, 0, 0)
    else:
        weights = (10, 10, 10, 10, 5, 1)


    white_list = [little_white, mid_white, high_white, mostly_white, point_markings, ['FULLWHITE']]
    chosen_white_patches = choice(
        random.choices(white_list, weights=weights, k=1)[0]
    )

    cat.white_patches = chosen_white_patches

def init_white_patches(cat):
    if cat.pelt.white:
        randomize_white_patches(cat)
    else:
        cat.white_patches = None


def init_tint(cat):
    # Basic tints as possible for all colors.
    possible_tints = Sprites.cat_tints["possible_tints"]["basic"].copy()
    if cat.pelt.colour in Sprites.cat_tints["colour_groups"]:
        color_group = Sprites.cat_tints["colour_groups"][cat.pelt.colour]
        possible_tints += Sprites.cat_tints["possible_tints"][color_group]
        cat.tint = choice(possible_tints)

