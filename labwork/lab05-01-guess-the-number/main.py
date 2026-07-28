#!usr/bin/env python3

# Name: Temitope S. Olugbemi
# Date: 2026-07-28
# Class Number: DEV108 9084
# Assignment: Code Practice Lab 5

import random

EASY_LIMIT = 5  # Maximum number of tries for easy difficulty
MEDIUM_LIMIT = 8  # Maximum number of tries for medium difficulty
HARD_LIMIT = 10  # Maximum number of tries for hard difficulty
WINS = 0  # Number of wins for the player
LOSSES = 0  # Number of losses for the player


def display_title():
    """Display the title of the game in a friendly banner."""
    print("""
=====================================
   🎉 Welcome to Guess The Number! 🎉
=====================================
""")


def get_player_name():
    """Prompt for the player's name and greet them."""
    name = input("What's your name? ").strip() or "Player"
    return name


def get_difficulty_level():
    """Ask the player to choose a difficulty level and return limits."""
    prompt = (
        "Choose a difficulty:\n"
        "  1) Easy   — 5 tries, numbers between 1 and 10\n"
        "  2) Medium — 8 tries, numbers between 1 and 100\n"
        "  3) Hard   — 10 tries, numbers between 1 and 1000\n"
        "Enter 1, 2, 3 or easy/medium/hard: "
    )
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("1", "easy", "e"):
            return EASY_LIMIT, 10
        if choice in ("2", "medium", "m"):
            return MEDIUM_LIMIT, 100
        if choice in ("3", "hard", "h"):
            return HARD_LIMIT, 1000
        print("Please enter a valid choice: 1, 2, 3, easy, medium, or hard.\n")


def update_scoreboard(won):
    """Update the player's wins/losses counters."""
    global WINS, LOSSES
    if won:
        WINS += 1
    else:
        LOSSES += 1


def get_player_score():
    """Return the player's current score as a tuple (wins, losses)."""
    return WINS, LOSSES


def play_game():
    """Play a single round of the game with friendly prompts and validation."""
    tries_limit, max_number = get_difficulty_level()

    number = random.randint(1, max_number)
    print(f"I'm thinking of a number between 1 and {max_number}.")
    print(f"You have {tries_limit} attempts to guess it. Good luck!\n")

    tries_used = 0
    won = False

    while tries_used < tries_limit:
        tries_used += 1
        prompt = f"Attempt {tries_used}/{tries_limit} — Enter your guess: "
        try:
            guess = int(input(prompt))
        except ValueError:
            print("That doesn't look like a number. Try again.\n")
            tries_used -= 1
            continue

        if guess < 1 or guess > max_number:
            print(f"Error: Please guess a number between 1 and {max_number}!\n")
            tries_used -= 1
            continue

        if guess < number:
            print("Too low.\n")
        elif guess > number:
            print("Too high.\n")
        else:
            won = True
            print(f"\n🎉 Nice! You guessed the number {number} in {tries_used} tries.\n")
            break

    if not won:
        print(f"Oh no — you've used all {tries_limit} attempts. The number was {number}.\n")

    update_scoreboard(won)


def main():
    display_title()
    print()
    player_name = get_player_name()
    print(f"\nNice to meet you, {player_name}! Let's play.\n")

    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play again? (y/n): ").strip() or "n"
        print()

    wins, losses = get_player_score()
    print("Thanks for playing! Here's your summary:\n")
    print("+----------------------+\n"
          f"| Wins: {wins:<3} Losses: {losses:<3} |\n"
          "+----------------------+\n")
    print("Goodbye — come back soon! 👋")


if __name__ == "__main__":
    main()
