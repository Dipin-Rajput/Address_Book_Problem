#  Start

class AddressBookMain:

    def __str__(self):    
        return ("\n------------------------- Welcome to Address Book Program -------------------------")
    
display_message = AddressBookMain()
print(display_message)


# UC1

class AddressBook:

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

contacts = AddressBook("first_name", "last_name", "address", "city", "state", 00000, 123456789, "email")