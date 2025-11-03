## this program will help the user showing an account balace of a fictional account
## also will help deposit or withdraw money from the account 

def show_balance(balance):
    print(f"Your balance is EUR {balance: .2f}. ")

def deposit():
    amount = float(input("How much money you wish to deposit? EUR: "))
    if amount < 0: 
        print("Negative amounts cannot be deposited.")
        return 0
    else: 
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn: EUR "))
    if amount > balance:
        print("----------------")
        print("Amount cannot be withdrawn. Insufficent funds.")
        return 0
    
    elif amount < 0: 
        print("----------------")
        print("Amount cannot be less than 0. ")
        return 0

    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------------")
        print("Welcome to your banking assistant.")
        print("Menu options: ")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("---------------------")

        choice = input("Enter your choice from 1 - 4: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else: 
            print("----------------")
            print("That is not a valid choice. Please select another option")
            
    print("Thank you for using our Banking assistant! ")

if __name__ == '__main__':
    main()