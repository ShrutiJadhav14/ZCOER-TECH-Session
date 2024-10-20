balance = 1000 
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    
    choice = int(input("Enter your choice [1-4]: "))
    
    
    if choice == 1:
        print(f"\nYour current balance is: ${balance:.2f}")
    
    
    elif choice == 2:
        deposit = float(input("\nEnter the amount to deposit: $"))
        if deposit > 0:
            balance += deposit
            print(f"\nYou have successfully deposited ${deposit:.2f}.")
            print(f"Your new balance is: ${balance:.2f}")
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
  
    elif choice == 3:
        withdraw = float(input("\nEnter the amount to withdraw: $"))
        if withdraw > 0:
            if withdraw <= balance:
                balance -= withdraw
                print(f"\nYou have successfully withdrawn ${withdraw:.2f}.")
                print(f"Your new balance is: ${balance:.2f}")
            else:
                print("\nInsufficient balance! Your current balance is less than the requested amount.")
        else:
            print("\nInvalid amount. Please enter a positive number.")
    
   
    elif choice == 4:
        print("\nThank you for using the ATM. Goodbye!")
        break
    
    
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")
