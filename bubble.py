# Bibliotecas
import time

# Instancia variável início
inicio = time.time()

# Bloco principal do código 
def bubbleSort(arr):
    n = len(arr)
    comparisons = 0  # Contador de comparações
    swaps = 0       # Contador de trocas
    
    # Travessia por todos os elementos
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            comparisons += 1  # Incrementa o contador de comparações

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swaps += 1  # Incrementa o contador de trocas
        if swapped == False:
            break
    
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

input_file = "C:/Users/Public/paa/input.txt"  # Lembrar do nome do input
output_file = "C:/Users/Public/output.txt"

# Ler input do arquivo
arr = read_input_file(input_file)

# Ordenar o array e contar comparações e trocas
comparisons, swaps = bubbleSort(arr)

# Escreve o array ordenado no arquivo
write_output_file(output_file, arr)

# Instancia variável fim
fim = time.time()

# Calcula o tempo de execução
delta = round(fim - inicio, 6)  # Apenas 6 casas decimais

# Print
print(f"Tempo de execução: {delta} segundos")
print(f"Número de comparações: {comparisons}")
print(f"Número de trocas: {swaps}")
