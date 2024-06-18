'''
1) when we pass the same parameter for the all class on that time me pass the parameter
only the perent class

2) if we pass the deffirent parameter for diffirent classes on that time me pass
the parameter saperatly

3) if we are printing the messege by the perent class method for all the class and same
is same for all the class on that time we do not implete the perent class method
into the child class method (we do not override the method)
'''





'''
Question 1: Animal Class Hierarchy
Create a class hierarchy to represent different types of animals. Create a 
base class called Animal with the following methods:

__init__(self, name): Initializes the animal with a name.
speak(self): A method that will be overridden by subclasses to print a specific sound.
Then, create two subclasses Dog and Cat that inherit from Animal and override
the speak method to print "Woof" for dogs and "Meow" for cats.
'''

class Animal:

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass
    

class Dog(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)
        
    def speak(self):
        print(f"My name is {self.name} and i speak Woof")


class Cat(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def speak(self):
        print(f"My name is {self.name} and i speak Meow")


dog1 = Dog("Tommy")
cat1 = Cat("Chikki")

dog1.speak()
cat1.speak()



'''
Question 2: Shape Hierarchy
Create a class hierarchy to represent different shapes. Create a base class called
Shape with the following methods:

__init__(self): Initializes the shape.
area(self): A method that will be overridden by subclasses to calculate the area of 
the shape. perimeter(self): A method that will be overridden by subclasses to
calculate the perimeter of the shape. Then, create two subclasses Rectangle and Circle 
that inherit from Shape and override the area and perimeter methods to calculate the
area and perimeter of a rectangle and a circle, respectively.
'''
    
import math

class Shape:

    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2  * (self.length + self.width)


class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
    
    def area(self):
        return (math.pi * math.pi) * self.r
    
    def perimeter(self):
        return 2 * (math.pi * self.r)
    

rectangle1 = Rectangle(20, 20)
circle1 = Circle(2)

area_of_rectangle1 = rectangle1.area()
perimeter_of_rectangle1 = rectangle1.perimeter()
print(area_of_rectangle1)
print(perimeter_of_rectangle1)

area_of_circle1 = circle1.area()
perimeter_of_circle1 = circle1.perimeter()
print(area_of_circle1)
print(perimeter_of_circle1)




'''
Question 3: Vehicle Hierarchy with Polymorphism
Create a class hierarchy to represent different types of vehicles. Create a base 
class called Vehicle with the following methods:

__init__(self, make, model, year): Initializes the vehicle with the make, model, and 
year.start_engine(self): A method that will be overridden by subclasses to print a
message indicating the engine has started. stop_engine(self): A method that will be
overridden by subclasses to print a message indicating the engine has stopped. Then, 
create two subclasses Car and Motorcycle that inherit from Vehicle and override the 
start_engine and stop_engine methods to print appropriate messages for starting and
stopping the engines of a car and a motorcycle.
'''

class Vahicle:

    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model} {self.year}...")

    def stop_engine(self):
        print(f"Stopping the engine of {self.make} {self.model} {self.year}...")


class Car(Vahicle):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
    

class Motorcycle(Vahicle):

    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)
    

car1 = Car("Toyota", "Camry", 2022)
motorcycle1 = Motorcycle("Honda", "CBR", 2020)

print("Car")
car1.start_engine()
car1.stop_engine()
print("")

print("Motorcycle")
motorcycle1.start_engine()
motorcycle1.stop_engine()


'''
Question 4: Polymorphic Shape Drawing
Create an abstract base class Shape with the following methods:

__init__(self): Initializes the shape.
draw(self): An abstract method that will be overridden by subclasses to print a 
message indicating how the shape is drawn.Then, create three subclasses Circle, 
Rectangle, and Triangle that inherit from Shape and override the draw method to 
print appropriate messages for drawing a circle, rectangle, and triangle. Ensure
 you use polymorphism to call the draw method on a list of shapes.

Example Usage
Create a list of shapes (Circle, Rectangle, Triangle) and iterate through the list,
calling the draw method on each shape.
'''
class Shape:
    

    def __init__(self) -> None:
        pass

    def draw(self):
        pass


class Circle(Shape):
    
    def draw(self):
        print("Drawing a Circle...")


class Rectangle(Shape):
    
    def draw(self):
        print("Drawing a Rectangle...")


class Triangle(Shape):
    
    def draw(self):
        print("Drawing a Triangle...")

shapes = [Circle(), Rectangle(), Triangle()]

# Iterate through the list and call the draw method
for shape in shapes:
    shape.draw()


'''
Next Question: Advanced Level
Question 5: Library Management System with Polymorphism Create an abstract base
class LibraryItem with the following methods:

__init__(self, title, author): Initializes the library item with a title and author.
get_info(self): An abstract method that will be overridden by subclasses to return a
string with the item's information.Then, create two subclasses Book and Magazine that
inherit from LibraryItem and override the get_info method to include additional 
information specific to each type. For example, Book should include the number of pages,
and Magazine should include the issue number.

Example Usage
Create a list of library items (both Book and Magazine) and iterate through the list, 
printing the information for each item using the get_info method.
'''

class LibraryItem:


    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages
    
    def get_info(self):
        print(f"Title: {self.title}, Author {self.author}, Pages: {self.pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def get_info(self ):
        print(f"Title: {self.title}, Author {self.author}, Pages: {self.issue}")


library_items = [
    Book("1984", "George Orwell", 328),
    Magazine("National Geographic", "Various", 2024),
    Book("To Kill a Mockingbird", "Harper Lee", 281),
    Magazine("Time", "Various", 2023)
]

for item in library_items:
    item.get_info()