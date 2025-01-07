class User:
    __users = []  # Class-level attribute to store all users

    def __init__(self, name, email, password, address=None):
        self.name = name
        self.email = email
        self.password = password
        self.address = address if address else {
            "Street": "",
            "House Number": "",
            "City": "",
            "State": "",
            "Zip Code": "",
            "Country": ""
        }

    def signup(self):
        for user in User.__users:
            if user.email == self.email:
                raise ValueError("Email already in use.")
        User.__users.append(self)
        print("Signup successful!")

    @classmethod
    def signin(cls, email, password):
        for user in cls.__users:
            if user.email == email and user.password == password:
                return user
        return None

    def signout(self):
        print(f"User {self.name} signed out successfully.")

    def updateProfile(self, newCustomerName=None, newEmail=None, newPassword=None, newAddress=None):
        if newCustomerName:
            self.name = newCustomerName
        if newEmail:
            for user in User.__users:
                if user.email == newEmail:
                    raise ValueError("Email already in use.")
            self.email = newEmail
        if newPassword:
            self.password = newPassword
        if newAddress:
            self.address = newAddress
        print("Profile updated successfully!")


class GeneralCustomer(User):
    def __init__(self, name, email, password, address=None, creditCardInfo=None, accountBalance=0.0):
        super().__init__(name, email, password, address)
        self.creditCardInfo = creditCardInfo if creditCardInfo else {
            "Type": "",
            "Card Number": "",
            "CVV": "",
            "Expiry": "",
            "Currency": ""
        }
        self.accountBalance = accountBalance
        self.shopping_cart = ShoppingCart()

    def updateProfile(self, newCustomerName=None, newEmail=None, newPassword=None, newAddress=None, newCreditCardInfo=None):
        super().updateProfile(newCustomerName, newEmail, newPassword, newAddress)
        if newCreditCardInfo:
            self.creditCardInfo = newCreditCardInfo
        print("Profile updated successfully!")

    def getCustomerDetails(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Address": self.address,
            "Card Details": self.creditCardInfo,
            "Account Balance": self.accountBalance
        }


class CommercialCustomer(User):
    def __init__(self, name, email, password, address=None, creditCardInfo=None, accountBalance=0.0):
        super().__init__(name, email, password, address)
        self.creditCardInfo = creditCardInfo if creditCardInfo else {
            "Type": "",
            "Card Number": "",
            "CVV": "",
            "Expiry": "",
            "Currency": ""
        }
        self.accountBalance = accountBalance
        self.shopping_cart = ShoppingCart()

    def updateProfile(self, newCustomerName=None, newEmail=None, newPassword=None, newAddress=None, newCreditCardInfo=None):
        super().updateProfile(newCustomerName, newEmail, newPassword, newAddress)
        if newCreditCardInfo:
            self.creditCardInfo = newCreditCardInfo
        print("Profile updated successfully!")

    def getCustomerDetails(self):
        return {
            "Name": self.name,
            "Email": self.email,
            "Address": self.address,
            "Card Details": self.creditCardInfo,
            "Account Balance": self.accountBalance
        }


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to the cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            print(f"Item {item} not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart Items:")
            for item in self.items:
                print(f"- {item}")


