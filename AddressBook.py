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

    # UC9

    # View Person by City or State

    def view_persons_by_location(self):

        if not self.addressbook:
            print("\nNo contacts found. Please add one first")

        else:
            print("\n------------------------- View Person by City or State -------------------------\n")

            print("Enter 1 to search by city")
            print("Enter 2 to search by state\n")

            choice = input("Enter your choice: ")

            if(choice == "1"):

                print("\nAvailable Cities:\n")

                for city in self.city_person_map.keys():
                    print(f"- {city}")

                selected_city = input("\nEnter the city name: ").capitalize()

                if selected_city in self.city_person_map:

                    person_in_city = self.city_person_map[selected_city]

                    print(f"\nTotal number of person found in {selected_city}: {len(person_in_city)}") # UC10
                    print(f"\nPersons in City: {selected_city}\n")

                    for person in person_in_city:
                        print(f"- {person}")
                else:
                    print(f"\nNo persons found in City: {selected_city}.")

            elif(choice == "2"):

                print("\nAvailable States:\n")

                for state in self.state_person_map.keys():
                    print(f"- {state}")

                selected_state = input("\nEnter the state name: ").capitalize()

                if selected_state in self.state_person_map:

                    person_in_state = self.state_person_map[selected_state]

                    print(f"\nTotal number of person found in {selected_state}: {len(person_in_state)}") # UC10
                    print(f"\nPersons in State: {selected_state}\n")

                    for person in person_in_state:
                        print(f"- {person}")
                else:
                    print(f"\nNo persons found in State: {selected_state}.")
            else:
                print("\nInvalid choice. Returning to main menu.")

    # UC11

    # Sort the Address Book alphabetically by Person name

    def sort_address_book(self):
        
        if not self.addressbook:
            print("\nNo contacts found to sort. Please add one first.")

        else:
            print("\n------------------------- Sort Address Book -------------------------\n")

            print("1. Sort by Name")
            print("2. Sort by City")
            print("3. Sort by State")
            print("4. Sort by Zip")
            print("Press Enter to Exit")

            choice = input("\nEnter your choice: ")

            match choice:

                case "1":
                    self.addressbook.sort(key=lambda contact: contact[0])  # Sort by the full name (first element of each contact)
                    print("\nAddress Book sorted alphabetically by name.")

                case "2":
                    self.addressbook.sort(key=lambda contact: contact[2]) # UC12
                    print("\nAddress Book sorted alphabetically by city name") # Sort by city

                case "3":
                    self.addressbook.sort(key=lambda contact: contact[3]) # UC12
                    print("\nAddress Book sorted alphabetically by state name") # Sort by state

                case "4":
                    self.addressbook.sort(key=lambda contact: contact[4]) # UC12
                    print("\nAddress Book sorted by zip code") # Sort by zip

                case _:
                    print("\nReturning to Main menu.")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Main

# UC8

# Search Persons with City and State

def search_person_by_location(address_books):

    if not address_books:
        print("\nNo Address Books available. Please create one first.")

    else:
        print("\n------------------------- Search Person by City or State -------------------------\n")

        print("Enter 1 to search by city")
        print("Enter 2 to search by state\n")

        search_type = input("Enter your choice: ")

        if(search_type == "1"):

            location = input("\nEnter the city name: ").capitalize()
            search_key = "City"

        elif search_type == "2":

            location = input("\nEnter the state name: ").capitalize()
            search_key = "State"

        else:
            print("\nInvalid choice. Returning to main menu.")
            return

        print(f"\nSearching for persons in {search_key}: {location}...\n")

        found = False

        for book_name, address_book in address_books.items():
            for contact in address_book.addressbook: # It is used to access addressbook[] list of the address_book object.
                
                if(location in contact):
                    if not found:
                        print("Matching Contacts:")
                    found = True
                    print(f"\nAddress Book: {book_name}")
                    print("Name:", contact[0])
                    print("Address:", contact[1])
                    print("City:", contact[2])
                    print("State:", contact[3])
                    print("Zip:", contact[4])
                    print("Phone number:", contact[5])
                    print("Email:", contact[6])

        if not found:
            print(f"\nNo persons found in {search_key}: {location}.")

# UC5

# Add Multiple Person To Address Book

def manage_address_book(book):

    while True:
        print("\n------------------------- Manage Address Book -------------------------\n")

        print("------------------------- Enter 1 to add contacts -------------------------")
        print("------------------------- Enter 2 to edit contacts -------------------------")
        print("------------------------- Enter 3 to delete contacts -------------------------")
        print("------------------------- Enter 4 to view person by city or state -------------------------")
        print("------------------------- Enter 5 to sort contacts alphabetically -------------------------")
        print("------------------------- Press Enter to exit -------------------------\n")

        choice = input("Enter you choice: ")

        if(choice == "1"):

            book.add_contact_details()

        elif(choice == "2"):

            book.edit_contact_details()

        elif(choice == "3"):

            book.delete_contact_details()

        elif(choice == "4"):

            book.view_persons_by_location()

        elif choice == "5":
            
            book.sort_address_book()

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
        print("3. Search Person by City or State")
        print("Press Enter to exit\n")    

        choice = input("Enter you choice: ")

        if(choice == "1"):

            book_name = input("\nEnter a unique name for the Address Book: ").title()

            if book_name in address_books:
                print(f"\nAddress Book '{book_name}' already exists.")
            else:
                address_books[book_name] = AddressBook()
                print(f"\nAddress Book '{book_name}' created successfully.")

        elif(choice == "2"):

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

        elif(choice == "3"):

            search_person_by_location(address_books)

        else:
            print("\nClosing Address Book, Thank you for joining.")
            break

main()