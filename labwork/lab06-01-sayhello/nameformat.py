""" Name formatting functions
    DESCRIPTION: This module contains functions for formatting names in different ways.
    FUNCTIONS:
    - sayhello(firstName): Returns a greeting message for the given first name.
    - fullname(firstName, lastName): Returns the full name for the given first and last names.
    - lastnamefirst(firstName, lastName): Returns the name in last name first format
"""

# sayHello() ex: Hello Tony!
def sayhello(firstName):
    """
    Returns a greeting message for the given first name.
    """
    return "Hello " + firstName + "!"



# fullName() ex: Tony Stark
def fullname(firstName, lastName):
    """
    Returns the full name for the given first and last names.
    """
    return firstName + " " + lastName


# lastNameFirst() ex: Stark, Tony
def lastnamefirst(firstName, lastName):
    """
    Returns the name in last name first format.
    """
    return lastName + ", " + firstName
