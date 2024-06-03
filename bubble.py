#bibliotecas
import time

#1.instancia variavel inicio 

inicio = time.time()


#bloco principal do codigo 
def bubbleSort(arr):
    n = len(arr)
    
    # Travessia por todos os elementos
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arr = [int(line.strip()) for line in lines]
    return arr

def write_output_file(file_path, arr):
    with open(file_path, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

input_file = "C:/Users/Public/paa/randomly_shuffled_array_1000.txt"  #lembrar do nome do input
output_file = "C:/Users/Public/output.txt"


#Ler input do arquivo
arr = read_input_file(input_file)

# Sorteio do array 
bubbleSort(arr)

# Escreve o array sorteado no arquivo
write_output_file(output_file, arr)



#instancia variavel fim
fim = time.time()

#instancia variavel delta (fim menos inicio)
delta = round (fim - inicio,6) # apenas 6 casas decimais

#print
print(f"tempo de execução: {delta} segundos")
