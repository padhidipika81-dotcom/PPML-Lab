#1.Write a program to print "Welcome to Python world"
print("Welcome to Python world")

#2.Write a program to input your name, age and address and print them.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

print("your name is", name)
print("your age is", age)
print("your address is", address)

#3.Write a program to find the area and perimeter of a circle.
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print("Area of the circle is", area)

perimeter = 2 * math.pi * radius
print("Perimeter of the circle is", perimeter)

#4.WAP to input two integers, find sum and product of them.
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

sum = a + b
print("sum is", sum)

product = a * b
print("product is", product)

#5.WAP to input two numbers, swap them using 3rd variable.
a = int(input("Enter the 1st integer: "))
b = int(input("Enter the 2nd integer: "))

temp = a
a = b
b = temp

print(a)
print(b)

#6.WAP to input two numbers, swap them without 3rd variable.
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

a = a + b
b = a - b
a = a - b

print(a)
print(b)

#7.WAP to input your marks for three subjects then find sum and percentage.
sub1 = int(input("Enter your marks in sub1: "))
sub2 = int(input("Enter your marks in sub2: "))
sub3 = int(input("Enter your marks in sub3: "))

sum = sub1 + sub2 + sub3
percentage = (sum / 300) * 100

print("sum is", sum)
print("percentage is", percentage)

#8.WAP to find the area and perimeter of a triangle.
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c
print(perimeter)

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(area)