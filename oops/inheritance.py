# Inheritance
class Bank:

    def __init__(self, account_holder, account_number) -> None:
        self.account_holder = account_holder
        self.account_number = account_number

class Loan(Bank):
    def __init__(self, loan_number, loan_type, amount, account_holder, account_number) -> None:
        self.loan_number = loan_number
        self.loan_type = loan_type
        self.amount = amount

        super().__init__(account_holder, account_number)
    
    def show_details(self):
        print(self.account_holder)
        print(self.account_number)
        print(self.loan_number)
        print(self.loan_type)
        print(self.amount)

loan1 = Loan(2001, "Home Loan", 2500000, "ankit", 42250001) 
loan1.show_details()




# method overloading
class Animal:

    def eat(self):
        print("it can eat")

class Cat(Animal):

    def eat(self):
        print("Cat can take milk")

cat1 = Cat()
cat1.eat()




# use of super()
'''
In some cases parent child class method overides the parent class method, in the some
case we have to need access the perent class method on that time we use the super()
function
'''
class Animal:

    def eat(self):
        print("it can eat")


class Cat(Animal):

    def eat(self):
        super().eat()
        print("Cat can take milk")

cat1 = Cat()
cat1.eat()




# multiple inheritance
class Student:
    def __init__(self, id, name, department) -> None:
        self.id = id
        self.name = name
        self.department = department
    
class Course:
    
    def __init__(self, course_code, course_name) -> None:
        self.course_code = course_code
        self.course_name = course_name
    
class College(Student, Course):

    def __init__(self, id, name, department, course_code, course_name) -> None:
        Student.__init__(self, id, name, department)
        Course.__init__(self, course_code, course_name)
    
    def show(self):
        print("Details")
        print("Student id: ", self.id)
        print("Student name: ", self.name)
        print("Department: ", self.department)
        print("Course code: ", self.course_code)
        print("Course name: ", self.course_name)
    
std1 = College("EN20CS301058", "Ankit Lovanshi","Engineering", "EN20CS01", "DSA")
std1.show()



# multilevel Inheritance
class A:

    def say_hello(self):
        print("Hello class A")
    
class B(A):
    
    def say_hello(self):
        print("Hello class B")

class C(B):

    def say_hello(self):
        print("Hello class C")
        return super().say_hello()

obj_c = C()
obj_c.say_hello()

