#Archivo principal de la aplicación
#Juego de aventura: Haunted Mansion
#Version: 1.0

#Se agrega soporte para pausas y limpieza de pantalla en la terminal
import time 
import os 

#Importacion de sprites (Por el momento no hay ninguno)
from sprites import *

#Esto para poder limpiar la terminal
def limpiar():
    print("\n" * 100)

#Inicio del juego 
(limpiar)
print("CARGANDO JUEGO...")
time.sleep(1)
(limpiar)

print("-------------------------------------")
print("  Bienvenido a Haunted Mansion V1.0  ")
print("-------------------------------------")

#Se solicita nombre al jugador
nombre_jugador = input("Por favor, ingresa tu nombre: ")

(limpiar)

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
    print("--------------------------------------")
    print("Se escuchan ruidos extraños provenientes de la cocina.")
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
            
    elif direccion == "escaleras":
        #Si el usuario escoge las escaleras
        print("--------------------------------------")
        print("Subes las escaleras lentamente.")
        print("En el segundo piso, ves un pasillo con dos puertas, una roja y otra verde")
        print("De repente, escuchas pasos acercandose...")
        print("Tienes que decidir rapido!")

        #Tercera desicion (Dentro de las escaleras)
        accion_escaleras = input("Que puerta eliges? Roja / Verde:").lower()

        if accion_escaleras == "roja":
            #ESTADO MEDIO
            print("--------------------------------------")
            print("Abres la puerta roja y entras a una habitacion un poco iluminada.")
            print("Dentro ves un espejo antiguo y una ventana que da al exterior.")

        elif accion_escaleras == "verde":
            #ESTADO MEDIO (Dentro de la habitacion verde)
            print("--------------------------------------")
            print("Abres la puerta verde y entras a una habitacion oscura.")
            print("De repente, se iluminan las luces del baño")

        else: 
            #Por el momento no pasa nada si no se escoge ninguna puerta
            print("Te quedaste en el pasillo sin hacer nada y te desmayaste...")