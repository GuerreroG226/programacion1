%%writefile Proyecto_Matrices/operaciones_matrices.py

import numpy as np

def sumar_matrices(A, B):
  A = np.array(A)
  B = np.array(B)
  if A.shape != B.shape:
    raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
  return A + B

def restar_matrices(A, B):
  A = np.array(A)
  B = np.array(B)
  if A.shape != B.shape:
    raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
  return A - B

def multiplicar_matrices(A, B):
  A = np.array(A)
  B = np.array(B)
  if A.shape[1] != B.shape[0]:
    raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")
  return np.dot(A, B)

def Hadamard_matrices(A, B):
  A = np.array(A)
  B = np.array(B)
  if A.shape != B.shape:
    raise ValueError("Para el producto Hadamard, las matrices deben tener las mismas dimensiones.")
  return A * B

def producto_Kronecker(A, B):
  A = np.array(A)
  B = np.array(B)
  return np.kron(A, B)
