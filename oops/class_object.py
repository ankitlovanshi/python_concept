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
Question 1: Rectangle Class
Create a class called Rectangle that represents a rectangle with attributes
for width and height. The class should have the following methods:

__init__(self, width, height): Initializes the rectangle with the given width and height.
area(self): Returns the area of the rectangle.
perimeter(self): Returns the perimeter of the rectangle.
'''
class Rectangle:

    def __init__(self, width, heigth, ) -> None:
        self.width = width
        self.heigth = heigth
    
    def get_area(self):
        return self.width * self.heigth
    
    def get_perimeter(self):
        return 2 * (self.width + self.heigth)

rect1 = Rectangle(20, 20)

area = rect1.get_area()
perimeter = rect1.get_perimeter()

print(area)
print(perimeter)



'''
 Question 2: Library System
Create a class called Library that manages a collection of books. Each book should have a title, author, and an availability status (whether it is currently borrowed or not). The class should have the following methods:

add_book(title, author): Adds a new book to the library.
borrow_book(title): Marks a book as borrowed if it is available; otherwise, prints an error message.
return_book(title): Marks a book as returned.
list_available_books(): Prints a list of all available books.
list_borrowed_books(): Prints a list of all borrowed books.
'''   

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrow = False
class Library:
    
    def __init__(self) -> None:
        self.books = []
    
    def add_book(self, title, author):
        new_book = Book(title, author) 
        self.books.append(new_book)
        # print("Succussfully added book")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrow == False:
                    book.is_borrow = True
                    print("Available")
                    return
                else:
                    print("Not available")
                    return
       
        print("This is book is not in the library")
    
    def list_available_books(self):
        print("All the available books")
        for book in self.books:
            if book.is_borrow == False:
                print(book.title)
    
    def list_borrowed_books(self):
        print("All the borrow books")
        for book in self.books:
            if book.is_borrow == True:
                print(book.title)
            

library = Library()
library.add_book("1984", "George Orwell") 
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.borrow_book("To Kill a Mockingbird")
library.list_available_books()
library.list_borrowed_books()




# '''
# Advanced Level Question
# Question 3: Inventory Management System
# Create a class called Inventory to manage items in a store. Each item should have a name, quantity, and price. The class should have the following methods:

# add_item(name, quantity, price): Adds a new item to the inventory or updates the quantity if the item already exists.
# remove_item(name, quantity): Removes a specified quantity of an item from the inventory, ensuring that the quantity does not go negative.
# get_item(name): Returns the details of a specific item (name, quantity, and price).
# get_total_value(): Returns the total value of the inventory (sum of the quantity times price for all items).

# '''

class Item:
    def __init__(self, name, quantity, price) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:

    def __init__(self) -> None:
        self.items = []
    
    def add_items(self, name, quantity, price):
        new_item = Item(name, quantity, price)
        self.items.append(new_item)
    
    def remove_item(self, name):
        for index, item in enumerate(self.items):
            if item.name == name:
                del self.items[index] 
                return 
            
    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                print(item.name)
                print(item.price)
                print(item.quantity)
                return
            else:
                print("Item is not found")
                return
        
    def get_total_value(self):
        total_price = 0
        total_quantity = 0
        for item in self.items:
            total_price = total_price + item.price
            total_quantity = total_quantity + item.quantity
        
        print("total price: ", total_price)
        print("total quantity: ", total_quantity)

inventory = Inventory()
inventory.add_items("Realme 5 pro", 10, 15000)
inventory.add_items("Boat Smart Watch", 7, 1500)
inventory.add_items("Bottel", 10, 50)

inventory.remove_item("Realme 5 pro")
inventory.show_items()
inventory.get_item("Realme 5")
inventory.get_total_value()



'''
Question 4: Employee Management System
Create a class called Employee to manage employee information. Each employee should have an ID, name, and salary. The class should also have a class attribute to keep track of the total number of employees. Implement the following methods:

__init__(self, id, name, salary): Initializes the employee with ID, name, and salary, and increments the total number of employees.
get_details(self): Returns the details of the employee.
update_salary(self, new_salary): Updates the employee's salary.
get_total_employees(): Class method to return the total number of employees.
Implement the class and provide a few example usages.   
'''
