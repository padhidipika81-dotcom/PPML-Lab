#1.WAP to test string is palindrome or not.
str = "madam"

if str == str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")

#2.WAP to input 3 coefficient values & find the real roots.
import math

a = int(input("Enter the 1st coefficient: "))
b = int(input("Enter the 2nd coefficient: "))
c = int(input("Enter the 3rd coefficient: "))

r1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
r2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)

print(r1)
print(r2)

#3.Find the greatest among 3 unequal numbers.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if (a > b and a > c):
    print("a is greater")
elif (b > a and b > c):
    print("b is greater")
else:
    print("c is greater")

#4.Accept a digit within 0 to 6 and display the week day.
num = int(input("Enter a number: "))

if num == 0:
    print("Sunday")
elif num == 1:
    print("Monday")
elif num == 2:
    print("Tuesday")
elif num == 3:
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5:
    print("Friday")
elif num == 6:
    print("Saturday")
else:
    print("Invalid digit")

#5.WAP to input marks for 5 subjects (max 50 each), find percent and display grade.
math = int(input("Enter math marks: "))
c = int(input("Enter c marks: "))
java = int(input("Enter java marks: "))
python = int(input("Enter python marks: "))
dsa = int(input("Enter dsa marks: "))

secure = math + c + java + python + dsa
percent = (secure / 250) * 100

if percent >= 90 and percent <= 100:
    print("O")
elif percent >= 80 and percent < 90:
    print("E")
elif percent >= 70 and percent < 80:
    print("A")
elif percent >= 60 and percent < 70:
    print("B")
elif percent >= 50 and percent < 60:
    print("C")
else:
    print("F")

#6. WAP to input an alphabet and check whether it is vowel or consonant.
a = input("Enter the alphabet: ")

vowel = ['a', 'e', 'i', 'o', 'u']

if a in vowel:
    print("vowel")
else:
    print("consonant")

#7.WAP to input two strings and check whether they are equal or not.
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")

if str1 == str2:
    print("equal string")
else:
    print("Not equal")