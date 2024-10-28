def greatestNumber(array):
    max_number = array[0]
    for num in array:
        if num > max_number:
            max_number = num
    
    return max_number

array = [4, 5, 2, 7, 0, 9, 1]
max_number = greatestNumber(array)
print(max_number)