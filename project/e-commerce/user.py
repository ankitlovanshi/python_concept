class User:

    def __init__(self, username, email, role) -> None:
        self.username = username
        self.email = email
        self.role = role

    def display_info(self):
        print("User name: ", self.username)
        print("Email: ", self.email)
        print("Role: ", self.role)


class Admin(User):

    def __init__(self, username, email) -> None:
        super().__init__(username, email, role = "admin")


class Customer(User):
    def __init__(self, username, email) -> None:
        super().__init__(username, email, role = "customer") 
