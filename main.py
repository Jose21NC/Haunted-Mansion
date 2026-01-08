#Archivo principal de la aplicación
#Juego de aventura: Haunted Mansion
#Version: 1.0

print("-------------------------------------")
print("  Bienvenido a Haunted Mansion V1.0  ")
print("-------------------------------------")

#Se solicita nombre al jugador
nombre_jugador = input("Por favor, ingresa tu nombre: ")

print("Hola " + nombre_jugador + ". Estas parado frente a una puerta gigante y vieja.")
print("Se escuchan ruidos extraños dentro...")

#Aqui empieza la primera desicion
#Uso .lower() para que si se usa "enter" funcione igual
desicion1 = input("Quieres entrar a la mansion? (si/no):").lower()

if desicion1 == "si":
    #Si el usuario dijo que si, entra a la mansion
    print("--------------------------------------")
    print("Abres la puerta lentamente y entras a la mansion...")
    print("De repente, la puerta se cierra detras de ti con un fuerte estruendo.")
    print("Te cientras en un pasillo oscuro. A la izquierda esta la COCINA")
    print("A la derecha hay unas ESCALERAS que suben.")

    #Segunda desicion
    direccion = input("A donde quieres ir? (Escribe 'COCINA' o 'ESCALERAS'):").lower()

    if direccion == "cocina":
        #Si el usuario escoge la cocina
        print("--------------------------------------")
        print("Entras a la cocina, huele a comida podrida.")
        print("Ves un refrigerador viejo y un armario de madera")

        #Tercera desicion (Dentro de la cocina)
        accion_cocina = input("¿Que abres? Refrigerador / Armario:").lower()

        if accion_cocina == "refrigerador":
            #FINAL MALO 1: MUERTE
            print("--------------------------------------")
            print("Oh no! Al abrir el refrigerador, un fantasma aparece y mueres de miedo!")
            print("FIN DEL JUEGO.")

        elif accion_cocina == "armario":
            #FINAL BUENO 1: ESCAPA
            print("--------------------------------------")
            print("Dentro del armario encuentras una salida al exterior!")
            print("Corres mientras los ruidos detras de ti se intensifican.")
            print("Felicidades " + nombre_jugador + ", Ganaste el juego!")

        else: 
            print("Te quedaste en la cocina sin hacer nada y los ruidos te alcanzaron...")
            print("FIN DEL JUEGO.")


            


