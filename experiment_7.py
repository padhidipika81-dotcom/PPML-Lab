#1.WAP to create a list containing natural numbers from 1 to n and find sum, average, largest, smallest and create another list of numbers divisible by 3.
n = int(input("Enter the value of n: "))
list1 = []

for i in range(1, n + 1):
    list1.append(i)

total = 0
largest = list1[0]
smallest = list1[0]

for num in list1:
    total = total + num
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

average = total / n

list2 = []
for num in list1:
    if num % 3 == 0:
        list2.append(num)

print("First list:", list1)
print("sum =", total)
print("average =", average)
print("largest =", largest)
print("smallest =", smallest)
print("second list (divisible by 3):", list2)

#2.WAP to generate all prime numbers within a given range.
m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

print("prime numbers between", m, "and", n, "are:")
for num in range(m, n + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

#3.WAP to create a string (paragraph) and find number of words, number of palindrome words and print each word in reverse.
para = input("Enter a paragraph: ")
words = para.split()

word_count = 0
for w in words:
    word_count += 1

pal_count = 0
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    if w.lower() == rev.lower() and len(w) > 1:
        pal_count += 1

print("Total number of words:", word_count)
print("Number of palindrome words:", pal_count)

print("Each word in reverse:")
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    print(rev)

