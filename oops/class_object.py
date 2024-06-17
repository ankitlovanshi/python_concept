'''
when we decleare the value in the class variable it will be defualt value for the all
the object and if you want something new value for the object we can the value for the'
# perticular object
# '''
# decleare the class
class Bike:
    name = "Yamma" #class variable

# create object
bike1 = Bike()
bike2 = Bike()
bike3 = Bike()

# initlize object value
bike1.name = "FZ-X"
bike2.name = "FZ-S"

print(bike1.name)
print(bike2.name)
print(bike3.name)



'''
In the example college_name is a class variable and it's value should be same for 
all the object and name is the instance variable and the value will be diffirent 
for all the object
'''
class Student:

    college_name = "Medicaps University"
    def __init__(self, name) -> None:
        self.name = name

student1 = Student("Romit")
student2 = Student("Raj")

print(student1.name, student1.college_name)
print(student2.name, student2.college_name)   


'''
Example 1
'''

class Room:
    length = 0.0
    wiedth = 0.0

    def calculate_area(self):
        return self.length * self.wiedth

room1 = Room()
room1.length = 2
room1.wiedth = 2

area = room1.calculate_area()
print("Area: ", area)



'''
Question 1: Bank Account Class

Create a class called BankAccount with the following attributes and methods:

Attributes:

account_number: A unique identifier for the account.
account_holder: Name of the account holder.
balance: The amount of money in the account, initialized to 0.
Methods:

deposit(amount): Adds the specified amount to the balance.
withdraw(amount): Subtracts the specified amount from the balance if there are sufficient funds; otherwise, prints an error message.
get_balance(): Returns the current balance.
transfer_to(another_account, amount): Transfers the specified amount from this account to another account if there are sufficient funds; otherwise, prints an error message.

'''

class BankAccount:
    

    def __init__(self, account_number, account_holder, balance) -> None:
        self.account_number = account_number
        self.acount_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrow(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Transection succussfuly completed")
        else:
            print("Ensufficient balance")
        
    def get_balance(self):
        print("Avalable balance", self.balance)
    
    def transfer_to(self, another_account, amount):
        
        if not isinstance(another_account, BankAccount):
            print("Wrong account details")
        
        elif amount > self.balance:
            print("Ensufficeint balance")

        elif amount < 0:
            print("Amoult should be positive")

        else:
            self.balance -= amount
            print(self.balance)
        
account1 = BankAccount(2001, "ankit", 100000)
account2 = BankAccount(2002, "Soruabh", 500000)

account1.deposit(100000)
print(account1.balance)

account1.withdrow(100000)
account1.get_balance()

account1.transfer_to(account2, 25000)


'''
Next Question: Library System

Create a class called Library that manages a collection of books. Each book should have a title, author, and an availability status (whether it is currently borrowed or not). The class should have the following methods:

add_book(title, author): Adds a new book to the library.
borrow_book(title): Marks a book as borrowed if it is available; otherwise, prints an error message.
return_book(title): Marks a book as returned.
list_available_books(): Prints a list of all available books.
list_borrowed_books(): Prints a list of all borrowed books.
Implement the class and provide a few example usages.
'''
# class Book:
#     def __init__(self, title, author) -> None:
#         self.title = title
#         self.author = author

# class Library:

#     def __init__(self) -> None:
#         self.books = [  ]

#     def add_book(self, title, author):
#         new_book = self.Book(title)
    
#     def borrow_book(self, ):
#         if isinstance(self.title, Library):
#             print("available")
        
#         else:
#             print("not available")
#     # 
# book1 = Library()
# book2 = Library()
# book1.add_book("Ramayan", "Tulsidas")
# book2.add_book("Geeta", "Krishna")
# book1.borrow_book(book2)



        

