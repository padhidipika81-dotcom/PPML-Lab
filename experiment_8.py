#1.WAP to find the square of a number using function.
def s(a):
    return a * a

a = 2
print(s(a))

#2.WAP to check whether a number is even or odd using function.
def eo(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

a = 5
eo(a)

#3.WAP to find the sum of two numbers using function.
def s_n(a, b):
    return a + b

a = 5
b = 6
print(s_n(a, b))

#4.WAP to find factorial of a number using function.
def factorial(a):
    fact = 1
    for i in range(1, a + 1):
        fact = fact * i
    return fact

a = 5
print(factorial(a))

#5.WAP to check whether a number is prime or not using function.
def prime_or_not(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

a = 6
print(prime_or_not(a))

#6.WAP to find reverse of a string using function.
def reverse_string(a):
    return a[::-1]

a = "Rudra Prasad Panigrahi"
print(reverse_string(a))

#7.WAP to count vowels in a string using function.
def count_vowel(a):
    count = 0
    for ch in a:
        if ch in "aeiouAEIOU":
            count += 1
    return count

a = "Rudra Prasad Panigrahi"
print(count_vowel(a))

#8.WAP to find largest of 3 numbers using function.
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = 5
b = 6
c = 10
print(largest(a, b, c))

#9.WAP to find simple interest using function.
def si(p, r, t):
    return (p * r * t) / 100

p = 100
r = 3
t = 2
print(si(p, r, t))

#10.WAP that accept list and return sum of elements.
def sum_a(a):
    return sum(a)

a = [1, 2, 3, 4, 5]
print(sum_a(a))