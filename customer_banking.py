# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
 

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your savings account balance? "))
    savings_interest = float(input("What is your interest rate percentage? "))
    savings_months = int(input("How many months for your savings account? "))
    
    # Call the create_savings_account function and pass the variables from the user.  
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your savings interest earned is: ${savings_interest_earned: ,.2f}")
    print(f"Updated savings account balance is: $ {updated_savings_balance: ,.2f}")  
        
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is your CD account balance? "))
    cd_interest = float(input("What is your interest rate percentage? "))
    cd_months = int(input("How many months for your CD account to mature? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_savings_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your CD interest earned is: ${cd_interest_earned: ,.2f}")
    print(f"Updated CD account balance is: $ {updated_cd_balance: ,.2f}")
       
if __name__ == "__main__":
    # Call the main function.
    main()