class Menu:
    def __init__(self):
        self.current_customer = None

    def display_menu(self):
        while True:
            self.show_options()
            choice = int(input("Enter your choice: "))
            self.execute_choice(choice)

    def show_options(self):
        if not self.current_customer:
            print("1. Signup")
            print("2. Signin")
            print("8. Exit")
        else:
            print("1. Update Profile")
            print("2. Add Item to Cart")
            print("3. Remove Item from Cart")
            print("4. View Cart")
            print("5. Signout")
            print("8. Exit")

    def execute_choice(self, choice):
        if not self.current_customer:
            if choice == 1:
                self.signup()
            elif choice == 2:
                self.signin()
            elif choice == 8:
                exit()
            else:
                print("Invalid choice")
        else:
            if choice == 1:
                self.update_profile()
            elif choice == 2:
                self.add_item_to_cart()
            elif choice == 3:
                self.remove_item_from_cart()
            elif choice == 4:
                self.view_cart()
            elif choice == 5:
                self.signout()
            elif choice == 8:
                exit()
            else:
                print("Invalid choice")

    def signup(self):
        while True:
            print("Do you want to sign up as a:")
            print("1. General Customer")
            print("2. Commercial Customer")
            try:
                customer_type_choice = int(input("Enter your choice: ").strip())
                if customer_type_choice in [1, 2]:
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        name = input("Enter Customer Name: ").strip()
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()

        if not name or not email or not password:
            print("Customer name, email, and password are required.")
            return

        address = {
            "Street": input("Enter Street: "),
            "House Number": input("Enter House Number: "),
            "City": input("Enter City: "),
            "State": input("Enter State: "),
            "Zip Code": input("Enter Zip Code: "),
            "Country": input("Enter Country: ")
        }

        creditCardInfo = {
            "Type": input("Enter Card Type: "),
            "Card Number": input("Enter Card Number: "),
            "CVV": input("Enter CVV: "),
            "Expiry": input("Enter Expiry: "),
            "Currency": input("Enter Currency: ")
        }

        while True:
            try:
                accountBalance = float(input("Enter Account Balance: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if customer_type_choice == 2:
            customer = CommercialCustomer(name, email, password, address, creditCardInfo, accountBalance)
        else:
            customer = GeneralCustomer(name, email, password, address, creditCardInfo, accountBalance)

        try:
            customer.signup()
        except ValueError as e:
            print(e)

    def signin(self):
        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()
        customer = GeneralCustomer.signin(email, password)
        if not customer:
            customer = CommercialCustomer.signin(email, password)
        if customer:
            self.current_customer = customer
            print("Signin successful!")
        else:
            print("Invalid email or password.")

    def signout(self):
        if self.current_customer:
            self.current_customer.signout()
            self.current_customer = None

    def update_profile(self):
        newCustomerName = input("Enter New Customer Name (leave blank to keep current): ").strip()
        newEmail = input("Enter New Email (leave blank to keep current): ").strip()
        newPassword = input("Enter New Password (leave blank to keep current): ").strip()

        newAddress = self.get_new_address()
        newCreditCardInfo = self.get_new_credit_info()

        self.current_customer.updateProfile(newCustomerName, newEmail, newPassword, newAddress, newCreditCardInfo)

    def get_new_address(self):
        if input("Change address? (y/n): ").lower() == 'y':
            return {
                "Street": input("Enter New Street (leave blank to keep current): ").strip(),
                "House Number": input("Enter New House Number (leave blank to keep current): ").strip(),
                "City": input("Enter New City (leave blank to keep current): ").strip(),
                "State": input("Enter New State (leave blank to keep current): ").strip(),
                "Zip Code": input("Enter New Zip Code (leave blank to keep current): ").strip(),
                "Country": input("Enter New Country (leave blank to keep current): ").strip()
            }
        return None

    def get_new_credit_info(self):
        if input("Change credit card info? (y/n): ").lower() == 'y':
            return {
                "Type": input("Enter New Card Type (leave blank to keep current): ").strip(),
                "Card Number": input("Enter New Card Number (leave blank to keep current): ").strip(),
                "CVV": input("Enter New CVV (leave blank to keep current): ").strip(),
                "Expiry": input("Enter New Expiry (leave blank to keep current): ").strip(),
                "Currency": input("Enter New Currency (leave blank to keep current): ").strip()
            }
        return None

    def add_item_to_cart(self):
        item = input("Enter item to add: ")
        self.current_customer.shopping_cart.add_item(item)

    def remove_item_from_cart(self):
        item = input("Enter item to remove: ")
        self.current_customer.shopping_cart.remove_item(item)

    def view_cart(self):
        self.current_customer.shopping_cart.view_cart()


# Run the application
menu = Menu()
menu.display_menu()
