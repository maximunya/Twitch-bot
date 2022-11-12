import random

characters_banner_additional_drop_probabilities = [
    0.07,
    0.1,
    0.135,
    0.15,
    0.2,
    0.25,
    0.24,
    0.23,
    0.21,
    0.195,
    0.175,
    0.165,
    0.15,
    0.145,
    0.135,
    0.13,
    0.125,
    0.1,
    0.05,
    0.03,
    0.01,
]

weapons_banner_additional_drop_probabilities = [
    0.1,
    0.11,
    0.12,
    0.13,
    0.14,
    0.15,
    0.15,
    0.15,
    0.125,
    0.125,
    0.11,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.08,
    0.04,
]


def get_successful_attempt_for_characters_banner(current_remains=90,
                                                 base_chance=0.6,
                                                 numbers=list(range(1, 91))):
    '''Calculates approximate weights for each attempt of gacha
    in Genshin Impact.

    After that, based on these weights, the function randomly returns
    the number of attempt when user will get a 5*
    character from the character event wish.
    '''
    probabilities = []
    for i in range(1, 70):
        var = current_remains / base_chance
        current_chance = 1 / var
        current_remains -= 1
        probabilities.append(current_chance)
    probabilities += characters_banner_additional_drop_probabilities

    successful_attempt = random.choices(numbers, weights=probabilities)
    return successful_attempt[0]


def get_successful_attempt_for_weapons_banner(current_remains=80,
                                              base_chance=0.6,
                                              numbers=list(range(1, 81))):
    '''Calculates approximate weights for each attempt of gacha
    in Genshin Impact.

    After that, based on these weights, the function randomly returns
    the number of attempt when user will get a 5*
    weapon from the weapon event wish.
    '''
    probabilities = []
    for i in range(1, 60):
        var = current_remains / base_chance
        current_chance = 1 / var
        current_remains -= 1
        probabilities.append(current_chance)
    probabilities += weapons_banner_additional_drop_probabilities

    successful_attempt = random.choices(numbers, weights=probabilities)
    return successful_attempt[0]
