#bibliotecas
import time

#1.instancia variavel inicio 

inicio = time.time()


#bloco principal do codigo 
# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)






def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def write_output_file(file_path, arr):
    with open(file_path, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

input_file = "C:/Users/Public/paa/randomly_shuffled_array_1000.txt"
output_file = "C:/Users/Public/output.txt"




# Read input from file
arr = read_input_file(input_file)

# Sort the array
quickSort(arr, 0, len(arr) - 1)

# Write sorted array to file
write_output_file(output_file, arr)




#instancia variavel fim
fim = time.time()

#instancia variavel delta (fim menos inicio)
delta = round (fim - inicio,6) # apenas 6 casas decimais

#print
print(f"tempo de execução: {delta} segundos")

