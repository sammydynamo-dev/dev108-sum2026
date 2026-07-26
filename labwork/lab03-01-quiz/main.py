"""An object-oriented quiz with several types of questions."""

import random
import time

DEFAULT_QUESTION_COUNT = 5
OPTION_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_user_input(prompt):
    """Read input and exit gracefully if the input stream is interrupted."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\n\n👋 The quiz was ended early. Thanks for playing. Goodbye!")
        raise SystemExit(0)


def start_countdown(seconds=3):
    """Display a dramatic countdown before a quiz round begins."""
    print("\n⏳ Get ready! Your quiz will begin in...")

    for seconds_remaining in range(seconds, 0, -1):
        print(f"   {seconds_remaining}...")
        # Pause for one second so the countdown feels like a real timer.
        time.sleep(1)

    print("🚀 Go!")


class Question:
    """Parent class containing behavior shared by every question type."""

    def __init__(self, prompt, correct_answer, hint):
        self.prompt = prompt
        self.correct_answer = correct_answer
        self.hint = hint

    def ask(self):
        """Display the question and return the user's answer."""
        return get_user_input(f"{self.prompt}\n✏️  Your answer: ").strip()

    def is_correct(self, user_answer):
        """Check a typed answer without worrying about capitalization."""
        return user_answer.casefold() == str(self.correct_answer).casefold()

    def answer_text(self):
        """Return the correct answer in a user-friendly format."""
        return str(self.correct_answer)


class ChoiceQuestion(Question):
    """Parent class for questions that display randomized answer options."""

    def __init__(self, prompt, options, correct_answer, hint):
        super().__init__(prompt, correct_answer, hint)
        self.options = tuple(options)
        self.option_map = {}

        if len(self.options) > len(OPTION_LETTERS):
            raise ValueError("There are not enough letters for all answer options.")

    def shuffle_options(self):
        """Randomize answer values and assign their display letters."""
        shuffled_options = random.sample(self.options, len(self.options))
        letters = OPTION_LETTERS[: len(shuffled_options)]
        self.option_map = dict(zip(letters, shuffled_options))

    def display_options(self):
        """Print the current randomized letter-to-answer mapping."""
        for letter, answer_value in self.option_map.items():
            print(f"  {letter}. {answer_value}")


class SingleChoiceQuestion(ChoiceQuestion):
    """A question for which the user chooses exactly one answer."""

    def __init__(self, prompt, options, correct_answer, hint):
        super().__init__(prompt, options, correct_answer, hint)

        if self.correct_answer not in self.options:
            raise ValueError("The correct answer must be in the answer options.")

    def ask(self):
        self.shuffle_options()
        print(self.prompt)
        self.display_options()

        while True:
            answer = get_user_input(
                f"👉 Choose one letter ({'/'.join(self.option_map)}): "
            ).strip().upper()
            if answer in self.option_map:
                return answer
            print("⚠️  Please choose one of the displayed letters.")

    def is_correct(self, user_answer):
        """Grade the answer value assigned to the user's selected letter."""
        selected_answer = self.option_map.get(user_answer.upper())
        return selected_answer == self.correct_answer

    def answer_text(self):
        for letter, answer_value in self.option_map.items():
            if answer_value == self.correct_answer:
                return f"{letter}. {answer_value}"
        return str(self.correct_answer)


class MultipleChoiceQuestion(ChoiceQuestion):
    """A question for which more than one answer may be correct."""

    def __init__(self, prompt, options, correct_answers, hint):
        correct_answer_values = set(correct_answers)
        super().__init__(prompt, options, correct_answer_values, hint)

        if not self.correct_answer.issubset(self.options):
            raise ValueError("Every correct answer must be in the answer options.")

    def ask(self):
        self.shuffle_options()
        print(self.prompt)
        self.display_options()

        while True:
            answer = get_user_input(
                "👉 Choose ALL correct letters, separated by commas: "
            ).strip()
            if self.parse_answers(answer) is not None:
                return answer
            print("⚠️  Please enter only displayed letters, such as A, C.")

    def parse_answers(self, user_answer):
        """Return valid selected letters or None when the response is invalid."""
        # Replacing commas with spaces supports both "A, C" and "A C".
        tokens = user_answer.upper().replace(",", " ").split()

        if not tokens:
            return None

        if not all(self.is_valid_option_token(token) for token in tokens):
            return None

        return set(tokens)

    def is_valid_option_token(self, token):
        """Check that a token is one displayed, single-letter option."""
        is_single_letter = len(token) == 1
        is_displayed_option = token in self.option_map
        return is_single_letter and is_displayed_option

    def is_correct(self, user_answer):
        selected_letters = self.parse_answers(user_answer)
        if selected_letters is None:
            return False

        selected_answers = {
            self.option_map[letter] for letter in selected_letters
        }
        return selected_answers == self.correct_answer

    def answer_text(self):
        answers = [
            f"{letter}. {answer_value}"
            for letter, answer_value in self.option_map.items()
            if answer_value in self.correct_answer
        ]
        return ", ".join(answers) or ", ".join(sorted(self.correct_answer))


