# Start

class AddressBookMain:

    def __str__(self):    
        return ("\n------------------------- Welcome to Address Book Program -------------------------")
    
# UC1
    
class AddressBook:

    # Constructor for Creating a Adress Book

    def __init__(self):
        self.addressbook = [] # Address Book

    # UC2

    # Add Contacts Details to Address Book

    def add_contact_details(self):

        print("\n------------------------- Enter your Details ------------------------\n")

        fname = input("Enter your first name: ").title()
        lname = input("Enter your last name: ").title()
        fullname = f"{fname} {lname}"

        # UC7

        # Check for duplicates

        for contact in self.addressbook:
            if (fullname in contact):
                print(f"\nDuplicate entry detected! A contact with the name '{fullname}' already exists.")
                return

        address = input("Enter your address: ").title()
        city = input("Enter your city: ").capitalize()
        state = input("Enter your state: ").capitalize()
        zip = int(input("Enter your zip: "))
        phone = int(input("Enter your phone number: "))
        email = input("Enter your email: ").lower()

        contact_details = [f"{fname} {lname}", address, city, state, zip, phone, email]
        self.addressbook.append(contact_details)
        print(f"\nContact '{fname} {lname}' added successfully.")
    
    # UC3

    # Edit Contact Details from Address Book

    def edit_contact_details(self):

        if not self.addressbook:
            print("\nNo contacts found. Please add one first")

        else:
            print("\n-------------------------- Please Enter your full name to edit your details --------------------------\n")

            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            fullname = (fname + " " + lname).title()

            for contact in self.addressbook:
                if(fullname in contact):

                    while True:

                        print(f"\nEditing details for {fullname}")
                        print("Enter new details or press Enter to keep current values\n")

                        print("\nSelect the detail you want to edit:\n")

                        print("1. First name")
                        print("2. Last name")
                        print("3. Address")
                        print("4. City")
                        print("5. State")
                        print("6. Zip")
                        print("7. Phone number")
                        print("8. Email")

                        print("\nPress Enter to Exit\n")

                        choice = input("Enter your choice: ")

                        # Add new details to Address Book

                        match(choice):

                            case "1":
                                new_firstname = input(f"\nEnter new first Name [current first name: {contact[0].split()[0]}]: ").title() or contact[0].split()[0]
                                contact[0] = new_firstname + " " + contact[0].split()[1]

                            case "2":
                                new_lastname = input(f"\nEnter new last Name [current last name: {contact[0].split()[1]}]: ").title() or contact[0].split()[1]
                                contact[0] = contact[0].split()[0] + " " + new_lastname
                                
                            case "3":
                                contact[1] = input(f"\nEnter new address [current address: {contact[1]}]: ").title() or contact[1]

                            case "4":
                                contact[2] = input(f"\nEnter new city [current city: {contact[2]}]: ").capitalize() or contact[2]

                            case "5":
                                contact[3] = input(f"\nEnter new state [current state: {contact[3]}]: ").capitalize() or contact[3]

                            case "6":
                                contact[4] = input(f"\nEnter new zip [current zip: {contact[4]}]: ") or contact[4]

                            case "7":
                                contact[5] = input(f"\nEnter new phone number [current phone number: {contact[5]}]: ") or contact[5]

                            case "8":
                                contact[6] = input(f"\nEnter new email [current email: {contact[6]}]: ") or contact[6]

                            case _:
                                print(f"\nContact '{fullname}' Updated Successfully, Thank you for Editing.")
                                return
        
            print("\nContact not found, please enter valid name")

    # UC4

    # Delete Contact Details from Address Book

    def delete_contact_details(self):

        if not self.addressbook:
            print("\nNo contacts found. Please add one first")

        else:
            print("\n------------------------- Please Enter your full name to delete your details -------------------------\n")

            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            fullname = (fname + " " + lname).title()

            for contact in self.addressbook:

                if(fullname in contact):
                    self.addressbook.remove(contact)
                    print(f"\nContact '{fullname}' Deleted Successfully.")
                    return
            
            print("\nContact not found, please enter valid name")   

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Main

# UC5

# Add Multiple Person To Address Book

def manage_address_book(book):

    while True:
        print("\n------------------------- Manage Address Book -------------------------\n")

        print("------------------------- Enter 1 to add contacts -------------------------")
        print("------------------------- Enter 2 to edit contacts -------------------------")
        print("------------------------- Enter 3 to delete contacts -------------------------")
        print("------------------------- Press Enter to exit -------------------------\n")

        choice = input("Enter your choice: ")

        if(choice == "1"):

            book.add_contact_details()

        elif(choice == "2"):

            book.edit_contact_details()

        elif(choice == "3"):

            book.delete_contact_details()

        else:
            print("\nReturning to main menu.")
            break

# UC6

# Managing Multiple Address Books

def main():

    display_message = AddressBookMain()
    print(display_message)

    address_books = {}

    while True:

        print("\n1. Create a new Address Book")
        print("2. Select an Address Book")
        print("Press Enter to exit\n")    

        choice = input("Enter your choice: ")

        if choice == "1":

            book_name = input("\nEnter a unique name for the Address Book: ").title()

            if book_name in address_books:
                print(f"\nAddress Book '{book_name}' already exists.")
            else:
                address_books[book_name] = AddressBook()
                print(f"\nAddress Book '{book_name}' created successfully.")

        elif choice == "2":

            if not address_books:
                print("\nNo Address Books available. Please create one first.")
            else:
                print("\nAvailable Address Books:\n")

                for name in address_books.keys():
                    print(f"- {name}")

                selected_book = input("\nEnter the name of the Address Book to select: ").title()

                if selected_book in address_books:
                    manage_address_book(address_books[selected_book])
                else:
                    print(f"\nAddress Book '{selected_book}' not found.")
        else:
            print("\nClosing Address Book, Thank you for joining.")
            break

main()