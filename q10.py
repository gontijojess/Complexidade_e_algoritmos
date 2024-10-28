def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

test_arrays = [
    ["banana", "apple", "cherry", "pineapple"],
    ["Brazil", "The United States", "France", "Japan", "China"],
    ["python", "java", "c++", "ruby", "javascript"],
    ["sun", "moon", "star", "jupyter"]
]

for array in test_arrays:
    print(f"Antes do bubble sort: {array}")
    bubbleSort(array)
    print(f"Depois do bubble sort: {array} \n")
