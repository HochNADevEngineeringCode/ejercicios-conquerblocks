# 1. IMPORTACIÓN DE LIBRERÍAS
import random  # esta libreria contiene elementos al azar.
import string  # esta libreria contiene listas de letras, números y símbolos.

def generar_password(longitud):
    # 2. DEFINICIÓN CARACTERES.
    # Unimos las letras mayúsculas/minúsculas, dígitos (0-9) y signos.
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # 3. GENRACION DE LA PASSWORD.
    # Elegimos un carácter al azar y los unimos en un texto.
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    return password

# 4. EJECUCION DEL PROMGRAMA.
if __name__ == "__main__":
    print("--- GENERADOR DE CONTRASEÑAS ---")
    try:
        # Pedimos el largo/longitud al usuario y lo convertimos a número entero.
        largo = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? (Ej. 12): "))
        
        if largo < 4:
            print("Por seguridad, elige al menos 4 caracteres.")
        else:
            nueva_clave = generar_password(largo)
            print(f"\nTu nueva contraseña segura es: {nueva_clave}")
            
    except ValueError:
        # Si el usuario escribe letras en vez de números, evita que el programa falle.
        print("Error: Por favor ingresa solo números enteros.")
