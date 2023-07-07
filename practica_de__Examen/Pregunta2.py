#Realice un programa que calcule el total a pagar por la compra de camisetas. Cada camiseta cuesta 6500. Si se compran 5 camisetas o menos no se realiza descuento. 
# Si se compran más de 5 pero menos de 15 se aplica un 10% de descuento sobre el total de la compra. Si se compran 15 o más se aplica un descuento del 20%. Utilizar 
# un do/while para preguntar al usuario si desea continuar comprando más llantas.

#paso1: Definir funciones operativas para calcular monto.
#Paso2: crear un bucle con while dentro del bucle hacer el proceso de solicitud de datos y resultados.add
#Paso3: crear un if dentro de while para llamar las funciones y dar los resultados
#paso4: Cerrar while y dar una opción para salir del bucle


#Defino variables de funciones de calculo


#Este es por la compra menor de 5 camisetas
def precio_normal (cantidad):
    valor = cantidad * 6500
    print ("el monto a pagar por", cantidad, "es de", valor, "colones")
 
 #esta es por compra mayores a 5 y menores a 15 camisetas   
def precio_10 (cantidad):
    valor = cantidad * 6500
    descuento = valor * 0.10
    total_pagar = valor - descuento
    print ("el monto a pagar por", cantidad, "con un descuento del 10 porciento es de", total_pagar , "colones")
    

 #esta es por compra mayores a 15 o mas camisetas   
def precio_20 (cantidad):
    valor = cantidad * 6500
    descuento = valor * 0.20
    total_pagar = valor - descuento
    print ("el monto a pagar por", cantidad, "con un descuento del 20 porciento es de", total_pagar , "colones")
    
    
#procedo a iniciar el while y a solicitar los datos al cliente
continuar = True
while continuar:
    print ("Hola bienvenido a la mejor tienda virtual de camisetas")
    
    nombre = input("Por favor digite su nombre para continuar con la compra: ")
    
    print ("Es un gusto atenderle", nombre)
    
    cantidad = float(input("Por favor digite la cantidad de camisetas que desea comprar: "))
    
    print ("gracias por digitar la cantidad procederemos con el calculo de su compra")
    
    if (cantidad <= 5):
       precio_normal (cantidad)
    
    elif (cantidad > 5 and cantidad < 15):
        precio_10 (cantidad)
    
    elif (cantidad  >= 15):
        precio_20 (cantidad)
    else: print ("por favor digite un dato correcto")
    
    pregunta = input ("desea realizar otra compra? (s/n): ")
    
    if (pregunta.lower() == "n"):
        continuar = False