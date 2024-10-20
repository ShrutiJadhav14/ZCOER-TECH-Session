def calculate_grade(marks):
   if marks>=90:
    return 'A'
   elif marks>=80 and marks<90:
    return 'B'
   elif marks>=70 and marks<80:
    return 'c'
   elif marks>=35 and marks<70:
      return 'pass'
   elif marks<35:
      return 'fail'
   else:
    print("Please enter correct input")

students={}
while True:
    print("\n1.add student")
    print("\n2.display")
    print("\n3.exit")
    choice=input("choose an option(1-3):")

    if choice=='1':
        name=input("Enter your name:")
        age=int(input(f"Enter {name}'s age:"))
        marks=int(input("enter marks:"))
        students[name]={'age':age,'marks':marks}
        print("Details added")
    elif choice=='2':
        if not students:
            print("no student found")
        else:
            for name,details in students.items():
                age=details['age']
                marks=details['marks']
                grade=calculate_grade(marks)
                print(f"Name:{name},age:{age},marks:{marks},grade:{grade}\n")
    elif choice=='3':
        print("Existing")
        break
    else:
        print("invalid choice")

    

    
    