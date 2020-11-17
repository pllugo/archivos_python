#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.3"


import csv


def contar_caracteres(lista):#Función para contar cantidad de caracteres de una lista
    cantidad_letras = 0
    contar_espacios = 0
    for i in range(len(lista)):
        for j in lista[i]:
            if (j.isalpha()):#Aqui veo si hay caracteres alfabeticos
                cantidad_letras += 1
            else:
                if j == " ":
                    contar_espacios += 1
                else:
                    continue
    resultado = cantidad_letras + contar_espacios
    print("Existen {} caracteres, los cuales {} son palabras y {} espacios".format(resultado,cantidad_letras,contar_espacios))
    return resultado


def promedio(sumatoria,cantidad):#función promedio
    if cantidad != 0:
        resultado_promedio = sumatoria / cantidad
    else:
        resultado_promedio = 0
    return round(resultado_promedio, 2)


def ej1():
    print("Cuenta caracteres")
    
    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    archivo = open("texto.txt","r")
    lineas = archivo.readlines()
    resultado = contar_caracteres(lineas)#Llamo a la función para dar la cantidad de caracteres
    print("La cantidad de caracteres ingresados son:", resultado)
    archivo.close()


def ej2():
    print("Transcribir!")
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open("escritura.txt", "w")
    while True:
        texto = str(input("Ingrese el texto a almacenar\n"))
        if texto != " ":
            fo.write(texto)
            fo.write("\n")
        else:
            break
    fo.close()#Debo cerrar el archivo para luego leerlo y contar los caracteres
    archivo_nuevo = open("escritura.txt","r")
    lista_escritura = archivo_nuevo.readlines()
    print("La cantidad de lineas agregadas fueron:", len(lista_escritura))
    caracteres_escritura = contar_caracteres(lista_escritura)#Se llama a la función para contar caracteres
    print("Hay {}  de caracteres totales".format(caracteres_escritura))
    archivo_nuevo.close()


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = str(input("Ingrese la cantidad de ambientes que se desea analizar:\n"))
    

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    
    archivo = "propiedades.csv"
    ambientes = 0 #contador de ambientes
    precio = 0
    lista_precios = []#Aqui voy almacenar la lista de precios
    with open(archivo) as csvfile: #Leo el archivo tipo diccionario
        data = list(csv.DictReader(csvfile))

    columna = "ambientes" #palabra clave
    columna_precio = "precio" #palabra clave
    columna_moneda = "moneda" #palabra clave
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        if data[i][columna] == cantidad_ambientes: #Aqui varia son las filas pero la columna
            if data[i][columna_moneda] == "ARS":
                ambientes += 1     
                precio = precio + float(data[i][columna_precio])
                lista_precios.append(float(data[i][columna_precio]))
            else:
                continue
        else:
            continue
    if ambientes != 0:#Encontro ambientes con esas caracteristicas
        print("Hay {} de departamentos {} ambientes disponibles".format(ambientes,cantidad_ambientes))
        print("El promedio de precios es: {} $ ARS".format(promedio(precio, ambientes)))
        lista_precios.sort()#Ordeno la lista generada de menor a mayor
        minimo_precio = lista_precios[0]#El primer valor es el menor precio
        maximo_precio = lista_precios[len(lista_precios) -1]#El último valor el maximo precio
        print("El maximo valor del alquiler es: {} $ ARS para apartamentos {} ambientes".format(maximo_precio, cantidad_ambientes))
        print("El mínimo valor del alquiler es: {} $ ARS para apartamentos {} ambientes".format(minimo_precio,cantidad_ambientes))
    else:#Ingresó una cantidad de ambientes diferentes
        print("No se encontró apartamentos con esas caracteristicas")


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    # ej2()
    # ej3()
