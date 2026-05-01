"""
Nombre :
Grupo  :
Fecha  :
"""

# Metodo que acepta el porcentaje de un alumno y evalua el grado
def evaluar_grado(porcentaje):
    if porcentaje > 90:
        print("Grado: A")
    elif porcentaje > 80:
        print("Grado: B")
    elif porcentaje >= 60:
        print("Grado: C")
    else:
        print("Grado: D")

#-------------------------------------------------------------------------#
# Metodo que calcula impuestos de una bicicleta
def impuesto_bicicleta(precio):
    impuesto = precio * 0.10
    total = precio + impuesto
    print("El impuesto es:", impuesto)
    print("Total a pagar:", total)

#-------------------------------------------------------------------------#
# Metodo para verificar si un año es bisiesto
def es_bisiesto(anio):
    if anio % 4 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

#-------------------------------------------------------------------------#
# Metodo que muestra el dia de la semana
def dia_semana(num):
    if num == 1:
        print("Lunes")
    elif num == 2:
        print("Martes")
    elif num == 3:
        print("Miercoles")
    elif num == 4:
        print("Jueves")
    elif num == 5:
        print("Viernes")
    elif num == 6:
        print("Sabado")
    elif num == 7:
        print("Domingo")
    else:
        print("Numero invalido")

#-------------------------------------------------------------------------#
# Metodo que muestra el mes y sus dias
def mes_y_dias(num):
    if num == 1:
        print("Enero tiene 31 dias")
    elif num == 2:
        print("Febrero tiene 28 dias")
    elif num == 3:
        print("Marzo tiene 31 dias")
    elif num == 4:
        print("Abril tiene 30 dias")
    elif num == 5:
        print("Mayo tiene 31 dias")
    elif num == 6:
        print("Junio tiene 30 dias")
    elif num == 7:
        print("Julio tiene 31 dias")
    elif num == 8:
        print("Agosto tiene 31 dias")
    elif num == 9:
        print("Septiembre tiene 30 dias")
    elif num == 10:
        print("Octubre tiene 31 dias")
    elif num == 11:
        print("Noviembre tiene 30 dias")
    elif num == 12:
        print("Diciembre tiene 31 dias")
    else:
        print("Numero invalido")

#-------------------------------------------------------------------------#
# Imprimir los primeros 10 numeros naturales
def numeros_naturales():
    for i in range(1,11):
        print(i)

#-------------------------------------------------------------------------#
# Imprimir los primeros 10 numeros impares
def numeros_impares():
    for i in range(1,20,2):
        print(i)

#-------------------------------------------------------------------------#
# Numeros naturales en orden descendente
def naturales_descendentes():
    for i in range(10,0,-1):
        print(i)

#-------------------------------------------------------------------------#
# Tabla de multiplicar
def tabla_multiplicar(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

#-------------------------------------------------------------------------#
# Producto de los digitos de un numero
def producto_digitos(num):
    producto = 1
    for digito in str(num):
        producto = producto * int(digito)
    print("Producto de los digitos:", producto)

#-------------------- EJEMPLOS DE USO --------------------#

evaluar_grado(85)
impuesto_bicicleta(1000)
es_bisiesto(2024)
dia_semana(5)
mes_y_dias(7)
numeros_naturales()
numeros_impares()
naturales_descendentes()
tabla_multiplicar(6)
producto_digitos(123)