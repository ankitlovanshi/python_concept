
class EmployeeDeatils:

    def __init__(self, emp_id, name, gender, role):
        self.emp_id = emp_id
        self.name = name
        self.gender = gender
        self.role = role
    

class Employee:
    
    def __init__(self) -> None:
        self.employees = {}

    def create_employee(self, emp_id, name, gender, role):
        if emp_id in self.employees:
            print("Employee id must be unique")

        new_employee = EmployeeDeatils(emp_id, name, gender, role)
        self.employees[emp_id] = new_employee

    def show_employees(self):
        for emp_id, emp_data in self.employees.items():
            print("Employee Id: ", emp_id)
            print(f"Name: {emp_data.name}, Gender: {emp_data.gender}")
            print(f"Role: {emp_data.role}")
            print("")
        
    def update(self, role, id):
        if role == "HR" or role == "Manager":
            for emp_id, emp_data in self.employees.items():
                if id == emp_id:
                    emp_data.name = input("Enter new Name: ")
                    emp_data.gender = input("Enter new Gender: ")
                    emp_data.role = input("Enter new Role: ")
                    print("Succussfully Updated your profile")
                    self.get_employee(id)
                    return
            print("Employee Does not exist")
            return
        
        print("You can't change the profile connect to admin")

    def get_employee(self, id):
        print("Your Details")
        for emp_id, emp_data in self.employees.items():
            if id == emp_id:
                print("Employee Id: ", emp_id)
                print(f"Name: {emp_data.name}, Gender: {emp_data.gender}")
                print(f"Role: {emp_data.role}")
                print("")
                return
            
        print("Employee Does not exist")
        return
    
    def remove_employee(self, role, id):
        if role == "HR" or role == "Manager":
            if id in self.employees:
                del self.employees[id]
                print("Succussfully Deleted")
                return 
            print("Employee Does not exist")
            return
        
        print("You can't Delete connect to admin")

              

emp = Employee()
emp.create_employee("2001", "Ankit", "Male", "Manger")
emp.create_employee("2002", "Sourabh", "Male", "HR")
emp.create_employee("2003", "Raj", "Male", "Employee")

# emp.show_employees()
# emp.get_employee("2002")
emp.update("HR", "2001")
# emp.remove_employee("HR", "2003")


