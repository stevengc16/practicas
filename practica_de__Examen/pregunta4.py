#Se tiene el siguiente problema en la empresa Parqueos Lia: Se quiere llevar el control del cobro por vehículo en su parqueo, 
# así como de los campos disponibles. La empresa cuenta con 25 espacios para vehículos, para lo cual lo contratan para que diseñe la aplicación usando python que resuelva el problema. 
#El parqueo funciona de la siguiente manera.
#Cada vez que ingresa un vehículo al parqueo, debe descontar en uno la cantidad de espacios disponibles.

# indico el maximo de espacios y inicializo los campos disponibles en 0
espacio_maximo = 25

espacio_usado = 0

# le doy la bienvenida al cliente    
print ("Hola bienvenido al parqueo Lia")
 
 #inicializo  while y defino el maximo de vueltas
while espacio_usado <= 25:

#solicito datos al usuario
 nombre= input("por favor anote su nombre para guardar su espacio: ")

 cantidad= int(input("Por favor digite la cantidad de vehiculos que desea guardar: "))

# formulo la operacion y doy el resultado
 if (espacio_usado + cantidad <= espacio_maximo):
    espacio_usado += cantidad
    resultado = espacio_maximo - espacio_usado
    
    print ("Hay", resultado, "campos disponibles y en el parqueo se encuentran", espacio_usado, "carros")
    
 else: print("ya no hay campos disponibles")
 
 #finalizo bucle while
 pregunta = input ("desea agregar otro vehiculo (s/n)?")
 
 if (pregunta.lower() == "n"):
     break
    
