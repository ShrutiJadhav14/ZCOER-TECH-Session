def generate_table(number, upto):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")
    print()

def generate_multiple_tables():
    while True:
        print("\nMultiplication Table Generator Menu:")
        print("1. Generate a multiplication table for a specific number")
        print("2. Generate tables for numbers from 1 to 10")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            number = int(input("Enter a number: "))
            generate_table(number, 10)
        
        elif choice == '2':
            for num in range(1, 11):
                generate_table(num, 10)
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    generate_multiple_tables()
