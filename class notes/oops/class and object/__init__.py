# 1. builtin functions:

list1 = [2,4,6]
print("1.builtin : length of list", len(list1))

# 2. manual implementaion : decision making or oops

list2 = [3,4,9]
length = 0
for each in list2:
    length += 1
    print("2.manual implementaion : length of list2", length)

# 3. functions

list3 = [4,8,12]

def get_length():
    length = 0
    for each in list3:
        length += 1
    return length

print("3. functions : length of list", get_length())

# 4. oops

class Lengthlist:
    list4 = [5,7,4]

    @classmethod
    def get_length(cls):
        length = 0
        for each in list3:
            length += 1
            return length

print("4. oops : length of list:", Lengthlist.get_length())

class Lengthlist:
    list5 = [10,20,30]

    @classmethod
    def get_length(cls):
        length = 0
        for each in list3:
            length += 1
            return length

print("4.oops : length of list:", Lengthlist.get_length())

empid = 201
name = "Naveen"
salary = 30000

def employee_details(empid, name, salary):
    salary = salary + salary * 10 /100
    print("the employee details are: ", empid, name, salary)

employee_details(empid, name, salary)

class Employee:
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def employee_details1(self):
        self.sal = self.sal + self.sal * 10 / 100

        print("the employee details are:",self.eid, self.name, self.sal)

Naveen= Employee(201, "Naveen", 30000)
Naveen.employee_details1()

class Employee:
    def __init__(self,eid,name,sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def update_hike(self,rating):
        print("emp details before hike:", self.eid, self.name, self.sal)
        if rating == 5:
            self.sal = self.sal + self.sal * 30/100
        elif rating == 3:
            self.sal = self.sal + self.sal * 20/100
        elif rating == 2:
            self.sal = self.sal + self.sal * 10/100
        else:
            print("No hike applicable for you.improve yourself!!")
            print("emp details after hike:", self.eid,self.name,self.sal)
Naveen = Employee(201, "Naveen", 30000)
Naveen.update_hike(0)






































