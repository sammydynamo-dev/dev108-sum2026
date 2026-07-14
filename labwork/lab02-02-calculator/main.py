#!/usr/bin/env python3

# Display a welcome message
print("The Area and Perimeter program")
print()
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
print()

# Calculate the area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Format and display the result
print("======================")
print("Length:\t\t", length)
print("Width:\t\t", width)
print("Area:\t\t", area)
print("Perimeter:\t", perimeter)
print()
print("Thanks for using our program. Bye!")