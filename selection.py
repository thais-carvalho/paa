#bibliotecas
import time

#1.instancia variavel inicio 

inicio = time.time()

#bloco principal do codigo 
def selectionSort(arr):
    # Travessia por todos os elementos do Array 
    for i in range(len(arr)-1):
        # Encontre o menor elemento nos arrays restantes 
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Troca o menor elemento encontrado com o primeiro elemento
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

input_file = "C:/Users/Public/paa/randomly_shuffled_array_1000.txt"
output_file = "C:/Users/Public/output.txt"

# Ler a entrada do arquivo
arr = read_input_file(input_file)

# Sorteio do arreio
selectionSort(arr)

#Escreve o array sorteado no arquivo
write_output_file(output_file, arr)

#instancia variavel fim
fim = time.time()

#instancia variavel delta (fim menos inicio)
delta = round (fim - inicio,6) # apenas 6 casas decimais

#print
print(f"tempo de execução: {delta} segundos")

