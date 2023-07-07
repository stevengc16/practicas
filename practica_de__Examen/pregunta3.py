#Realice una aplicación que calcule el total a pagar en una llantera al comprar x(equis) cantidad de llantas, si se compran menos de 5 llantas, 
#el precio de cada una es de $800 y de $650 si se compran 5 o más. Muestre el total a pagar. Utilizar un while debe preguntar al usuario si desea continuar comprando más llantas.

#PAsos
#1- defino funsiones para realizar los calculos y dar respuesta
#2- definimos valor true y iniciar un while ( de aqui en adelante trabajaremos dentro del while)
#3- proceder con la solicitud de datos.
#4- usamos un if para llamar las funciones y dar las respuestas
#5- Cerramos el while con con una pregunta y un if

def precio_normal (cantidad):
    valor= cantidad * 800
    print ("el precio total a pagar es de ", valor, "dolares")
    
def precio_descuento (cantidad):
    valor = cantidad * 650
    print ("el precio total a pagar es de ", valor, "dolares")
    
continuar = True

while continuar:
    
    print("Hola bienvenido a la llantera virtual")
    nombre= input("por favor digite su nombre para continuar con la compra: ")
    
    cantidad= int(input("Por favor digite la cantidad de llantas que desea comprar: "))
    
    print ("Monto registrado acontinuación le daremos el monto a pagar")
    
    if (cantidad < 5):
        precio_normal (cantidad)
        
    elif (cantidad >= 5):
        precio_descuento (cantidad)
        
    else: print ("Por favor digite un monto correcto")
    
    pregunta = input("desea continuar comprando llantas (s/n)?")
    
    if (pregunta.lower() == "n"):
        continuar = False