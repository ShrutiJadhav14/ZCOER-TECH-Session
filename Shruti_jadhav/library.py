library = {}

def add_book(title, author, year):
    if title in library:
        print("This book already exist")
    else:
        library[title] = {
            'author': author,
            'year': year,
            'available': True
        }
        print(f"Book '{title}' added successfully.")

def update_availability(title, status):
    if title in library:
        library[title]['available'] = status
        statusT = "available" if status else "not available"
        print(f"Book '{title}' is now {statusT}.")
    else:
        print("Book not found in the library.")

def display_available_books():
    """Display all available books."""
    print("\nAvailable Books:")
    for title, details in library.items():
        if details['available']:
            print(f"Title: {title}, Author: {details['author']}, Year: {details['year']}")
def main():
    while True:
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Available Books")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter publication year: ")
            add_book(title, author, year)
        
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            update_availability(title, False)
        
        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            update_availability(title, True)
        
        elif choice == '4':
            display_available_books()
        
        elif choice == '5':
            print("Exiting the library system.")
            break
        
        else:
            print("Invalid option")

if __name__ == "_main_":
    main()