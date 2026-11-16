#INPORTAMOS LIBRERIAS.
import random

# 1. ESTABLESEMOS LA CONFIGURACION INICIAL.
numero_secreto = random.randint(1, 100)  # Número aleatorio entre 1 y 100
intentos_restantes = 5

print("--- ADIVINA EL NÚMERO (1 al 100) ---")
print(f"Tienes {intentos_restantes} intentos para lograrlo.")

# 2. BUCLE PRINCIPAL.
while intentos_restantes > 0:
    try:
        # Pedimos el número al usuario.
        intento = int(input("\nIngresa tu número: "))
        
        # 3. COMPROBACIÓN DEL RESULTADO.
        if intento == numero_secreto:
            print(f"¡FELICIDADES! Adivinaste el número {numero_secreto}.")
            break  # salimos del bucle si el usuario adivina corectamente.
        elif intento < numero_secreto:
            print("Pista: El número secreto es MÁS ALTO.")
        else:
            print("Pista: El número secreto es MÁS BAJO.")
            
        # Restamos un intento o vida al usuario.
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.")
        
    except ValueError:
        print("Por favor, escribe un número válido.")

# 4. MENSAJE DE DERROTA SI SE ACABAN LOS INTENTOS.
if intentos_restantes == 0:
    print(f"\n¡Perdiste! El número secreto era {numero_secreto}.")
