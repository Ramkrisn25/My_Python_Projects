# task8_contact_book.py

def display_menu():
    """Prints the contact book menu options."""
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
    print("-------------------------")

def add_contact(contacts):
    """Adds a new contact to the dictionary."""
    name = input("Enter contact name: ").strip().title()
    if name in contacts:
        print(f"Contact '{name}' already exists. Use update option to modify.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address (optional): ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts):
    """Searches and displays a contact's details."""
    name = input("Enter contact name to search: ").strip().title()
    if name in contacts:
        contact_info = contacts[name]
        print(f"\n--- Contact Details for {name} ---")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email'] if contact_info['email'] else 'N/A'}")
        print("----------------------------------")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts):
    """Updates an existing contact's phone or email."""
    name = input("Enter contact name to update: ").strip().title()
    if name in contacts:
        print(f"Current details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email'] if contacts[name]['email'] else 'N/A'}")
        
        new_phone = input("Enter new phone number (leave blank to keep current): ").strip()
        new_email = input("Enter new email address (leave blank to keep current): ").strip()
        
        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email
            
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Deletes a contact from the dictionary."""
    name = input("Enter contact name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def list_all_contacts(contacts):
    """Lists all contacts in the dictionary."""
    if not contacts:
        print("\nNo contacts in the book.")
        return
    print("\n--- All Contacts ---")
    for name, info in sorted(contacts.items()):
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email'] if info['email'] else 'N/A'}")
    print("--------------------")

def main():
    """Main function to run the contact book application."""
    contacts = {} # Initialize an empty dictionary for contacts

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            list_all_contacts(contacts)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()