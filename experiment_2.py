#1.Display simple and compound interest.
p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))

si = (p * t * r) / 100
print("The simple interest is:", si)

ci = (p * (1 + (r/100))**t) - p
print("The compound interest is:", ci)

#2.WAP to input first name, middle name & last name into 3 variables & then apply concatenation.
first = input("Enter your 1st name: ")
middle = input("Enter your middle name: ")
last = input("Enter your last name: ")

full = first + middle + last
print("my name is:", full)

#3.WAP to create a list by initializing with 5 different fruits name and display them.
l = ["apple", "Banana", "Mango", "Lemon", "Pineapple"]
print(l)

#4.WAP to create a tuple & display the element of it.
t = ("Rudra", "Python", 5)
print(t)

#5.WAP to create a dictionary, store simple data & then display the key value of it.
dict = {
    "name": "Rudra",
    "roll": 84,
    "subject": "Python"
}

print(dict.keys())
print(dict.values())

for key, value in dict.items():
    print(key, value)

#6.WAP to input a sentence and then print the reverse of it.
sent = input("Enter your sentence: ")
print(sent[::-1])

#7.WAP to input data for int, string, float, Boolean, complex and then display datatype.
i = 10
str = "Hello"
com = 12j
f = 3.14
b = True

print(i, type(i))
print(str, type(str))
print(com, type(com))
print(f, type(f))
print(b, type(b))