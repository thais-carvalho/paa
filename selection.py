def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)-1):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]




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
selectionSort(arr)

# Write sorted array to file
write_output_file(output_file, arr)
