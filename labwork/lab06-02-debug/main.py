# Test Case Values pre-debugging
# Test Num          Inputs                              Expected Output                             Actual Output                                                   Pass/Fail
# ------------|-------------------------------------|--------------------------------------------|--------------------------------------------------------------|-----------------
# 1                 x                                   Total Score: 0  Average Score: 0            ZeroDivisionError: division by zero                             Fail
# 2                 100 90 80 x                         Total Score: 270.0  Average Score: 90.0     Total Score: 270.0 Average Score: 45.0                          Fail
# 3                 90.5 90.5 90.5                      Total Score: 271.5  Average Score: 90.5     ValueError: invalid literal for float() with base 10: '90.5'    Fail  
# 4                 100 -5                              Test score must be from 0 through 100.      Test score must be from 0 through 100. Score discarded.         Pass
# 5                 100 x                               Total Score: 100.0  Average Score: 100.0    Total Score: 100.0 Average Score: 50.0                          Fail
# 6                 100 90 80 70 60 50 40 30 20 10 x    Total Score: 550.0  Average Score: 55.0     Total Score: 550.0 Average Score: 28.0                          Fail

# Test Case Values post-debugging
# Test Num          Inputs                             Output                                          Logic changes                                                   Pass/Fail
# ------------|---------------------------------------|-----------------------------------------------|--------------------------------------------------------------|-----------------
# 1                 x                                   Total Score: 0  Average Score: 0                skip division when counter is 0                                 Pass
# 2                 100 90 80 x                         Total Score: 270.0  Average Score: 90.0         only increment valid test scores once                           Pass
# 3                 90.5 90.5 90.5                      Total Score: 271.5  Average Score: 90.5         convert input to float before validation                        Pass  
# 4                 100 -5                              Test score must be from 0 through 100.          None                                                            Pass
# 5                 100 x                               Total Score: 100.0  Average Score: 100.0        only increment valid test scores once                           Pass
# 6                 100 90 80 70 60 50 40_3０ 2０ 1０ x  Total Score: 55０.０  Average Score: 5５.０      only increment valid test scores once                           Pass

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

while True:
    test_score = input("Enter test score (or 'x' to quit): ")
    if test_score != "x":
        test_score = float(test_score) # convert input to float to handle decimal scores
        # not incrementing counter here to avoid incrementing twice for valid scores and incrementing at all for invalid scores
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# calculate average score
average_score = round(score_total / counter, 1) if counter > 0 else 0 # prevent division by zero
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")