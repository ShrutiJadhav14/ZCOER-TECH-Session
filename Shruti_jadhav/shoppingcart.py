cart={}
while True:
    print("Shopping cart menu:")
    print("\n1.add items:")
    print("\n2.remove items")
    print("\n3.display ")
    print("\n4.check if discount is available ")
    print("\n5.Exit")
    choice=int(input("enter choice:[1-4]:"))
    if choice==1:
        name=input("Enter name of elements:")
        quantity=int(input("Enter how much quantity you want:"))
        prize=float(input("Enter prize:"))
        cart[name]={'quantity':quantity,'prize':prize}
        print("Details added succesfully")
    elif choice==2:
        if not cart:
            print("Your cart is empty noyhing to remove")
        else:
            deleteEle=input("Enter element to delete")
            if deleteEle in cart:
                del cart[deleteEle]
                print(f"{deleteEle}has been removed")
            else:
                print(f"{deleteEle}is not in cart")
    elif choice==3:
         if not cart:
            print("no cart found")
         else:
            for name,details in cart.items():
                quantity=details['quantity']
                prize=details['prize']
                print(f"Name:{name},quantity:{quantity},prize:{prize}\n")
    elif choice==4:
        for i in cart:
            if prize>=100:
                print(f"10%_discount is applicable on {name}")
            elif prize>50 and prize<100:
                print(f"5%_discount is applicable on {name}")
            else:
                print("no 1discount is applicable ")
    elif choice==5:
        print("Existing")
        break
    else:  
        print("invalid choice")

                
            
     

