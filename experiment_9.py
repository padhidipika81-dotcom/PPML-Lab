#1.What are positional arguments?
#=>Positional arguments are passed to a function in the same order as parameters are defined.
#2.WAP using positional arguments.
def add(a, b):
    return a + b

print(add(5, 10))

#3.What are keyword arguments?
#=> Keyword arguments are passed using parameter names, order does not matter.

#4.WAP using keyword arguments.
def student(name, course):
    print("Name:", name)
    print("course:", course)

student(course="Python", name="Rudra")

#5.What are default arguments?
#=>Default arguments have predefined values; if no value is passed, default is used.
#6.WAP using default arguments.
def bill(amount=100):
    print("Bill amount:", amount)

bill(500)
bill()

#7.What are arbitrary arguments?
#=>When number of arguments is not fixed, using *args and **kwargs.

#8.AP using *args.
def total(*nums):
    print("sum:", sum(nums))

total(10, 20, 30)

#9.WAP using **kwargs.
def book(**details):
    for k, v in details.items():
        print(k, ":", v)

book(name="python", author="john")

