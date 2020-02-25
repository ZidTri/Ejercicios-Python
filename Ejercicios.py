#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      estudiantes
#
# Created:     25/02/2020
# Copyright:   (c) estudiantes 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
print ("Hola Mundo")

nombre = input("Como te llamas?")
print ("Hola ", nombre)

numero = int(input("Ingrese un numero positivo"))
if numero >0:
    print("El numero es positivo")
elif numero ==0:
    print("El numero es cero")
else:
    print("El numero es negativo")

uno = int(input("Ingrese un numero"))
dos = int(input("Ingrese otro numero mayor al anterior"))
tres = int(input("Nuevamente ingrese otro numero mayor al anterior"))

if uno<dos & dos<tres:
    print("Los numeros se han ingresado en orden creciente")

i=0
while i<=90:
    print(i+1, i+2, i+3, i+4, i+5, i+6, i+7, i+8, i+9, i+10, "\n")
    i=i+10

i=2
while i<25:
    print(i)
    i=i+2

i=0

lista = input('Escriba la cadena')
lista.remove(" ")
print(lista)

while i<=len(lista):
    if lista== " ":
        lista[i].remove
    ++i

for i in range(len(lista_calificaciones)):
    print(lista[i])


