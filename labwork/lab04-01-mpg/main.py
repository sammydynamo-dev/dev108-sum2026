# Starting file for Exercise 3-1

# display a welcome message
print("The Miles Per Gallon application")
print()

another_trip = "y"

while another_trip == "y":
    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    while cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero.")
        cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display trip information
        mpg = miles_driven / gallons_used
        total_gas_cost = gallons_used * cost_per_gallon
        cost_per_mile = total_gas_cost / miles_driven

        print("Miles Per Gallon:          ", round(mpg, 2))
        print("Total Gas Cost:            ", round(total_gas_cost, 2))
        print("Cost Per Mile:             ", round(cost_per_mile, 2))

    print()
    another_trip = input("Get entries for another trip (y/n)? ")
    print()

print("Bye")
