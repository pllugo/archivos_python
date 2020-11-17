#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.2"

import csv

def convertir_segundos(segundos):#Función para convertir los segundos en hh:mm:s
    hora = segundos // 60 // 60
    minuto = segundos // 60 % 60
    segundo = segundos % 60
    return hora, minuto, segundo


def informacion_diccionario(datos):#Función para generar listas del diccionario
    with open(datos) as csvfile: #Leo el archivo tipo diccionario
        datos_diccionario = list(csv.DictReader(csvfile))
    columna_resultados_swim = "Swim"
    columna_resultados_bike = "Bike"
    columna_resultados_run = "Run"
    lista_swim = []
    lista_bike = []
    lista_run = []
    cantidad_filas = len(datos_diccionario)
    contador = 0
    for i in range(3, cantidad_filas):
        if datos_diccionario[i][columna_resultados_swim] != 0:
            contador += 1
            lista_swim.append(datos_diccionario[i][columna_resultados_swim])    
            lista_bike.append(datos_diccionario[i][columna_resultados_bike])        
            lista_run.append(datos_diccionario[i][columna_resultados_run])
        else:
            print("El diccionario esta vacio")
            break
    csvfile.close()
    return lista_swim, lista_bike, lista_run, contador


def conocimiento(nombre_archivo, divisiones, sub_divisiones):#Función para generar listas individuales
    with open(nombre_archivo) as csvfile: #Leo el archivo tipo diccionario
        data = list(csv.DictReader(csvfile))
    columna = "Division" #palabra clave
    columna_swim = "Swim"
    columna_bike = "Bike"
    columna_run = "Run"
    lista = []#Lista en vacio
    cantidad_filas = len(data)
    contador = 0
    resultados = {}#Diccionario de resultados para categoria Swim + Bike + Run
    csvfile = open('diccionario_resultados.csv', 'w', newline='')
    header = [divisiones, "Swim", "Bike", "Run"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    writer.writerow(resultados)
    for i in range(cantidad_filas):
            if data[i][columna] == divisiones: 
                if sub_divisiones == 1:#Swim
                    if data[i][columna_swim] != "" and data[i][columna_swim] != " ":
                        contador += 1
                        lista.append(data[i][columna_swim])
                    else:
                        continue
                else:
                    if sub_divisiones == 2:#Bike
                        if data[i][columna_bike] != "" and data[i][columna_bike] != " ":
                            contador += 1
                            lista.append(data[i][columna_bike])
                        else:
                            continue
                    else:
                        if sub_divisiones == 3:#Run
                            if data[i][columna_run] != "" and data[i][columna_run] != " ":
                                contador += 1
                                lista.append(data[i][columna_run])
                            else:
                                continue
                        else:
                            if sub_divisiones == 4:#todas en esa división
                                if (data[i][columna_swim] != "" and data[i][columna_swim] != " " and 
                                    data[i][columna_bike] != "" and data[i][columna_bike] != " " and 
                                    data[i][columna_run] != "" and data[i][columna_run] != " "):
                                        contador += 1
                                        resultados= {divisiones : contador, "Swim" : data[i][columna_swim], "Bike": data[i][columna_bike], "Run": data[i][columna_run]}
                                        writer.writerow(resultados)
                                else:
                                    continue
                            else:
                                continue
            else:
                continue
    csvfile.close()
    return lista, contador


def informacion(lista_categoria, contador_categoria, dato_categoria):#Función para sub-categorias
    if contador_categoria != 0 and lista_categoria:#contador de sub-categorias
        lista_total = []
        for j in range(len(lista_categoria)):
            tiempo = lista_categoria[j]
            if tiempo != "" and tiempo != " ":#En este punto extraigo hora, minuto y segundo
                hora = int(tiempo[:2])      #de la lista generada
                minutos = int(tiempo[3:5])
                segundos = int(tiempo[6:8])
                tiempo_total = hora*3600 + minutos*60 + segundos
                lista_total.append(tiempo_total)
            else:
                print("Existen espacios en blanco")
        lista_total.sort()#ordeno la lista de menor a mayor
        mayor_valor = lista_total[len(lista_total)-1]#el mayor valor esta en la ultima posición
        hora_mayor, minuto_mayor, segundo_mayor = convertir_segundos(mayor_valor)
        menor_valor = lista_total[0]#el menor valor esta en la primera posición
        hora_menor, minuto_menor, segundo_menor = convertir_segundos(menor_valor)
        print("El mayor tiempo fue: {} s ó {}h:{}min:{}s".format(mayor_valor, hora_mayor, minuto_mayor, segundo_mayor))
        print("El menor tiempo fue: {} s ó {}h:{}min:{}s".format(menor_valor, hora_menor, minuto_menor, segundo_menor))
        sumatoria = 0
        for y in range(len(lista_total)):
            sumatoria = sumatoria + int(lista_total[y])
        promedio = sumatoria / len(lista_total)
        promedio_hora, promedio_min, promedio_segundos = convertir_segundos(promedio)
        if dato_categoria == 1:#Swim
            print("Hay {} personas en la categoria {}".format(contador_categoria,"Swim"))
            print("El promedio de la categoria {} fue de: {} s ó {}h:{}min:{}s".format("Swim",round(promedio,2),promedio_hora, promedio_min, promedio_segundos))
        else:
            if dato_categoria == 2:#Bike
                print("Hay {} personas en la categoria {}".format(contador_categoria,"Bike"))
                print("El promedio de la categoria {} fue de: {} s ó {}h:{}min:{}s".format("Bike",round(promedio,2),promedio_hora, promedio_min, promedio_segundos))
            else:#Run
                print("Hay {} personas en la categoria {}".format(contador_categoria,"Run"))
                print("El promedio de la categoria {} fue de: {} s ó {}h:{}min:{}s".format("Run",round(promedio,2),promedio_hora, promedio_min, promedio_segundos))
    else:
        print("No se encontró categorias con esas caracteristicas")


def ironman():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    archivo = "2019 Ironman world Championship Results.csv"
    archivo_diccionario = "diccionario_resultados.csv"
    categorias = str(input("""Ingrese la categoria que se desea analizar:
                            MPRO
                            M45-49
                            M25-29
                            M18-24\n"""))
    sub_categoria = int(input("""Ingrese la sub-categoria que se desea analizar:
                                1 = Swim
                                2 = Bike
                                3 = Run
                                4 = Swim + Bike + Run\n""")) #Categoria 4 porque tomo las personas que
                                                            #completaron las 3 categorias
                                                            #Hay personas que solo estaban en Swim, Bike o Run
    if categorias == "MPRO":   
        lista, cantidad = conocimiento(archivo, categorias, sub_categoria)
        if sub_categoria == 4: #Llamo a la función para generar las listas
            lista_nado, lista_bicicleta, lista_correr, cantidad = informacion_diccionario(archivo_diccionario)
            informacion(lista_nado, cantidad, 1)
            informacion(lista_bicicleta, cantidad, 2)
            informacion(lista_correr, cantidad, 3)
        else:
            informacion(lista, cantidad, sub_categoria)#Aqui genera la lista individual                        
    else:                                                        
        if categorias == "M45-49":
            lista, cantidad = conocimiento(archivo, categorias, sub_categoria)
            if sub_categoria == 4: 
                lista_nado, lista_bicicleta, lista_correr, cantidad = informacion_diccionario(archivo_diccionario)
                informacion(lista_nado, cantidad, 1)
                informacion(lista_bicicleta, cantidad, 2)
                informacion(lista_correr, cantidad, 3)
            else:
                informacion(lista, cantidad, sub_categoria)
        else:
            if categorias == "M25-29":
                lista, cantidad = conocimiento(archivo, categorias, sub_categoria)
                if sub_categoria == 4: #Llamo a la función para generar la lista
                    lista_nado, lista_bicicleta, lista_correr, cantidad = informacion_diccionario(archivo_diccionario)
                    informacion(lista_nado, cantidad, 1)
                    informacion(lista_bicicleta, cantidad, 2)
                    informacion(lista_correr, cantidad, 3)
                else:
                    informacion(lista, cantidad, sub_categoria)
            else:
                if categorias == "M18-24":
                    lista, cantidad = conocimiento(archivo, categorias, sub_categoria)
                    if sub_categoria == 4: 
                        lista_nado, lista_bicicleta, lista_correr, cantidad = informacion_diccionario(archivo_diccionario)
                        informacion(lista_nado, cantidad, 1)
                        informacion(lista_bicicleta, cantidad, 2)
                        informacion(lista_correr, cantidad, 3)
                    else:
                        informacion(lista, cantidad, sub_categoria)
                else:
                    print("No existe esa división o categoria")


if __name__ == '__main__':
    print("Ejercicios de práctica extra")
    ironman()
