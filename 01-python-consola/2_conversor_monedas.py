# 1. TASAS DE CAMBIO FIJAS (es de ejemplo, pudes cambiarlas segun tu tasa de cambio actual).
TASA_DOLAR = 1000.0
TASA_EURO = 1100.0

# 2. FUNCIONES DE CONVERSIÓN.
def pesos_a_dolares(pesos):
    return pesos / TASA_DOLAR

def pesos_a_euros(pesos):
    return pesos / TASA_EURO

# 3. MENÚ INTERACTIVO EN BUCLE.
while True:
    print("\n--- CONVERSOR DE MONEDAS ---")
    print("1. Pesos a Dólares")
    print("2. Pesos a Euros")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    # Salida del program
    if opcion == "3":
        print("¡Hasta luego!")
        break
        
    # Entrada y validación de opciones.
    if opcion in ["1", "2"]:
        try:
            monto = float(input("Ingresa la cantidad en pesos: "))
            if opcion == "1":
                resultado = pesos_a_dolares(monto)
                print(f"${monto} pesos equivalen a ${resultado:.2f} USD")
            elif opcion == "2":
                resultado = pesos_a_euros(monto)
                print(f"${monto} pesos equivalen a €{resultado:.2f} EUR")
        except ValueError:
            print("Error: Ingresa un monto numérico válido.")
    else:
        print("Opción no válida. Intenta de nuevo.")
