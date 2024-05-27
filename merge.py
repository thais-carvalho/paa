# Merges two subarrays of array[].
# First subarray is arr[left..mid]
# Second subarray is arr[mid+1..right]
def merge(array, left, mid, right):
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Create temp arrays
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    # Copy data to temp arrays leftArray[] and rightArray[]
    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0  # Initial index of first sub-array
    indexOfSubArrayTwo = 0  # Initial index of second sub-array
    indexOfMergedArray = left  # Initial index of merged array

    # Merge the temp arrays back into array[left..right]
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of left[], if any
    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        indexOfMergedArray += 1

    # Copy the remaining elements of right[], if any
    while indexOfSubArrayTwo < subArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        indexOfMergedArray += 1

# begin is for left index and end is right index
# of the sub-array of arr to be sorted
def mergeSort(array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

# Function to print an array
def printArray(array, size):
    for i in range(size):
        print(array[i], end=" ")
    print()



def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def write_output_file(file_path, arr):
    with open(file_path, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

input_file = "/uploads/input.txt"
output_file = "/myfiles/output.txt"




# Read input from file
arr = read_input_file(input_file)

# Sort the array
mergeSort(arr, 0, len(arr) - 1)

# Write sorted array to file
write_output_file(output_file, arr)
