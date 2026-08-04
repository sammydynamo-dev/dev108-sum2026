# Starting file for Exercise 6.1 in our textbook

import statistics


def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    # prompt the user to enter test scores until they enter 'x' to exit
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate the total, count, average, lowest, highest, and median
    score_total = sum(scores)
    count = len(scores)
    average = round(score_total / count if count > 0 else 0)    
    lowest = min(scores) if count > 0 else 0
    highest = max(scores) if count > 0 else 0
    
    median_index = count // 2
    median = statistics.median(scores) if count > 0 else 0

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Lowest Score:      ", lowest)
    print("Highest Score:     ", highest)
    print("Median Score:      ", median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
