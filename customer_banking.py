# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account 
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter starting balance of savings account. ")) 
    savings_interest = float(input("Enter interest rate of savings account. ")) 
    savings_months = float(input("Enter number of months your account will accrue intrest. "))

    # Call the create_savings_account function and pass the variables from the user.
    if all(var > 0 for var in (savings_balance, savings_interest, savings_months)):
        updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your balance after {savings_months} months will be ${updated_savings_balance,.2f}.") 
    print(f"Interest earned on savings of ${savings_balance:,.2f} will be ${interest_earned:,.f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter balance of CD account. "))
    cd_interest_rate = float(input("Enter interest rate for CD account. "))
    cd_months = int(input("Enter the number of months account will accrue interst. "))


    # Call the create_cd_account function and pass the variables from the user.
    if all(var > 0 for var in (cd_balance, cd_interest, cd_months)):
        updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your final balance after {cd_months} ,months will be ${updated_cd_balance:,.2f}")
    print(f"Interest earned on original balance of ${cd_balance:,.2f} will be ${interest_earned:,.2f}.")

if __name__ == "__main__":
    # Call the main function.
    main()
