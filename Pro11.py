print(".....OOPs in python.....\n\n")

class Faculty:
    def data(self, name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = subject
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
            
        
f1 = Faculty()
f1.data("DHRUV MAHAJAN",50000,"PAI")
f1.display()
f1.salaryEvalution()
f1.greet()print(".....OOPs in python.....\n\n")

class Faculty:
    def data(self, name, salary, subject):
        self.name = name
        self.salary = salary
        self.subject = subject
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
            
        
f1 = Faculty()
f1.data("DHRUV MAHAJAN",50000,"PAI")
f1.display()
f1.salaryEvalution()
f1.greet()