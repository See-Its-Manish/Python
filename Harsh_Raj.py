class students:
    def __init__(self,name):
        self.name = name
        self.marks = []
        
    def entermarks(self):
        for i in  range(3):
            m = int(input("enter the marks of %s in %d subject: "%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
        
name = input("enter the name of student:")
s1 = students(name)
s1.entermarks()
s1.display()

name = input("enter the name of student:")
s2 = students(name)
s2.entermarks()
s2.display()