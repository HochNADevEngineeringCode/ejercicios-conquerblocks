# IPORTAMOS LIBRERIAS.
import tkinter as tk
from tkinter import messagebox

# 1. FUNCIONES DE GESTIÓN DE LAS TAREAS.
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea.strip() != "":  # Verificamos que no esté vacio.
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpiamos el cuadro de texto.
    else:
        messagebox.showwarning("Aviso", "Escribe una tarea antes de agregar.")

def eliminar_tarea():
    try:
        # Obtenemos el índice de la tarea seleccionada por el usuario.
        indice_seleccionado = lista_tareas.curselection()[0]
        lista_tareas.delete(indice_seleccionado)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea de la lista para eliminar.")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        texto_actual = lista_tareas.get(indice)
        # Evitamos marcarla dos veces.
        if not texto_actual.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, f"✔ {texto_actual}")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla.")

# 2. CONFIGURACIÓN DE LA VENTANA.
ventana = tk.Tk()
ventana.title("Mis Tareas")
ventana.geometry("350x420")

# 3. ELEMENTOS SUPERIORES (Entrada y Botónes).
entrada_tarea = tk.Entry(ventana, font=("Arial", 12), width=25)
entrada_tarea.pack(pady=10)

btn_agregar = tk.Button(ventana, text="Agregar Tarea", font=("Arial", 11), bg="#4CAF50", fg="white", command=agregar_tarea)
btn_agregar.pack(pady=5)

# 4. LISTA VISUAL DE TAREAS.
lista_tareas = tk.Listbox(ventana, font=("Arial", 12), width=32, height=12, selectbackground="#a6a6a6")
lista_tareas.pack(pady=10, padx=15)

# 5. BOTONES INFERIORES DE ACCIÓN.
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

btn_completar = tk.Button(marco_botones, text="Marcar Lista", font=("Arial", 10), command=marcar_completada)
btn_completar.pack(side=tk.LEFT, padx=5)

btn_eliminar = tk.Button(marco_botones, text="Eliminar", font=("Arial", 10), bg="#f44336", fg="white", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)

# 6. EJECUTAR APP.
ventana.mainloop()
