import tkinter as tk
import re
from math import sqrt

def es_numero_real(expresion):
    return bool(re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)$', expresion))

def tiene_radicales(expresion):
    return bool(re.search(r'√|sqrt', expresion))

def es_trinomio_de_la_forma(expresion):
    return bool(re.match(r'^[+-]?(\d+)?x\^2[+-]?(\d+)?x[+-]?\d*$', expresion))

def es_ecuacion_cuadratica(expresion):
    return bool(re.match(r'^[+-]?(\d+)?x\^2[+-]?(\d+)?x[+-]?\d* *= *0$', expresion))

def es_ecuacion_lineal(expresion):
    return bool(re.match(r'^[+-]?(\d+)?x[+-]?\d* *= *0$', expresion))

def analizar_expresion(expresion):
    expresion = expresion.replace(" ", "")
    
    if '=' in expresion:
        partes = expresion.split('=')
        if len(partes) != 2:
            return "Expresión inválida. Hay más de un signo '='."
        lhs, rhs = partes
    else:
        lhs = expresion

    terminos = re.findall(r'([+-]?\d*\.?\d*x?\^?\d*)', lhs)
    terminos = [t for t in terminos if t]  # Filtrar términos vacíos

    # Determinar el tipo de expresión
    if es_numero_real(lhs):
        return "Número real"
    elif tiene_radicales(lhs):
        return "Contiene radicales"
    elif es_trinomio_de_la_forma(lhs):
        return "Trinomio de la forma x^2 + bx + c"
    elif es_ecuacion_cuadratica(expresion):
        return "Ecuación cuadrática"
    elif es_ecuacion_lineal(expresion):
        return "Ecuación lineal"
    
    return "No se detectó ningún tipo específico."

#                                            --apartado gráfico---

#ventana principal
ventanap=tk.Tk()
ventanap.title("Identificador De Expresiones Algebraicas")
ventanap.geometry("800x600")
ventanap.config(bg="black")

#mensaje
mensaje=tk.Label(ventanap,text="Ingresa una expresion algebraica", bg="black", fg="white", font=("Arial", 12))
mensaje.pack(pady="10")

#entrada de datos
entrada=tk.Entry(ventanap, bg="gray", font=("Arial", 20))
entrada.pack(pady="99")

#funcion de leer y analizar para el boton
def leer_analizar():
    expresion=entrada.get()
    tipo=analizar_expresion(expresion)
    respuesta.config(text=f"la expresión es de titpo: {tipo}") #--"IMPRIME" la respuesta--
    
#boton para Analizar
boton=tk.Button(ventanap, text="Analizar", bg="gray", command=leer_analizar)
boton.pack(pady="10", side="top")

#funcion para el boton de limpiar todo
def clear():
    entrada.delete(0, tk.END)
    respuesta.config(text=" ")

#boton para limpiar todo
botonclr= tk.Button(ventanap, text="limpiar", command=clear)
botonclr.pack(padx="10", side="top")

#--"DEFINE" la el mensaje de respuesta--
respuesta=tk.Label(ventanap, bg="black", fg="white", font=("Arial", 15))
respuesta.pack(pady="12")

ventanap.mainloop()
# (i) ------Hace falta agregarle la resolucion del tipo de expresion------