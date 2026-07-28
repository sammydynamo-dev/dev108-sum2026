#!/usr/bin/env python3
import nameformat as nf

def main():
    print("Hello, welcome to the name formatting program!")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    
    print()
    print("**********************")
    print("\tMENU\t")
    print("**********************")
    print("Please select an option from the menu below:")
    print("1 - Say Hello")
    print("2 - Output Full Name")
    print("3 - Output Last Name, First Name")
    print("4 - Read Documentation")
    print("5 - Exit")
    print()
    
    while (choice := input("What is your choice? ")) != "5":
        if choice == "1":
            print(nf.sayhello(first_name))
        elif choice == "2":
            print(nf.fullname(first_name, last_name))
        elif choice == "3":
            print(nf.lastnamefirst(first_name, last_name))
        elif choice == "4":
            print(nf.__doc__)
        else:
            print("Invalid option.")
        
    print("Thank you for using the name formatting program. Goodbye!")

if __name__ == "__main__":
    main()