class TypedAnswerQuestion(Question):
    """A question for which the user types a word or number."""

    def ask(self):
        return get_user_input(f"{self.prompt}\n✏️  Type your answer: ").strip()


def generate_math_question(pattern=None):
    """Create one random PEMDAS question from several expression patterns."""
    if pattern is None:
        pattern = random.randint(1, 7)

    # Each pattern calculates its answer directly. This is safer than using eval().
    if pattern == 1:
        a = random.randint(2, 15)
        b = random.randint(2, 10)
        c = random.randint(2, 8)
        d = random.randint(1, c - 1)
        expression = f"{a} + {b} x ({c} - {d})"
        answer = a + b * (c - d)
        hint = "Solve the subtraction in parentheses, then multiply, then add."

    elif pattern == 2:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        c = random.randint(2, 8)
        d = random.randint(1, 15)
        expression = f"({a} + {b}) x {c} - {d}"
        answer = (a + b) * c - d
        hint = "Add inside the parentheses before multiplying and subtracting."

    elif pattern == 3:
        a = random.randint(2, 9)
        b = random.randint(2, 10)
        c = random.randint(2, 10)
        expression = f"{a}² + {b} x {c}"
        answer = a**2 + b * c
        hint = "Evaluate the exponent and multiplication before adding."

    elif pattern == 4:
        a = random.randint(2, 8)
        b = random.randint(2, 8)
        c = random.randint(2, 20)
        expression = f"({a} + {b})² - {c}"
        answer = (a + b) ** 2 - c
        hint = "Add inside the parentheses, square that result, then subtract."

    elif pattern == 5:
        # Build the dividend from the divisor so division has a whole answer.
        quotient = random.randint(2, 12)
        divisor = random.randint(2, 10)
        dividend = quotient * divisor
        b = random.randint(2, 9)
        c = random.randint(2, 9)
        expression = f"{dividend} ÷ {divisor} + {b} x {c}"
        answer = dividend // divisor + b * c
        hint = "Complete division and multiplication before adding the results."

    elif pattern == 6:
        # This pattern also guarantees an exact division result.
        divisor = random.randint(2, 8)
        factor = random.randint(2, 8)
        a = divisor * factor
        b = random.randint(2, 10)
        c = random.randint(1, 12)
        expression = f"({a} x {b}) ÷ {divisor} + {c}"
        answer = (a * b) // divisor + c
        hint = "Multiply inside the parentheses, then divide, then add."

    else:
        a = random.randint(2, 15)
        b = random.randint(2, 10)
        c = random.randint(2, 10)
        d = random.randint(2, 15)
        expression = f"{a} + {b} x {c} - {d}"
        answer = a + b * c - d
        hint = "Multiply first, then work through addition and subtraction."

    return TypedAnswerQuestion(
        f"Solve using PEMDAS: {expression}",
        answer,
        hint,
    )


