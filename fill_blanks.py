# Given an array containing None values fill in the None values with most recent 
# non None value in the array 

array1 = [1,None,2,3,None,None,5,None] # => [1, 1, 2, 3, 3, 3, 5, 5]

# assuming non null value at arr[0]

def fill_blanks(arr):
    for i in range(len(arr)):
        if arr[i] == None:
            arr.pop(i)
            if i == len(arr):
                arr.append(arr[i - 1])
            else:
                arr.insert(arr[i - 1], arr[i - 1])

    return arr

# another solution

def fill_blanks2(arr):
    valid = 0            
    result = []                 
    for num in arr: 
        if num is not None:    
            result.append(num)
            valid = num
        else:
            result.append(valid)
    return result


# print(fill_blanks(array1))
print(fill_blanks2(array1))
