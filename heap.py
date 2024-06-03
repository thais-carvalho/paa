# Bibliotecas
import time

# Instancia variável início
inicio = time.time()

# Bloco principal do código 
def heapify(arr, N, i, comparisons, swaps):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < N:
        comparisons += 1
        if arr[largest] < arr[l]:
            largest = l

    # See if right child of root exists and is greater than root
    if r < N:
        comparisons += 1
        if arr[largest] < arr[r]:
            largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swaps += 1

        # Heapify the root.
        comparisons, swaps = heapify(arr, N, largest, comparisons, swaps)

    return comparisons, swaps

def heapSort(arr):
    N = len(arr)
    comparisons = 0  # Contador de comparações
    swaps = 0        # Contador de trocas

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        comparisons, swaps = heapify(arr, N, i, comparisons, swaps)

    # One by one extract elements
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        swaps += 1
        comparisons, swaps = heapify(arr, i, 0, comparisons, swaps)

    return comparisons, swaps

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def write_output_file(file_path, arr):
    with open(file_path, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

input_file = "C:/Users/Public/paa/input.txt"
output_file = "C:/Users/Public/output.txt"

# Read input from file
arr = read_input_file(input_file)

# Sort the array and count comparisons and swaps
comparisons, swaps = heapSort(arr)

# Write sorted array to file
write_output_file(output_file, arr)

# Instancia variável fim
fim = time.time()

# Instancia variável delta (fim menos início)
delta = round(fim - inicio, 6)  # Apenas 6 casas decimais

# Print
print(f"Tempo de execução: {delta} segundos")
print(f"Número de comparações: {comparisons}")
print(f"Número de trocas: {swaps}")
