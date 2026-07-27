# starting file for Exercise 3-2

# be sure to follow along with my video demonstration video in our Canvas assignment instructions if you need help

# display a welcome message
print("The Test Scores application")
print()

another_set = "y"

while another_set == "y":
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

    # initialize variables for this set of scores
    total_score = 0
    score_count = 0

    while True:
        user_input = input("Enter test score: ")

        if user_input.lower() == "end":
            break

        score = int(user_input)

        if score >= 0 and score <= 100:
            total_score += score
            score_count += 1
        else:
            print("Test score must be from 0 through 100. Try again.")

    # calculate and display the results for this set
    print("======================")
    if score_count > 0:
        average_score = round(total_score / score_count)
        print("Total Score:", total_score,
              "\nAverage Score:", average_score)
    else:
        print("No test scores were entered.")

    print()
    another_set = input(
        "Enter another set of test scores (y/n)? "
    ).lower()
    print()

print("Bye")
