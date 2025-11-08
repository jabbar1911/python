# Phonebook Mini-Project with Exception Handling

phonebook = {}

def add_contact():
    try:
        name = input("Enter name: ")
        if name in phonebook:
            print("Contact already exists!")
            return
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"{name} added successfully!")
    except Exception as e:
        print("Error adding contact:", e)

def view_contacts():
    if not phonebook:
        print("Phonebook is empty!")
    else:
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def update_contact():
    try:
        name = input("Enter name to update: ")
        if name not in phonebook:
            print("Contact not found!")
            return
        number = input("Enter new phone number: ")
        phonebook[name] = number
        print(f"{name} updated successfully!")
    except Exception as e:
        print("Error updating contact:", e)

def delete_contact():
    try:
        name = input("Enter name to delete: ")
        if name not in phonebook:
            print("Contact not found!")
            return
        del phonebook[name]
        print(f"{name} deleted successfully!")
    except Exception as e:
        print("Error deleting contact:", e)

while True:
    print("\nPhonebook Options:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Phonebook. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1-5.")
