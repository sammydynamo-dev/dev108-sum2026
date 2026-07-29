#!/usr/bin/env python3
"""CLI UI helpers for the Conditional Twist Mad Libs game."""

WIDTH = 80


def print_section_header(title):
    header = f"{title}"
    underline = "─" * len(title)
    print(f"\n{header}\n{underline}")


def print_prompt(prompt_text):
    return f"> {prompt_text}"


def display_game_overview():
    title = "🎪 WELCOME TO THE CONDITIONAL TWIST MAD LIBS ENGINE 🎪"
    subtitle = (
        "Answer a few fun prompts and watch the story transform. "
        "Each playthrough gets a fresh twist and a polished terminal presentation."
    )
    print("\n")
    print_section_header(title.center(WIDTH))
    print(subtitle.center(WIDTH))
    print("\n")


def greet_player():
    name = input(print_prompt("Before we begin, what name should we call you?:") + " ")
    print(f"\nHi {name}! Let's get started! Please follow the prompts to enter your words.\n")


def get_user_input(word_type):
    """Prompt the user for a single word or phrase with validation."""
    while True:
        user_input = input(print_prompt(f"Please enter a/an {word_type}:") + " ")
        if user_input.strip():
            return user_input.strip()
        print(f"Invalid input. Please enter a valid {word_type}.")


def choose_story_idea(ideas):
    print_section_header("Choose a story idea")
    for index, idea in enumerate(ideas, start=1):
        print(f"  {index}) {idea['title']}")
        for line in idea["description"].splitlines():
            print(f"     {line}")
        print("")

    while True:
        choice = input(print_prompt("Enter 1 or 2:") + " ")
        if choice in {"1", "2"}:
            return ideas[int(choice) - 1]
        print("Invalid selection. Please enter 1 or 2 to choose one of the story ideas.")


def choose_vibe():
    print_section_header("Choose a vibe for your story")
    print("  1) Creepy")
    print("  2) Silly")
    while True:
        choice = input(print_prompt("Enter 1 or 2:") + " ")
        if choice == "1":
            return "creepy"
        if choice == "2":
            return "silly"
        print("Please choose 1 or 2.")


def collect_user_inputs(chosen, prompt_map, preselected_vibe=None):
    user_inputs = {}
    if preselected_vibe is not None:
        user_inputs["vibe_input"] = preselected_vibe
    elif "vibe" in chosen["fields"]:
        user_inputs["vibe_input"] = choose_vibe()

    for field in chosen["fields"]:
        if field == "vibe":
            continue
        user_inputs[field] = get_user_input(prompt_map.get(field, field))

    return user_inputs


def print_story_card(story, story_number=None):
    title = "📖 STORY OUTPUT"
    print(f"\n{title}")
    print("-" * WIDTH)
    for line in story.splitlines():
        print(line)
    print("-" * WIDTH)


def play_again():
    answer = input(print_prompt("Would you like to play again? (y/n):") + " ")
    return bool(answer and answer.strip().lower().startswith("y"))
