#1.WAP that print the decimal equivalent of 1/2, 1/3, … up to 1/100
i = 1
while (i <= 100):
    value = 1 / i
    print(value)
    i += 1

#2.WAP to test a number is prime or not.
num = int(input("Enter a number: "))
i = 1
count = 0

while (i <= num):
    if (num % i == 0):
        count += 1
    i += 1

if (count == 2):
    print("prime")
else:
    print("Not prime")

#3.WAP to find the GCD of 3 numbers.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

i = 1
gcd = 0

while (i <= a and i <= b and i <= c):
    if (a % i == 0 and b % i == 0 and c % i == 0):
        gcd = i
    i += 1

print("The gcd of 3 numbers is:", gcd)

#4.Find sum of digits of a +ve number.
num = int(input("Enter a number: "))
sum = 0

while (num != 0):
    rem = num % 10
    sum = sum + rem
    num = num // 10

print("The sum of digits is:", sum)

#5.WAP to test a number is palindrome or not.
num = int(input("Enter a number: "))
rev = 0
org = num

while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if (org == rev):
    print("palindrome no")
else:
    print("Not palindrome")

#6.Find factorial of a number using while loop.
num = int(input("Enter a number: "))
fact = 1
i = 1

while (i <= num):
    fact = fact * i
    i += 1

print(f"The factorial of {num} is {fact}")

#7.Print Fibonacci series upto n terms.
n = int(input("Enter a number upto which fibonacci series will calculated: "))

a = 0
b = 1

print("fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#8.WAP to reverse a number using while loop.
num = int(input("Enter a number: "))
rev = 0

while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

print(f"The reverse of {num} is {rev}")
