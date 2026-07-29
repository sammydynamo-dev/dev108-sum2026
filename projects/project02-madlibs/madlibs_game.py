#!/usr/bin/env python3
"""Mad Libs game engine for the conditional twist story generator."""

import random
from time import sleep
import tracery
from tracery.modifiers import base_english

from cli_ui import (
    WIDTH,
    choose_story_idea,
    collect_user_inputs,
    display_game_overview,
    greet_player,
    print_section_header,
    print_story_card,
    play_again,
)

TEMPLATES = {
    "road_tale": {
        "text": (
            "The legend of #hero# began on a dark night when they boarded #vehicle.a# "
            "with nothing but a pocket full of #food#.\n\n"
            "Suddenly, #twist_for# "
            "Our hero reacted by unleashing a battle cry: '#dialogue_for#!' "
            "The event went down in history as the most #vibe_input# moment of the century."
        ),
        "fields": ["hero", "vehicle", "food", "vibe"],
    },
    "haunted_house": {
        "text": (
            "#hero# crept across the rotten floorboards of the abandoned manor, clutching only a #flashlight# flashlight.\n\n"
            "A sudden #scary_sound# echoed from the attic. #twist_for# "
            "In a hushed voice #hero# whispered: '#dialogue_for#!' The house seemed to swallow the words."
        ),
        "fields": ["hero", "flashlight", "scary_sound"],
    },
    "cooking_fiasco": {
        "text": (
            "Chef #chef# prepared a masterpiece using a humble #ingredient# and a trusty #utensil#.\n\n"
            "Without warning, #twist_for# "
            "Chef #chef# shouted: '#dialogue_for#!' The kitchen never smelled the same again."
        ),
        "fields": ["chef", "ingredient", "utensil"],
    },
    "space_mission": {
        "text": (
            "Commander #astronaut# piloted the #ship# toward #planet#, carrying only a snack pack and a sense of destiny.\n\n"
            "Suddenly, #twist_for# "
            "They radioed back: '#dialogue_for#!' Mission control logged the incident as Anomaly #vibe_input#."
        ),
        "fields": ["astronaut", "ship", "planet", "vibe"],
    },
}

PROMPT_MAP = {
    "hero": "character's name",
    "vehicle": "vehicle",
    "food": "type of food",
    "flashlight": "brand or color of a flashlight",
    "scary_sound": "scary sound",
    "chef": "chef's name",
    "ingredient": "ingredient",
    "utensil": "kitchen utensil",
    "astronaut": "astronaut's name",
    "ship": "name/type of spaceship",
    "planet": "planet name",
}

TWIST_DIALOGUE_RULES = {
    "twist_for_creepy": [
        "a shadowy figure appeared, whispering secrets of the underworld.",
        "the ground cracked open, revealing a portal to another dimension.",
        "the shadows detached themselves from the walls and began whispering ancient secrets.",
        "a pair of glowing red eyes blinked from inside the dashboard, freezing them with fear.",
        "time stopped completely, and the distant sound of a music box began to play backward.",
        "the radio started playing lullabies backwards, and a child's laugh echoed from the trunk.",
        "the rearview mirror reflected a different city entirely, where no one ever aged.",
        "a cold hand tapped the passenger seat, though no one was sitting there.",
    ],
    "dialogue_for_creepy": [
        "I must face the darkness!",
        "This is only the beginning of my nightmare!",
        "the shadows are watching us",
        "it is already too late to turn back",
        "who turned off the gravity",
        "I hear them whisper my name",
        "Do not look behind you",
    ],
    "twist_for_silly": [
        "a parade of dancing penguins blocked the path, demanding a snack.",
        "a giant rubber duck floated down the street, honking loudly.",
        "a clown wearing a jetpack smashed through the window and started throwing cream pies.",
        "their vehicle suddenly transformed into a giant, rolling piece of string cheese.",
        "a flash mob of dancing penguins surrounded them, demanding a sacrificial TikTok dance.",
        "a troupe of breakdancing llamas blocked the intersection and insisted on a dance-off.",
        "the streetlights began to blink in rhythm with a funky bassline, and a disco ball descended.",
        "an ice cream truck pursued them, playing heavy metal and offering free samples.",
    ],
    "dialogue_for_silly": [
        "I'm not a duck, I'm a hero!",
        "This is the most ridiculous thing I've ever done!",
        "honk honk, out of my way",
        "I blame the internet for this",
        "this is completely unhinged",
        "Do you accept payment in jellybeans?",
        "Please stop tickling my cape!",
        "Who hired the circus for this emergency?",
    ],
    "twist_for_cooking": [
        "the sauce bubbled into a small, singing geyser.",
        "the oven began to moonwalk across the kitchen floor.",
        "the spices formed a tiny tornado and swept the counter clean.",
        "the spoon melted into a perfect ladle-shaped hat.",
    ],
    "dialogue_for_cooking": [
        "That's not how you flambé a planet!",
        "Someone call a plumber—this soup is boiling over into another dimension!",
        "I require more butter to finish this ritual",
        "Who invited the sentient soufflé?",
    ],
}


