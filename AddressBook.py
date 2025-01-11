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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Main

contacts = AddressBook("suresh", "sharma", "#47 new zone, garden street", "chandigarh", "punjab", 14587, 123456789, "suresh123@gmail.com")
contacts.add_contact_details()

print(contacts.addressbook)