#bibliotecas
import time
import os
import random

#1.instancia variavel inicio 

inicio = time.time()

#bloco principal do codigo 
def generate_sorted_array(n):
    return list(range(1, n+1))

def generate_reverse_sorted_array(n):
    return list(range(n, 0, -1))

def generate_randomly_shuffled_array(n):
    array = list(range(1, n+1))
    random.shuffle(array)
    return array

def write_array_to_file(array, file_path):
    with open(file_path, 'w') as file:
        for num in array:
            file.write(f"{num}\n")

def generate_arrays_for_sizes(sizes, output_dir):
    for n in sizes:
        sorted_array = generate_sorted_array(n)
        reverse_sorted_array = generate_reverse_sorted_array(n)
        randomly_shuffled_array = generate_randomly_shuffled_array(n)

        write_array_to_file(sorted_array, os.path.join(output_dir, f"sorted_array_{n}.txt"))
        write_array_to_file(reverse_sorted_array, os.path.join(output_dir, f"reverse_sorted_array_{n}.txt"))
        write_array_to_file(randomly_shuffled_array, os.path.join(output_dir, f"randomly_shuffled_array_{n}.txt"))

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 50000, 100000]  # Adjust the array sizes as needed
    output_dir = "C:/Users/Public/"  # Adjust the output directory path as needed

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    generate_arrays_for_sizes(sizes, output_dir)
    print(f"Arrays for sizes {sizes} have been generated and written to files in {output_dir}.")
#instancia variavel fim
fim = time.time()

#instancia variavel delta (fim menos inicio)
delta = round (fim - inicio,6) # apenas 6 casas decimais

#print
print(f"tempo de execução: {delta} segundos")



