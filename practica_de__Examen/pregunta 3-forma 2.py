precio_menos_cinco = 800  # Precio de la llanta si se compran menos de 5
precio_cinco_mas = 650  # Precio de la llanta si se compran 5 o más

continuar_comprando = True  #para controlar el bucle

while continuar_comprando:
    cantidad = int(input("Ingrese la cantidad de llantas a comprar: "))
    
    if cantidad < 5:
        total_pagar = cantidad * precio_menos_cinco
    else:
        total_pagar = cantidad * precio_cinco_mas
    
    print("El total a pagar es:", total_pagar)
    
    opcion = input("¿Desea continuar comprando? (s/n): ")
    
    if opcion.lower() != "s":
        continuar_comprando = False

print("Gracias por su compra. ¡Hasta luego!")