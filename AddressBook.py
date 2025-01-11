#  Start

class AddressBookMain:

    def __str__(self):    
        return ("\n------------------------- Welcome to Address Book Program -------------------------")
    
display_message = AddressBookMain()
print(display_message)


# UC1

class AddressBook:

    addressbook = [] # Address Book

    # Constructor for Input of Data

    def __init__(self, firstname, lastname, address, city, state, zip, phonenumber, email):

        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phonenumber = phonenumber
        self.email = email

        self.fullname = self.firstname + " " + self.lastname

    # UC2

    # Add Contacts Details to Address Book

    def add_contact_details(self):

        contact_details = []

        contact_details.append(self.fullname.title())
        contact_details.append(self.address.title())
        contact_details.append(self.city.capitalize())
        contact_details.append(self.state.capitalize())
        contact_details.append(self.zip)
        contact_details.append(self.phonenumber)
        contact_details.append(self.email.lower())

        self.addressbook.append(contact_details)

    # UC3

    #  Edit Contact Details from Address Book

    def edit_contact_details(self, fullname):

        for contact in self.addressbook:

            if(fullname in contact):

                while True:

                    print(f"\nEditing details for {fullname}")
                    print("Enter new details or press Enter to keep current details\n")

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
                            new_firstname = input(f"Enter new first Name [current first name: {contact[0].split()[0]}]: ").title() or contact[0].split()[0]
                            contact[0] = new_firstname + " " + contact[0].split()[1]

                        case "2":
                            new_lastname = input(f"Enter new last Name [current last name: {contact[0].split()[1]}]: ").title() or contact[0].split()[1]
                            contact[0] = contact[0].split()[0] + " " + new_lastname
                            
                        case "3":
                            contact[1] = input(f"Enter new address [current address: {contact[1]}]: ").title() or contact[1]

                        case "4":
                            contact[2] = input(f"Enter new city [current city: {contact[2]}]: ").capitalize() or contact[2]

                        case "5":
                            contact[3] = input(f"Enter new state [current state: {contact[3]}]: ").capitalize() or contact[3]

                        case "6":
                            contact[4] = input(f"Enter new zip [current zip: {contact[4]}]: ") or contact[4]

                        case "7":
                            contact[5] = input(f"Enter new phone number [current phone number: {contact[5]}]: ") or contact[5]

                        case "8":
                            contact[6] = input(f"Enter new email [current email: {contact[6]}]: ") or contact[6]

                        case _:
                            print("\nContact Updated Successfully, Thank you for Editing.")
                            break
                break

        else:
            print("\nContact not found, please enter valid name")

    # UC4

    # Delete Contact Details from Address Book

    def delete_contact_details(self, fullname):

        counter = 0

        for contact in self.addressbook:

            if(fullname in contact):
                self.addressbook.pop(counter)
                print("\nContact Deleted Successfully.")
                break
            else:
                counter += 1
        else:
            print("\nContact not found, please enter valid name")   

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Main

contacts = AddressBook("suresh", "sharma", "#47 new zone, garden street", "chandigarh", "punjab", 14587, 123456789, "suresh123@gmail.com")
contacts.add_contact_details()
contacts.edit_contact_details("Suresh Sharma")
contacts.delete_contact_details("Suresh Sharma")

print(contacts.addressbook)