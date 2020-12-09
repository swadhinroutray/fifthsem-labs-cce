
class Employee:
    EmpList = []
    def __init__(self,id,name,salary, department):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department 
        emp  = ( self.id , self.name,self.salary,self.department)
        Employee.EmpList.append(emp)

    @staticmethod
    def findEmpByID(id):
        for i in Employee.EmpList:
            if i[0] == id:
                print("Employee exist with details: \n")
                print(i[0], end = "\n")
                print(i[1], end = "\n")
                print(i[2], end = "\n")
                print(i[3], end = "\n")
                break
            else: 
                print("Employee Not found")
    @staticmethod
    def getallEmployees():
         for i in Employee.EmpList:
            print("Employee exist with details: \n")
            print(i[0], end = "\n")
            print(i[1], end = "\n")
            print(i[2], end = "\n")
            print(i[3], end = "\n")
            

def main():
    x = int(input("Input number of employees \n"))
    for i in range(x):
        id = int(input("Input ID of Employee: "))
        name = input("Input name of Employee: ")
        salary = input("Input Salary of Employee: ")
        department = input("Input Department of Employee: ")
        Employee(id,name,salary,department)
    IDcheck = int(input("Enter ID of Employee to be checked: "))

    Employee.findEmpByID(IDcheck)
    Employee.getallEmployees()
if __name__ == "__main__":
    main()



                