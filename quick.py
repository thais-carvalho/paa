# Bibliotecas
import time

# Instancia variavel inicio
inicio = time.time()

# Contadores globais
comparisons = 0
swaps = 0

# Função para encontrar a posição de partição
def partition(array, low, high):
    global comparisons, swaps
    # Escolhe o último elemento como pivô
    pivot = array[high]

    # Ponteiro para o elemento maior
    i = low - 1

    # Percorre todos os elementos
    # compara cada elemento com o pivô
    for j in range(low, high):
        comparisons += 1
        if array[j] <= pivot:
            # Se o elemento menor que o pivô for encontrado
            # troque-o com o elemento maior apontado por i
            i = i + 1

            # Trocando elemento em i com elemento em j
            array[i], array[j] = array[j], array[i]
            swaps += 1

    # Troca o elemento pivô com
    # o elemento maior especificado por i
    array[i + 1], array[high] = array[high], array[i + 1]
    swaps += 1

    # Retorna a posição de onde a partição é feita
    return i + 1

# Função para executar o quicksort
def quickSort(array, low, high):
    if low < high:
        # Encontra o elemento pivô tal que
        # elementos menores que o pivô estão à esquerda
        # elementos maiores que o pivô estão à direita
        pi = partition(array, low, high)

        # Chamada recursiva à esquerda do pivô
        quickSort(array, low, pi - 1)

        # Chamada recursiva à direita do pivô
        quickSort(array, pi + 1, high)

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
quickSort(arr, 0, len(arr) - 1)

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
