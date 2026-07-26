 #! /usr/bin/env python3
 # Name: Temitope S. Olugbemi
 # Date: 2026-07-23
 # Project 1: Fake "Sales ChatBot"
 
""" 
main.py
~~~~~~~
This is the main entry point for the SalesChat application.
It initializes the application and starts the main loop."""


PRODUCT_NAME = "SalesChat"
PRODUCT_DESCRIPTION = (
    "SalesChat is a cutting-edge application designed to streamline your sales process. "
    "With its intuitive interface and powerful features, you can effortlessly manage your sales pipeline, "
    "engage with customers, and close deals faster than ever before."
)
PRODUCT_FEATURES = [
    "Intuitive user interface for easy navigation.",
    "Lead tracking and management tools.",
    "Customer interaction logging and analysis.",
    "Sales data analytics and reporting.",
    "Customizable sales workflows."
]
PRODUCT_BENEFITS = [
    "Increase sales efficiency and productivity.",
    "Enhance customer engagement and satisfaction.",
    "Gain valuable insights into sales performance.",
    "Streamline your sales process from lead to close.",
    "Achieve sales success with a powerful tool at your fingertips."
]
PRODUCT_PERSONALITY = (
    "SalesChat is not just a tool; it's your sales companion. "
    "With a friendly and approachable interface, it makes managing your sales conversations a breeze. "
    "Whether you're a seasoned sales professional or just starting out, SalesChat is here to support you every step of the way."
)
PRODUCT_PRICE = 49.99  # Example price for the product

def greet_user():
    """Greets the user and provides a brief introduction to the application."""
    print(f"==========================================================")
    print(f"\t\t\tWelcome to {PRODUCT_NAME}!\t\t")
    print(f"==========================================================")
    
    print("This application helps you manage your sales conversations efficiently.")
    print("Let's get started!\n")
    
def product_prompt():
    """Ask the user if they want to learn about your product or service."""
    learn = input("Would you like to learn about our product or service? (yes/no): ").strip().lower()
    return learn

def generate_product_overview():
    """Generate a brief overview of the product or service."""
    overview = (
        f"{PRODUCT_DESCRIPTION} "
        f"Key features include: {', '.join(PRODUCT_FEATURES)}. "
        f"Benefits you'll gain include: {', '.join(PRODUCT_BENEFITS)}. "
        f"Our product is priced at ${round(PRODUCT_PRICE, 2)} per unit."
    )
    return overview

def generate_sales_pitch():
    """Generate a sales pitch for the product or service. 
    Includes product description, features, benefits, and a bit of personality."""
    pitch = (
        f"{PRODUCT_PERSONALITY} "
    )
    return pitch

def generate_purchase_offer_prompt():
    """Ask the user if they’d like to buy your product."""
    offer = input(f"Would you like to purchase our product at just ${round(PRODUCT_PRICE, 2)}? (yes/no): ").strip().lower()
    return offer

def close_sale():
    """Gather these details from the user, calculate the total cost, and provide a receipt of the purchase."""
    print("\nThank you for your interest in our product!")
    name, email, phone = get_user_details()
    quantity = int(input("How many units would you like to purchase? "))
    unit_price, total_cost = calculate_total_cost(quantity)
    provide_receipt(name, email, phone, quantity, unit_price, total_cost)
    
def get_user_details():
    """Gather user details for the purchase."""
    name = input("Please enter your full name: ").strip()
    email = input("Please enter your email address: ").strip()
    phone = input("Please enter your phone number: ").strip()
    return name, email, phone

def calculate_total_cost(quantity):
    """Calculate the total cost based on the quantity and unit price."""    
    unit_price = PRODUCT_PRICE  # Use the global product price
    total_cost = quantity * unit_price
    
    return unit_price, total_cost

def provide_receipt(name, email, phone, quantity, unit_price, total_cost):
    """Provide a receipt of the purchase."""
    
    print("\n--- Purchase Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ${round(unit_price, 2)}")
    print(f"Total Cost: ${round(total_cost, 2)}")
    print("------------------------")
    print("Thank you for your purchase! We will contact you shortly with further details.")

def main():
    """Main function to run the SalesChat application."""
    greet_user()
    print()
    
    learn = product_prompt().lower()
    while learn not in ["yes", "y", "no", "n"]:
        print("Invalid input. Please respond with 'yes' or 'no'.")
        learn = product_prompt().lower()
        print()
        
    if learn == "yes" or learn == "y":
        print(generate_product_overview())
        print()
        
        print(generate_sales_pitch())
        print()
        
        offer = generate_purchase_offer_prompt().lower()
        print()
        
        while offer not in ["yes", "y", "no", "n"]:
            print("Invalid input. Please respond with 'yes' or 'no'.")
            print()
            
            offer = generate_purchase_offer_prompt().lower()
            print()
            
        if offer == "yes" or offer == "y":
            close_sale()
        elif offer == "no" or offer == "n":
            print("Thank you for your time! Feel free to reach out if you change your mind.")
    elif learn == "no" or learn == "n":
        print("No worries! If you have any questions in the future, we're here to help.")

if __name__ == "__main__":
    main()