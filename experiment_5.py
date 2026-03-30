#1.Generate fibonacci series between 0 to 1000 then find the sum of even valued terms.
lst = []
a = 0
b = 1

for i in range(1000):
    lst.append(a)
    a, b = b, a + b

sum = 0
for i in lst:
    if (i % 2 == 0):
        sum = sum + i

print(lst)
print("The sum of all even:", sum)

#2.WAP that loops over a sequence of elements of a list, tuple, dictionary & set.
lst = ["Rudra", 84, 19]
tuple1 = (10, 20, 30, 40, 50)
dict1 = {"name": "Rudra", "roll": 126}
set1 = {1, 2, 3, 4, 5}

for i in lst:
    print(f"The list value are: {i}")

for i in tuple1:
    print(f"The tuple values are: {i}")

for key, value in dict1.items():
    print("The dictionary key, values are:")
    print(key, ":", value)

for i in set1:
    print(f"The set values are: {i}")

#3.WAP that find the Fahrenheit for given Celsius from the list.
celsius_list = [0, 10, 20, 30, 40]
fahrenheit = []

for c in celsius_list:
    f = (9/5) * c + 32
    fahrenheit.append(f)

print("fahrenheit:", fahrenheit)

#4.WAP to create an empty list & input a group of numbers into the list, remove duplicate elements and sort in ascending order then display.
nums = []
n = int(input())

for i in range(n):
    x = int(input("Enter element: "))
    nums.append(x)

unique_nums = list(set(nums))
unique_nums.sort()

print("List after removing duplicates & sorting:")
print(unique_nums)


