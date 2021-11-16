class Employee:
    office = "Wipro"
    caddress = "hitec city, hyderabad"

    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_emp_details(self):
        print("employee details are:",self.eid, self.name, self.sal, Employee.office, Employee.caddress)

Naveen = Employee(201, "Naveen", 30000)
Naveen.get_emp_details()

class Employee:
    office = "Snap hunt"
    caddress = "Dlf, Bangalore"

    def __init__(self, eid,name,sal):
        self.eid = eid
        self.name = name
        self. sal = sal

    def get_emp_details(self):
        print("employee details are:",self.eid, self.name, self.sal, Employee.office, Employee.caddress)
Naveen = Employee(202, "Naveen", 35000)
Naveen.get_emp_details()

class Employee:
    office = "Accenture"
    caddress = "Madhapur, Hyderbad"

    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_emp_details(self):
        print("employee details are:",self.eid, self.name, self.sal, Employee.office, Employee.caddress)

Naveen = Employee(205, "Naveen", 45000)
Naveen.get_emp_details()

# class data structures

class Employee:
    office = "Mphasis"
    caddress = {

        "flat no": "110" ,
        "landmark": "near ragvendhra colony",
        "area": "hitech city",
        "location": "hyderbad",
        "pincode": "500083"

    }

    def __init__(self,eid,name,  sal, tech_details):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.tech_details = tech_details

    def get_emp_details(self):
        print("emp details are:", self.eid, self.name,self.sal, Employee.office)
        for each in self.tech_details:
            print(each)

Naveen = Employee(206, "Naveen", 46000, "django")
Naveen.get_emp_details()




