class Quiz:
    """Select questions, run the quiz, and keep track of the score."""

    def __init__(
        self,
        title,
        question_bank,
        number_of_questions=DEFAULT_QUESTION_COUNT,
    ):
        self.title = title
        self.question_bank = question_bank
        self.number_of_questions = number_of_questions
        self.score = 0

    def select_questions(self):
        """Randomly select the requested number of questions."""
        question_types = (
            SingleChoiceQuestion,
            MultipleChoiceQuestion,
            TypedAnswerQuestion,
        )

        # With fewer than three questions, select freely from the entire bank.
        if self.number_of_questions < len(question_types):
            return random.sample(
                self.question_bank,
                self.number_of_questions,
            )

        # Select one random question of each required type.
        selected = []
        for question_type in question_types:
            matching_questions = [
                question
                for question in self.question_bank
                if isinstance(question, question_type)
            ]
            selected.append(random.choice(matching_questions))

        # Randomly fill the remaining positions without repeating questions.
        remaining_questions = [
            question for question in self.question_bank if question not in selected
        ]
        number_needed = self.number_of_questions - len(selected)
        selected.extend(random.sample(remaining_questions, number_needed))
        random.shuffle(selected)
        return selected

    def ask_question_count(self):
        """Prompt until the user enters a valid number of questions."""
        maximum = len(self.question_bank)
        minimum = min(DEFAULT_QUESTION_COUNT, maximum)

        while True:
            response = get_user_input(
                "\n🔢 How many questions would you like to try? "
                f"({minimum}-{maximum}, press Enter for {minimum}): "
            ).strip()

            if response == "":
                return minimum

            try:
                question_count = int(response)
            except ValueError:
                print("⚠️  Please enter a whole number.")
                continue

            if minimum <= question_count <= maximum:
                return question_count

            print(
                f"⚠️  Please enter a number from {minimum} through {maximum}."
            )

    def run(self):
        """Run one or more quiz rounds and display each final result."""
        print("=" * 46)
        print(self.title.center(46))
        print("=" * 46)

        while True:
            play_quiz = get_user_input(
                "\n🎯 Would you like to take the quiz? (yes/no): "
            ).strip().lower()

            if play_quiz in ("yes", "y"):
                break
            if play_quiz in ("no", "n"):
                print("\n👋 No problem. Thanks for stopping by. Goodbye!")
                return
            print("⚠️  Please enter yes or no.")

        print("\n👋 Welcome! Great choice—you've got this!")
        print("🌟 Every question is a chance to learn. Let's have some fun!")

        while True:
            # Every new round starts with a fresh score.
            self.score = 0

            # Let the user decide the quiz length before questions are selected.
            self.number_of_questions = self.ask_question_count()
            selected_questions = self.select_questions()
            start_countdown()

            for number, question in enumerate(selected_questions, start=1):
                print("\n" + "-" * 46)
                print(f"📝 Question {number} of {self.number_of_questions}")
                user_answer = question.ask()

                if question.is_correct(user_answer):
                    correct_feedback = (
                        "✅ Correct! Great work!",
                        "🌟 Excellent! You got it!",
                        "🎉 That's right! Keep it up!",
                        "👏 Fantastic job!",
                        "🚀 You nailed it! Well done!",
                    )
                    print(random.choice(correct_feedback))
                    self.score += 1
                else:
                    print(
                        "❌ Sorry, that's not right. "
                        f"The answer was {question.answer_text()}."
                    )
                    print(f"💡 Solution hint: {question.hint}")

            self.show_results()

            if not self.ask_to_play_again():
                break

            print("\n🎯 Awesome! Let's play another round!")

        print("👋 Thanks for playing. Goodbye!")

    def ask_to_play_again(self):
        """Ask whether the user wants another round and validate the response."""
        while True:
            response = get_user_input(
                "\n🔄 Would you like to play another quiz? (yes/no): "
            ).strip().lower()

            if response in ("yes", "y"):
                return True
            if response in ("no", "n"):
                return False

            print("⚠️  Please enter yes or no.")

    def show_results(self):
        """Print the score and personalized feedback."""
        print("\n" + "=" * 46)
        print(
            f"🏆 Your total score is "
            f"{self.score}/{self.number_of_questions}."
        )

        percentage = self.score / self.number_of_questions

        if percentage == 1:
            print("🤩 Awesome work! You are a Rockstar.")
        elif percentage >= 0.8:
            print("🎉 Nice job! Almost 100%.")
        elif percentage >= 0.4:
            print("📚 Keep studying—you can do it!")
        else:
            print("💪 Don't give up—every attempt helps you improve!")


# A list can hold objects of different subclasses, making it a flexible text bank.
question_bank = [
    SingleChoiceQuestion(
        "Which number is a prime number?",
        ["9", "13", "15", "21"],
        "13",
        "A prime number has exactly two factors: 1 and itself.",
    ),
    SingleChoiceQuestion(
        "What is 7 x 8?",
        ["48", "54", "56", "64"],
        "56",
        "Think of 7 groups with 8 items in each group.",
    ),
    SingleChoiceQuestion(
        "Which shape has exactly three sides?",
        ["Square", "Circle", "Triangle", "Pentagon"],
        "Triangle",
        "The prefix 'tri-' means three.",
    ),
    MultipleChoiceQuestion(
        "Which of these numbers are even?",
        ["2", "5", "8", "11"],
        {"2", "8"},
        "Even numbers can be divided by 2 with no remainder.",
    ),
    MultipleChoiceQuestion(
        "Which expressions equal 12?",
        ["6 + 6", "3 x 4", "15 - 2", "24 / 2"],
        {"6 + 6", "3 x 4", "24 / 2"},
        "Calculate each option separately and select every result equal to 12.",
    ),
    MultipleChoiceQuestion(
        "Which of these numbers are multiples of 5?",
        ["10", "13", "20", "22"],
        {"10", "20"},
        "Multiples of 5 always end in 0 or 5.",
    ),
    TypedAnswerQuestion(
        "What is 30 / 3?",
        "10",
        "Ask how many groups of 3 fit evenly into 30.",
    ),
    TypedAnswerQuestion(
        "How many degrees are in a right angle?",
        "90",
        "A right angle is one quarter of a full 360-degree turn.",
    ),
    TypedAnswerQuestion(
        "What is 33 x 11?",
        "363",
        "Break 11 into 10 + 1, then calculate 33 x 10 plus 33 x 1.",
    ),
    # random.sample chooses three different PEMDAS patterns without duplicates.
    *[
        generate_math_question(pattern)
        for pattern in random.sample(range(1, 8), 3)
    ],
]


# Start the interactive quiz only when this file is run directly.
if __name__ == "__main__":
    math_quiz = Quiz("🧠 MATH SUPERSTAR QUIZ 🧠", question_bank)
    math_quiz.run()
