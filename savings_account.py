"""Imports the SavingsAccount class and attributes from the Account.py file."""
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    if (type(balance) == float or type(balance) == int) and (type(interest_rate) == float or type(interest_rate) == int) and type(months) == int:
        interest = 0
        user_account = Account(balance, interest) 


    # Calculate interest earned
    interest_earned = balance * (interest_earned/100 * months/12)
    
    # Update the savings account balance by adding the interest earned
    update_balance = user_account.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    user_account.set_balance(update_balance) 

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    user_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return user_account.balance, user_account.interest 
    else:
        error_string = ""
        if not (type(balance) == float or type(balance) == int):
            error_string += (f"The balance ({balance}) was not a number.")
        if not (type(interest_rate) == float or type(interest_rate) == int):
            error_string += (f"The interest rate entered ({interest_rate}) was not a number.")
        if not type(months) == int:
            error_string += (f"The months ({months}) was not an integer.")
        #The error string is returned with an additional empty quote to maintain output consistency
        return error_string, " "

if __name__ == "__main__":

    print(create_savings_account(2000,20, 12)
    print(Returning 3000, 300))

    print(create_savings_account(2000, 'Money', 12)
    print("Interest rate was not a number.") 
