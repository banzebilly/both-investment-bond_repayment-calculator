"""
    For this task, assume that you have been approached by a small financial
    company and asked to create a program that allows the user to access two
    different financial calculators: an investment calculator and a home loan
    repayment calculator, My first capston project using python fuctions.
    
    Banze Billy.
    
"""


import math

def calculate_investment_interest():
    principal = float(input("Enter principal amount for investment:\n"))
    rate = float(input("Enter amount of interest rate:\n"))
    time = float(input("Enter duration for investment in years:\n"))

    rate = (rate / 100) / 12  # Monthly interest rate

    simple_compound = input("Select either simple or compound:\n").lower()

    if simple_compound == "simple":
        amount = principal * (1 + rate * time)
    elif simple_compound == "compound":
        amount = principal * math.pow((1 + rate), time)
    else:
        print("Invalid selection.")
        return

    print(f"Interest earned over {time} years: {amount}")

def calculate_bond_repayment():
    house_value = float(input("Enter the current value of the house:\n"))
    interest_rate = float(input("Enter the interest rate:\n"))
    interest_rate = ((interest_rate / 100) / 12) / 12  # Monthly interest rate
    duration_months = float(input("Enter the duration in months:\n"))

    monthly_repayment = math.floor((interest_rate * house_value) / (1 - (1 + interest_rate) ** (-duration_months)))

    print(f"Monthly repayment: {monthly_repayment}")

def main():
    print("\nSelect an option:\n1. Investment\n2. Bond")

    choice = input("Enter your choice (1 or 2):\n")

    if choice == "1":
        calculate_investment_interest()
    elif choice == "2":
        calculate_bond_repayment()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
