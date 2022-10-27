#crear un archivo con los datos de un grupo de n estudiantes, comprendidos por su codigo, apellido, nombres, genero, total de creditos cursados;
# crear un archivo llamado Alumnos para los estudiantes de genero masculino y otro arcvhivo llamado Alumnas para las estudiantes de genero femenino.

import os 
archivo = "alumnos.txt"
f = open(archivo, 'w')
archivo = "alumnas.txt"
g = open(archivo, 'w')
n = int(input("Digite la cantidad de alumnos: "))
for i in range(n):
    codigo = input("Digite código: ")
    apellidos = input("Digite apellidos: ")
    nombres = input("Digite nombres: ")
    genero = input("Digite género: ")
    credito = input("Total créditos: ")
    if genero == "F" or genero == "f":
        g.write(codigo + " " + apellidos + " " + nombres + " " + genero + " " + credito +'\n')
    elif genero == "M" or genero == "m":
        f.write(codigo + " " + apellidos + " " + nombres + " " + genero + " " + credito +'\n')

f.close()
g.close()