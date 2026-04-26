%%writefile Proyecto_Matrices/entrada.py
import numpy as np

def solicitar_matriz(nombre):
    while True:
        try:
            filas = int(input(f"Ingrese número de filas para Matriz {nombre}: "))
            cols = int(input(f"Ingrese número de columnas para Matriz {nombre}: "))
            if filas <= 0 or cols <= 0:
                print("Las dimensiones deben ser mayores a cero.")
                continue
            break
        except ValueError:
            print("Error: Ingrese un número entero válido para las dimensiones.")

    matriz = []
    print(f"Ingrese los elementos de la Matriz {nombre} fila por fila:")
    for i in range(filas):
        while True:
            try:
                fila_str = input(f"Fila {i+1} (separe los {cols} elementos por espacios): ")
                fila = [float(x) for x in fila_str.split()]
                if len(fila) != cols:
                    print(f"Error: Debe ingresar exactamente {cols} elementos.")
                    continue
                matriz.append(fila)
                break
            except ValueError:
                print("Error: Ingrese solo valores numéricos.")

    return np.array(matriz)

def obtener_matrices_AB():
    print("--- Entrada de Matrices ---")
    A = solicitar_matriz("A")
    print("\n")
    B = solicitar_matriz("B")
    return A, B
