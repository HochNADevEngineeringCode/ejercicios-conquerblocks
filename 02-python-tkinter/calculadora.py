# INPORTAMOS LIBRERIAS.
import tkinter as tk

# 1. FUNCIONES LÓGICAS DE LA CALCULADORA.
def presionar_tecla(valor):
    # Agrega el número o símbolo presionado al final de la pantalla.
    entrada_texto.insert(tk.END, valor)

def limpiar_pantalla():
    # Borra todo el contenido desde el carácter 0 hasta el final.
    entrada_texto.delete(0, tk.END)

def calcular_resultado():
    try:
        # eval() toma el texto matemático y lo resuelve.
        expresion = entrada_texto.get()
        resultado = eval(expresion)
        limpiar_pantalla()
        entrada_texto.insert(0, str(resultado))
    except Exception:
        limpiar_pantalla()
        entrada_texto.insert(0, "Error")

# 2. CONFIGURACIÓN DE LA VENTANA PRINCIPAL.
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x380")
ventana.resizable(False, False)

# 3. PANTALLA DE VISUALIZACIÓN.
entrada_texto = tk.Entry(ventana, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

# 4. CREACIÓN DE BOTONES.
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    if texto == '=':
        comando = calcular_resultado
    elif texto == 'C':
        comando = limpiar_pantalla
    else:
        # capturamos el valor exacto de 'texto' en cada vuelta del bucle.
        comando = lambda t=texto: presionar_tecla(t)
        
    btn = tk.Button(ventana, text=texto, font=("Arial", 16), command=comando)
    btn.grid(row=fila, column=columna, sticky="nsew", padx=3, pady=3)

# 5. AJUSTES DE FILAS Y COLUMNAS.
for i in range(5):
    ventana.rowconfigure(i, weight=1)
for i in range(4):
    ventana.columnconfigure(i, weight=1)

# 6. INICIAR LA APP CALCULADORA.
ventana.mainloop()
