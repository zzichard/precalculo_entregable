import tkinter as tk
import re
from math import sqrt
import math

def es_numero_real(expresion):
    return bool(re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)$', expresion))

def tiene_radicales(expresion):
    return bool(re.search(r'√|sqrt', expresion))

def es_trinomio_de_la_forma(expresion):
        if "=" in entrada.get():
            return False    
        else:
            return bool(re.match(r'^[+-]?(\d+)?x\^2([+-]\d*x)?([+-]\d+)?$', expresion))

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
        return "Número real. \n\nInformación: Este numero pertenece al conjunto de los numero reales."
    elif tiene_radicales(lhs):
        return "Radical. \n\nResolución: cuando una raiz es muy grande (cuantitativamente)\n es conveniente escribirla como factores."
    elif es_trinomio_de_la_forma(lhs):
        return """Trinomio de la forma x^2 + bx + c. \n\nFactorización:                                                                                                              
        escribimos dos binomios con la raiz cuadrada de X en el principio de ambos              
        En el primero el simbolo del primer termino del trinomio                                            
        En el segundo el signo como producto del signo del segundo por el tercer termino    
        1) Si los signos soniguales:                                                                                        
        buscamos que sumados den el segundo termino y multiplicados el tercer termino 
        2) Si los signos son distintos:                                                                                      
        buscamos que restados den el segundo termino y multiplicados el tercer termino 
        ( i ) si los binomios son iguales puedes escribirlos como uno sólo elevado al cuadrado    """
    elif es_ecuacion_cuadratica(expresion):
        return """Ecuación cuadrática.\n\nRsolución:                                          
        identificamos los teminos a b y c
        usa la formula cuadratica general"""
    elif es_ecuacion_lineal(expresion):
        return "Ecuación lineal"
    elif es_cuadrado_perfecto(expresion):
    return "No se detectó ningún tipo específico."

#                                            --apartado gráfico---

#ventana principal
ventanap=tk.Tk()
ventanap.title("Identificador De Expresiones Algebraicas")
ventanap.geometry("800x600")
ventanap.config(bg="#1e1f20")

#mensaje
mensaje=tk.Label(ventanap,text="Ingresa una expresion algebraica", bg="#1e1f20", fg="white", font=("Arial", 15))
mensaje.pack(pady="10")

#entrada de datos
entrada=tk.Entry(ventanap, bg="gray", font=("Arial", 20))
entrada.pack(pady="10")

#funcion de leer y analizar para el boton
def leer_analizar():
    expresion=entrada.get()
    tipo=analizar_expresion(expresion)
    respuesta.config(text=f"La expresión es de titpo: {tipo}", bg="black") #--"IMPRIME" la respuesta--
    
#boton para Analizar
boton=tk.Button(ventanap, text="Analizar", bg="#1c77d3", command=leer_analizar)
boton.pack(pady="10", side="top")

#funcion para el boton de limpiar todo
def clear():
    entrada.delete(0, tk.END)
    respuesta.config(text="", bg="#1e1f20")

#boton para limpiar todo
botonclr= tk.Button(ventanap, text="limpiar", bg="#d8453e", command=clear)
botonclr.pack(padx="10", side="top")

#--"DEFINE" la el mensaje de respuesta--
respuesta=tk.Label(ventanap, bg="#1e1f20", fg="#39ced0", font=("Arial", 15))
respuesta.pack(pady="12")

ventanap.mainloop()
# (i) ------Hace falta agregarle la resolucion del tipo de expresion------