CONTACTS_FILE ="contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added!")

def view_contacts():
    print("\n📒 Contact List:")
    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                print(f"Name: {name} | Phone: {phone} | Email: {email}")
    except FileNotFoundError:
        print("No contacts found.")

def search_contacts():
    search_term = input("Search name: ").lower()
    found = False
    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                if search_term in name.lower():
                    print(f"🔍 Found: {name} | {phone} | {email}")
                    found = True
        if not found:
            print("No matching contact found.")
    except FileNotFoundError:
        print("No contacts file found.")

def main():
    while True:
        print("\n📞 Contact Book Menu")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice  == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()