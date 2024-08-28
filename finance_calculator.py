import math

# The user to choose which calculator they want
print("Select a calculation:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

# Get user choice and normalize it to lowercase
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").strip().lower()

if choice == 'investment':
    print("\nInvestment Calculator")
    
    # Get user inputs
    principal = float(input("Enter the amount of money you are depositing (R): "))
    rate = float(input("Enter the interest rate (as a percentage, e.g., 8 for 8%): "))
    years = float(input("Enter the number of years you plan on investing: "))
    interest = input("Enter 'simple' for simple interest or 'compound' for compound interest: ").strip().lower()

    # Convert rate percentage to decimal
    rate /= 100

    # Calculate total amount based on interest type
    if interest == 'simple':
        total_amount = principal * (1 + rate * years)
    elif interest == 'compound':
        total_amount = principal * math.pow((1 + rate), years)
    else:
        print("\nInvalid interest type entered. Please choose 'simple' or 'compound'.")
        exit()
    
    print(f"\nThe total amount after {years} years with {interest} interest is: R{total_amount:.2f}")

elif choice == 'bond':
    print("\nBond Repayment Calculator")
    
    present_value = float(input("Enter the present value of the house (R): "))
    annual_rate = float(input("Enter the annual interest rate (as a percentage, e.g., 7 for 7%): "))
    months = int(input("Enter the number of months you plan to take to repay the bond: "))
    
    # Convert annual interest rate to monthly and percentage to decimal
    monthly_rate = (annual_rate / 100) / 12
    
    # Calculate monthly repayment
    repayment = (monthly_rate * present_value) / (1 - math.pow(1 + monthly_rate, -months))
    
    print(f"\nThe monthly repayment amount is: R{repayment:.2f}")

else:
    print("\nInvalid choice entered. Please select 'investment' or 'bond'.")
