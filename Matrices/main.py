import Proyecto_Matrices.operaciones_matrices as ops
import Proyecto_Matrices.entrada as entrada
import Proyecto_Matrices.menu as menu

def ejecutar_programa():
    A, B = entrada.obtener_matrices_AB()

    print("\n--- Matrices Ingresadas ---")
    print("Matriz A:\n", A)
    print("\nMatriz B:\n", B)

    while True:
        opcion = menu.mostrar_menu()

        if opcion == 5:
            print("Saliendo del programa...")
            break

        try:
            resultado = None
            if opcion == 1:
                resultado = ops.sumar_matrices(A, B)
                operacion = "Suma"
            elif opcion == 2:
                resultado = ops.multiplicar_matrices(A, B)
                operacion = "Multiplicación"
            elif opcion == 3:
                resultado = ops.Hadamard_matrices(A, B)
                operacion = "Producto de Hadamard"
            elif opcion == 4:
                resultado = ops.producto_Kronecker(A, B)
                operacion = "Producto de Kronecker"

            print(f"\nResultado de la {operacion}:\n", resultado)
        except ValueError as e:
            print(f"\nError en la operación: {e}")

if __name__ == "__main__":
    ejecutar_programa()
