print(".....OOPs in python.....\n\n")

class Faculty:
    def data(self):
        self.name = input ("Enter the name of Faculty: ")
        self.salary = int(input("Enter the salary obtained: "))
        self.subject = input ("Enter the subject assigned: ")
    def display(self):
        print("\nFaculty Name:",(self.name))
        print("Salary obtained:",(self.salary))
        print("subject assigned:",(self.subject))
        
    def greet(self):
        print("\nGood Morning Thank you for providing the information! Have a great Day...",self.name)
        
    def salaryEvalution(self):
        if self.salary >= 10000:
            print("status : Good")
        else:
            print("Status : Bad")
            
        
s1 = Faculty()
s1.data()
s1.display()
s1.salaryEvalution()
s1.greet()