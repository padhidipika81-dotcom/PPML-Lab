#1.WAP to demonstrate inheritance (parent and child class).
class parent:
    def show_parent(self):
        print("This is parent class method")

class child(parent):
    def show_child(self):
        print("This is the child class method")

obj = child()
obj.show_child()
obj.show_parent()
#2.WAP to demonstrate multilevel inheritance.
class grandparent:
    def property(self):
        print("Grandparent has property")

class parent(grandparent):
    def business(self):
        print("parent business")

class child(parent):
    def education(self):
        print("child education")

obj = child()
obj.property()
obj.business()
obj.education()
#3.WAP to demonstrate multiple inheritance.
class father:
    def skill1(self):
        print("Father: can play football")

class mother:
    def skill2(self):
        print("Mother: can cook")

class child(father, mother):
    def skill3(self):
        print("Child skills")

c = child()
c.skill1()
c.skill2()
c.skill3()
#4.Write a program to demonstrate method overriding.
class father:
    def skill(self):
        print("father likes driving")

class child(father):
    def skill(self):
        print("child likes driving")

f = father()
f.skill()

c = child()
c.skill()
#5.WAP to overload + operator.
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("sum:", self.value)

n1 = Number(10)
n2 = Number(20)

n3 = n1 + n2
n3.display()