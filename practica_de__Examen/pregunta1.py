#Realice un programa que administre la venta de tiquetes de un cine de tal forma que el valor del tiquete es de 2000 colones y el impuesto por tiquete es de 5%. 
#Si se da el caso que el cliente compra más de 3 tiquetes se le realiza un descuento del 10% al total de la compra. Al final se debe imprimir la cantidad de tiquetes,
# el total, el impuesto y el descuento en colones.

#Paso 1 crear funciones para hacer los calculos.
#paso 2 saludar al usuario y pedirle los Datos
#paso 3 con los datos proporcionados usar if para llamar las funciones y dar el resultado
# imprimir cantidad de tiquetes, el total, el impuesto y el descuento.


#Defino las funciones para las operaciones
def precio_tiquete (cantidad):
    valor = cantidad * 2000
    impuesto = valor * 0.05
    total_pagar = valor + impuesto
    print ("nombre de cliente: ",nombre)
    print ("cant. Tiquetes: ", cantidad)
    print ("total. Impuesto: ", impuesto)
    print ("El monto total a pagar es de: ", total_pagar)
    return

def promo_tiquete (cantidad):
    valor = cantidad * 2000
    impuesto = valor * 0.05
    total= valor + impuesto
    descuento = total * 0.10
    total_pagar = total - descuento
    print ("nombre de cliente: ",nombre)
    print ("cant. Tiquetes: ", cantidad)
    print ("total. Impuesto: ", impuesto)
    print ("total: ", total)
    print ("descuento promocional: ", descuento)
    print ("El monto total a pagar es de: ", total_pagar)
    return
    

# Procedo a pedir los datos al usuario

print ("Hola bienvenido al cine virtual steven")

nombre= input ("Por favor digita tu nombre para proceder con la compra: ")

print ("Bienvenido", nombre, "gracias por visitarnos" )

cantidad= float(input("por favor digite la cantidad de boletos que desea comprar: "))

if (cantidad < 3):
    precio_tiquete (cantidad)
    
elif (cantidad >= 3):
    promo_tiquete (cantidad)
    
else: print ("Por favor digite un monto correcto")