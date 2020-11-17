#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.2"

import csv
import re


def contar_lineas(archivo): #Función para contar lineas
    archivo_texto = open(archivo,"r")
    lineas_texto = archivo_texto.readlines()
    cantidad_lineas = len(lineas_texto)
    archivo_texto.close()
    return cantidad_lineas


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''
    dato = contar_lineas("notas.txt")#Llamo a la función para leer un archivo
    print("La cantidad de lineas son: {} , usando una función".format(dato))
    with open('notas.txt') as fi:#creando un programa
        for line in fi:
            print('Linea:', line, end='')
            cantidad_lineas += 1
    print("La cantidad de lineas son: {}".format(cantidad_lineas))


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)
    fi = open("notas.txt", "r")
    fo = open("nuevo.txt", "w")
    for i in fi:
        cantidad_lineas += 1
        fo.writelines(i)
    print(cantidad_lineas)#Imprime la cantidad de lineas que agrega
    fi.close()
    fo.close()
    lineas_nuevas = contar_lineas("nuevo.txt")#Debo cerrar primero el archivo para luego leerlo
    print("La cantidad de lineas son {} del nuevo archivo".format(lineas_nuevas))#imprime la cantidad usando la función
                                                                      #contar_lineas
    
    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
    dos_ambientes = 0
    tres_ambientes = 0
    with open(archivo) as csvfile:#Leo el archivo tipo diccionario
        data = list(csv.DictReader(csvfile))
        
    columna = "ambientes" #palabra clave
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        if data[i][columna] == "2":#Aqui varia son las filas pero la columna
            dos_ambientes += 1     #es fija
        else:
            if data[i][columna] == "3":
                tres_ambientes += 1
    print("Hay {} de departamentos 2 ambientes disponibles".format(dos_ambientes))
    print("Hay {} de departamentos 3 ambientes disponibles".format(tres_ambientes))


def ej4():
    # Ejercicios con diccionarios
    inventario = {"manzanas":6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    '''
    #Creo un archivo csv para hacer un diccionario
    

    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    #otra forma de hacer el diccionario
    print("Programa para hacer un inventario de frutas y verduras:\n")
    while True:
        nombre = str(input("Ingrese la fruta/vverdura o FIN si quiere terminar el programa:\n"))
        if nombre == "FIN":
            break
        else:
            cantidad = str(input("Ingrese la cantidad:\n"))
            inventario[nombre] = cantidad
    print(inventario)


def ej5():
    # Ejercicios con archivos CSV
    inventario = {'Fruta Verdura': 'manzana', 'Cantidad': 10}

    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    print("Programa para hacer un diccionario creando un archivo csv")
    csvfile = open('diccionario.csv', 'w', newline='')
    header = ["Fruta Verdura", "Cantidad"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerow(inventario)
    while True:
        nombre = str(input("Ingrese el nombre de la fruta/verdura o palabra FIN para terminar el programa:\n"))
        if nombre == "FIN":
            break
        else:
            stock = str(input("Ingrese el la cantidad que hay en stock:\n"))
            inventario= {"Fruta Verdura" : nombre, "Cantidad" : stock}#Introduzco los valores al diccionario
            writer.writerow(inventario)
    csvfile.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
