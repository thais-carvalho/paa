# Bibliotecas
import time

# Instancia variavel inicio
inicio = time.time()

# Contadores globais
comparisons = 0
assignments = 0

# Função para mesclar dois subarrays de array[]
def merge(array, left, mid, right):
    global comparisons, assignments
    subArrayOne = mid - left + 1
    subArrayTwo = right - mid

    # Cria arrays temporários
    leftArray = [0] * subArrayOne
    rightArray = [0] * subArrayTwo

    # Copia dados para os arrays temporários leftArray[] e rightArray[]
    for i in range(subArrayOne):
        leftArray[i] = array[left + i]
    for j in range(subArrayTwo):
        rightArray[j] = array[mid + 1 + j]

    indexOfSubArrayOne = 0  # Índice inicial do primeiro subarray
    indexOfSubArrayTwo = 0  # Índice inicial do segundo subarray
    indexOfMergedArray = left  # Índice inicial do array mesclado

    # Mescla os arrays temporários de volta em array[left..right]
    while indexOfSubArrayOne < subArrayOne and indexOfSubArrayTwo < subArrayTwo:
        comparisons += 1
        if leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]:
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
            indexOfSubArrayOne += 1
        else:
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
            indexOfSubArrayTwo += 1
        assignments += 1
        indexOfMergedArray += 1

    # Copia os elementos restantes de leftArray[], se houver
    while indexOfSubArrayOne < subArrayOne:
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne]
        indexOfSubArrayOne += 1
        assignments += 1
        indexOfMergedArray += 1

    # Copia os elementos restantes de rightArray[], se houver
    while indexOfSubArrayTwo < subArrayTwo:
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo]
        indexOfSubArrayTwo += 1
        assignments += 1
        indexOfMergedArray += 1

# Função para ordenar o array utilizando Merge Sort
def mergeSort(array, begin, end):
    if begin >= end:
        return

    mid = begin + (end - begin) // 2
    mergeSort(array, begin, mid)
    mergeSort(array, mid + 1, end)
    merge(array, begin, mid, end)

# Função para ler o arquivo de entrada
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

# Função para escrever o array ordenado no arquivo de saída
def write_output_file(file_path, arr):
    with open(file_path, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

input_file = "C:/Users/Public/paa/input.txt"
output_file = "C:/Users/Public/output.txt"

# Ler a entrada do arquivo 
arr = read_input_file(input_file)

# Ordena o array
mergeSort(arr, 0, len(arr) - 1)

# Escreve o array ordenado no arquivo
write_output_file(output_file, arr)

# Instancia variável fim
fim = time.time()

# Instancia variável delta (fim menos início)
delta = round(fim - inicio, 6)  # Apenas 6 casas decimais

# Print
print(f"Tempo de execução: {delta} segundos")
print(f"Número de comparações: {comparisons}")
print(f"Número de atribuições: {assignments}")
