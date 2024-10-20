employees = {}

def calculate_pay(hours, wage):
    regular_hours = 40
    if hours > regular_hours:
        overtime_hours = hours - regular_hours
        overtime_pay = overtime_hours * wage * 1.5
        total_pay = (regular_hours * wage) + overtime_pay
    else:
        total_pay = hours * wage
    return total_pay

def update_employee(name, hours, wage):
    employees[name] = {'hours_worked': hours, 'hourly_wage': wage}
    print(f"Employee '{name}' updated successfully.")

def calculate_total_payroll():
    total_payroll = 0
    for name, details in employees.items():
        pay = calculate_pay(details['hours_worked'], details['hourly_wage'])
        total_payroll += pay
        print(f"Employee: {name}, Pay: ${pay:.2f}")
    return total_payroll

def main():
    while True:
        print("\nEmployee Payroll System Menu:")
        print("1. Update Employee")
        print("2. Calculate Total Payroll")
        print("3. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            hours = float(input("Enter hours worked: "))
            wage = float(input("Enter hourly wage: "))
            update_employee(name, hours, wage)

        elif choice == '2':
            total_payroll = calculate_total_payroll()
            print(f"\nTotal Payroll: ${total_payroll:.2f}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
