#1.WAP to create a list of fruits, display elements in reverse with length & create another list with reverse of each element.
fruits = ["apple", "banana", "mango", "orange"]

print("Reverse order with length:")
for fruit in fruits[::-1]:
    print(fruit, "length", len(fruit))

rev_list = [fruit[::-1] for fruit in fruits]
print("Reversed elements list:", rev_list)

#2.WAP to create a dictionary, then create another dictionary by swapping keys and values & display both.
n = int(input("How many items: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

d2 = {v: k for k, v in d.items()}

print("Original Dictionary:", d)
print("Reversed Dictionary:", d2)

#3.WAP to input a sentence, store words in list, display with index and create another list of numbers, then zip both lists.
sentence = input("Enter a sentence: ")
list1 = sentence.split()

print("List with index:")
for index, word in enumerate(list1):
    print(index, word)

list2 = list(range(1, len(list1) + 1))
list3 = list(zip(list1, list2))

print("Zipped list:", list3)

