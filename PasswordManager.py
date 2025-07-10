# NO SAVE FEATURE YET
# So yes, it's pretty much useless
import time

Running = True
Passwords = {}

def add_password():
    while True:
        print("\n--- Add a New Password ---")
        new_password_name = input("Enter the service or site name: ")
        new_password = input("Enter the password: ")
        Passwords[new_password_name] = new_password
        time.sleep(1)
        print(f"\nPassword for \"{new_password_name}\" added successfully.")

        choice = input("\nWould you like to add another password? (Y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            break

def list_passwords():
    if len(Passwords) == 0:
        print("\nNo passwords have been added yet.")
    else:
        time.sleep(1)
        print("---------------------------------------")
        print(f"Saved Passwords ({len(Passwords)} total)")
        print("---------------------------------------")
        for i in Passwords.keys():
            print(f"{i}: {Passwords[i]}")
            time.sleep(0.5)
        time.sleep(1)
        print("---------------------------------------")
    input("\nPress Enter to return to the menu.")

def search_password():
    if len(Passwords) == 0:
        print("\nNo passwords have been added yet.")
        time.sleep(1)
        input("Press Enter to return to the menu.")
    else:
        while True:
            matches = 0
            passwords_found = {}
            password = input("\nEnter the name of the service or site to search: ")
            for key in Passwords:
                if key.lower() == password.lower():
                    matches += 1
                    passwords_found[key] = Passwords[key]
            
            if matches == 0:
                print("\nNo matching entries found.")
            else:
                time.sleep(1)
                print(f"\nFound {matches} match{'es' if matches > 1 else ''}:")
                for key in passwords_found:
                    print(f"{key}: {passwords_found[key]}")
            
            choice = input("\nSearch for another password? (Y/n): ")
            if choice.lower() == 'y':
                continue
            else:
                break

def delete_password():
    global Passwords
    print("\n--- Delete Password ---")
    if len(Passwords) == 0:
        print("\nNo passwords have been added yet.")
        input("Press Enter to return to the menu.")
    else:
        list_passwords()
        print("1. Delete a password")
        print("2. Delete all passwords")
        print("3. Cancel and return to menu")
        print()
        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    matches = 0
                    password = input("Enter the name of the password to delete: ")
                    to_delete = [key for key in Passwords if password.lower() == key.lower()]
                    for key in to_delete:
                        del Passwords[key]
                        matches += 1
                    time.sleep(1)
                    if matches:
                        print(f"\nDeleted {matches} entr{'y' if matches == 1 else 'ies'} successfully.")
                    else:
                        print("\nNo matching entries found.")
                    input("\nPress Enter to return to the menu.")
                elif choice == 2:
                    consent = input("This will delete all saved passwords. Are you sure? (Y/n): ")
                    if consent.lower() == 'y':
                        Passwords = {}
                        time.sleep(0.5)
                        print("\nAll passwords deleted.")
                        input("\nPress Enter to return to the menu.")
                        break
                    else:
                        print("\nOperation canceled.")
                        break
                elif choice == 3:
                    print("\nReturning to main menu.")
                    break
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                    time.sleep(1)
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

while Running:
    try:
        print("\n---------------------------------------")
        print("Simple Password Manager")
        print("---------------------------------------")
        print("1. Add a password")
        print("2. Delete a password")
        print("3. List all passwords")
        print("4. Search for a password")
        print("5. Exit")
        print("---------------------------------------")
        choice = int(input("Enter your choice (1-5): "))
        if choice == 1:
            add_password()
        elif choice == 2:
            delete_password()
        elif choice == 3:
            list_passwords()
        elif choice == 4:
            search_password()
        elif choice == 5:
            print("\nThank you for using the Password Manager. Goodbye.")
            time.sleep(1)
            break
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        input("Press Enter to continue.")
