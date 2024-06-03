# Bibliotecas
import time

# Instancia variável início
inicio = time.time()

# Bloco principal do código 
# Função para fazer insertion sort
def insertionSort(arr):
    comparisons = 0  # Contador de comparações
    swaps = 0        # Contador de trocas

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]:
            comparisons += 1  # Incrementa o contador de comparações
            arr[j + 1] = arr[j]
            swaps += 1  # Incrementa o contador de trocas
            j -= 1
        # Incrementa o contador de comparações para a última comparação falhada no while
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key

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

# Ler a entrada do arquivo 
arr = read_input_file(input_file)

# Ordena o array e conta comparações e trocas
comparisons, swaps = insertionSort(arr)

# Escreve o array ordenado no arquivo
write_output_file(output_file, arr)

# Instancia variável fim
fim = time.time()

# Instancia variável delta (fim menos início)
delta = round(fim - inicio, 6)  # Apenas 6 casas decimais

# Print
print(f"Tempo de execução: {delta} segundos")
print(f"Número de comparações: {comparisons}")
print(f"Número de trocas: {swaps}")
