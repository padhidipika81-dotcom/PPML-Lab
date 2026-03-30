#1.WAP for ndarray object, indexing & slicing
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print("Array:\n", arr)

print("Element at (0,1):", arr[0,1])
print("Row 1:", arr[1])
print("Column 2:", arr[:,1])

#2.WAP for data types & structures in NumPy
arr = np.array([1,2,3], dtype=int)
print("Data type:", arr.dtype)

arr = arr.astype(float)
print("Updated type:", arr.dtype)

#3.WAP for NumPy array properties
ones_array = np.ones((2,3))
zeros_array = np.zeros((2,3))
empty_array = np.empty((2,3))

print("Ones:\n", ones_array)
print("Zeros:\n", zeros_array)
print("Empty:\n", empty_array)

arr = np.array([[1,2,3],[4,5,6]])
print("Shape of array:", arr.shape)

reshaped = arr.reshape((3,2))
print("Reshaped array:\n", reshaped)
#NumPy array functions
arr1 = np.array([1,2,3])

copy_arr = arr1.copy()
view_arr = arr1.view()

print("Original:", arr1)
print("Copy:", copy_arr)
print("View:", view_arr)

arr2 = np.array([1,2])
arr3 = np.array([3,4])

concatenated = np.concatenate((arr2, arr3))
print("Concatenated:", concatenated)

arr = np.array([5,2,9,1])
print("Sorted array:", np.sort(arr))


#4.WAP for statistical operations & broadcasting
arr = np.array([1,2,3,4])

print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Product:", arr.prod())

print("Broadcasted result:", arr + 5)

#5.WAP for saving & loading arrays
arr = np.array([1,2,3,4])

np.save("my_array", arr)
loaded_arr = np.load("my_array.npy")

print("Loaded array:", loaded_arr)

#pandas

#1.WAP to create & work with Pandas Series
import pandas as pd

data = [10,20,30]
labels = ['a','b','c']

series = pd.Series(data, index=labels)

print("Pandas Series:")
print(series)

print("Value at label b:", series['b'])

#2.WAP to create & manipulate DataFrame
data = {
    'Name': ['Alice','Bob','Charlie'],
    'Age': [25,30,35],
    'City': ['New York','San Francisco','Los Angeles']
}

df = pd.DataFrame(data)

print("Data Frame:")
print(df)

print("Age column:")
print(df['Age'])

print(df.loc[1])

#3.WAP to read CSV & JSON files
df_csv = pd.read_csv("sample.csv")
print("DataFrame from CSV:")
print(df_csv)

df_json = pd.read_json("sample.json")
print("DataFrame from JSON:")
print(df_json)
#4.WAP to calculate correlation between columns
data = {
    'Math': [90,85,80,95],
    'Science': [88,82,85,90],
    'English': [78,75,80,85]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

correlation = df.corr()

print("Correlation Matrix:")
print(correlation)