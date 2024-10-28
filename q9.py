def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

test_arrays = [
    [64, 31, 25, 17, 22, 11, 90],
    [5, 3, 4, 2, 8., 12],
    [3, 0, -2, 5, -3, 7],
    [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
]

for array in test_arrays:
    print(f"Lista antes do bubble sort: {array}")
    bubbleSort(array)
    print(f"Lista depois do bubble sort: {array} \n")
