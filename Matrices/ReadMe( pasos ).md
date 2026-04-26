#Crear el siguiente directorio en el programa:

import os
os.makedirs('Proyecto_Matrices', exist_ok=True)

#COPIAMOS CADA UNO DE LOS MODULOS(".py")  EN EL PROGRAMA (DE PREFERENCIA entrada.py QUE CONTIENE LA CARPETA).

#LUEGO, EJECUTAMOS LA SIGUIENTE LINEA DE CODIGO PARA INICIAR EL PROGRAMA:

import Proyecto_Matrices.main as proyecto

import importlib

importlib.reload(proyecto)

proyecto.ejecutar_programa()
