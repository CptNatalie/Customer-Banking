"""Import the Account class from the Account.py file."""
from Account import Account 

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    cd_account = Account(balance, 0)
   if (type(balance) == float or type(balance) == int)  and (type(interest_rate) == float or type(interest_rate) == int) and type(months) == int:
        interest_p = 0
        user_cd = Account(balance, interest_p)

    # Calculate interest earned
    interest_earned = balance * (interest_rate/100 * months/12) 

    # Update the CD account balance by adding the interest earned
     updated_balance = user_cd.balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    user_cd.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    user_cd.set_interest(interest_earned)


    # Return the updated balance and interest earned.
    return  user_cd.balance, user_cd.interest
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

    print(" Returning 2000, 100")
    print(create_cd_account(3000, 30, 12))

    print("Your balance wasn't a number.")
    print(create_cd_account('money', 13, 12))