def choose_story_template():
    chosen_key = random.choice(list(TEMPLATES.keys()))
    return chosen_key, TEMPLATES[chosen_key]


def choose_two_story_ideas():
    ideas = [
        {
            "key": "road_tale",
            "vibe": "creepy",
            "title": "Creepy Road Tale",
            "description": "A dark highway adventure where the twist is eerie and the mood is spooky.",
        },
        {
            "key": "road_tale",
            "vibe": "silly",
            "title": "Silly Road Tale",
            "description": "A ridiculous highway escapade where oddball twists and absurd jokes keep the laughs coming.",
        },
        {
            "key": "space_mission",
            "vibe": "creepy",
            "title": "Creepy Space Mission",
            "description": "A deep-space journey that turns unsettling when the stars stop behaving normally.",
        },
        {
            "key": "space_mission",
            "vibe": "silly",
            "title": "Silly Space Mission",
            "description": "A playful space trip full of wacky anomalies and cosmic comedy.",
        },
        {
            "key": "haunted_house",
            "vibe": "creepy",
            "title": "Creepy Haunted House",
            "description": "A classic haunted house scenario where every creak and shadow sparks suspense.",
        },
        {
            "key": "cooking_fiasco",
            "vibe": "silly",
            "title": "Silly Cooking Fiasco",
            "description": "A kitchen mishap that turns into a laugh-out-loud cooking disaster.",
        },
    ]
    return random.sample(ideas, 2)


def build_tracery_rules(user_inputs, chosen_key):
    rules = {"origin": [TEMPLATES[chosen_key]["text"]]}
    rules.update(TWIST_DIALOGUE_RULES)

    for key, value in user_inputs.items():
        rules[key] = [value]

    if "vibe_input" in rules:
        if rules["vibe_input"][0] == "creepy":
            rules["twist_for"] = rules["twist_for_creepy"]
            rules["dialogue_for"] = rules["dialogue_for_creepy"]
        else:
            rules["twist_for"] = rules["twist_for_silly"]
            rules["dialogue_for"] = rules["dialogue_for_silly"]
    elif chosen_key == "haunted_house":
        rules["twist_for"] = rules["twist_for_creepy"]
        rules["dialogue_for"] = rules["dialogue_for_creepy"]
    elif chosen_key == "cooking_fiasco":
        rules["twist_for"] = rules["twist_for_cooking"]
        rules["dialogue_for"] = rules["dialogue_for_cooking"]
    else:
        rules["twist_for"] = rules["twist_for_silly"]
        rules["dialogue_for"] = rules["dialogue_for_silly"]

    return rules


def generate_story(rules):
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar.flatten("#origin#")


def play_game(story_number=None):
    print("\n" + "~" * WIDTH)
    print("🎬 A NEW STORY BEGINS...")
    print("~" * WIDTH + "\n")
    sleep(1)

    story_ideas = choose_two_story_ideas()
    chosen_idea = choose_story_idea(story_ideas)
    chosen_key = chosen_idea["key"]
    chosen = TEMPLATES[chosen_key]
    theme_name = chosen_idea["title"]
    print_section_header(f"Theme: {theme_name}")

    user_inputs = collect_user_inputs(chosen, PROMPT_MAP, preselected_vibe=chosen_idea.get("vibe"))
    rules = build_tracery_rules(user_inputs, chosen_key)
    story = generate_story(rules)

    print_story_card(story, story_number)


def main():
    display_game_overview()
    sleep(1)
    greet_player()
    sleep(1)
    story_count = 0

    while True:
        story_count += 1
        play_game(story_count)
        print(f"\nStories created so far: {story_count}")

        if not play_again():
            print("Thanks for playing! Goodbye. 👋")
            break
