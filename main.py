# Importamos la función construccion_subconjuntos desde el archivo logic.py.
# Esta función se encarga de convertir un AFND en un AFD.
from logic import construccion_subconjuntos

# =========================
# EJEMPLO 1: LENGUAJE SIMPLE CON 'a' Y 'b' 
# L=(a|b)*ab(a|b)*
# 
# =========================

# Función que define las transiciones del AFND para el ejemplo 1.
def transiciones_ejemplo1():
    return {
        ('q0', 'a'): {'q0', 'q1'},  # Desde el estado q0, con 'a', puede quedarse en q0 o ir a q1.
        ('q0', 'b'): {'q0'},        # Desde q0, con 'b', permanece en q0.
        ('q1', 'b'): {'q2'},        # Desde q1, con 'b', transita a q2.
        ('q2', 'a'): {'q3'},        # Desde q2, con 'a', transita a q3.
        ('q2', 'b'): {'q3'},        # Desde q2, con 'b', transita a q3.
        ('q3', 'a'): {'q3'},        # Desde q3, con 'a', permanece en q3.
        ('q3', 'b'): {'q3'},        # Desde q3, con 'b', permanece en q3.
    }

# Definimos los elementos del AFND para el ejemplo 1
estados1 = {'q0', 'q1', 'q2', 'q3'}        # Conjunto de estados
alfabeto1 = {'a', 'b'}                     # Alfabeto: los símbolos que procesa
transiciones1 = transiciones_ejemplo1()    # Transiciones definidas con la función anterior
estado_inicial1 = 'q0'                     # Estado inicial
estados_finales1 = {'q3'}                  # Conjunto de estados finales

# Convertimos el AFND del ejemplo 1 en un AFD
afd_resultado1 = construccion_subconjuntos(estados1, alfabeto1, transiciones1, estado_inicial1, estados_finales1)

# =========================
# EJEMPLO 2: LENGUAJE QUE CONTIENE LA SUBCADENA "011"
# L = (0|1)*011(0|1)*
# =========================

# Función que define las transiciones del AFND para el ejemplo 2.
def transiciones_ejemplo2():
    return {
        ('q0', '0'): {'q0', 'q1'},  # Desde q0, con '0', puede quedarse en q0 o ir a q1.
        ('q0', '1'): {'q0'},        # Desde q0, con '1', permanece en q0.
        ('q1', '1'): {'q2'},        # Desde q1, con '1', transita a q2.
        ('q2', '1'): {'q3'},        # Desde q2, con '1', transita a q3.
        ('q3', '0'): {'q3'},        # Desde q3, con '0', permanece en q3.
        ('q3', '1'): {'q3'},        # Desde q3, con '1', permanece en q3.
    }

# Definimos los elementos del AFND para el ejemplo 2
estados2 = {'q0', 'q1', 'q2', 'q3'}        # Conjunto de estados
alfabeto2 = {'0', '1'}                     # Alfabeto: los símbolos que procesa
transiciones2 = transiciones_ejemplo2()    # Transiciones definidas con la función anterior
estado_inicial2 = 'q0'                     # Estado inicial
estados_finales2 = {'q3'}                  # Conjunto de estados finales

# Convertimos el AFND del ejemplo 2 en un AFD
afd_resultado2 = construccion_subconjuntos(estados2, alfabeto2, transiciones2, estado_inicial2, estados_finales2)

# =========================
# EJEMPLO 3: LENGUAJE COMPLEJO
# =========================

# Función que define las transiciones del AFND para el ejemplo 3.
def transiciones_ejemplo3():
    return {
        ('q0', 'a'): {'q1'},        # Desde q0, con 'a', transita a q1.
        ('q1', 'b'): {'q2', 'q3'},  # Desde q1, con 'b', transita a q2 o q3.
        ('q1', 'a'): {'q1'},        # Desde q1, con 'a', permanece en q1.
        ('q2', 'a'): {'q1'},        # Desde q2, con 'a', transita a q1.
        ('q3', 'a'): {'q2'},        # Desde q3, con 'a', transita a q2.
    }

# Definimos los elementos del AFND para el ejemplo 3
estados3 = {'q0', 'q1', 'q2', 'q3'}        # Conjunto de estados
alfabeto3 = {'a', 'b'}                     # Alfabeto: los símbolos que procesa
transiciones3 = transiciones_ejemplo3()    # Transiciones definidas con la función anterior
estado_inicial3 = 'q0'                     # Estado inicial
estados_finales3 = {'q1'}                  # Conjunto de estados finales

# Convertimos el AFND del ejemplo 3 en un AFD
afd_resultado3 = construccion_subconjuntos(estados3, alfabeto3, transiciones3, estado_inicial3, estados_finales3)

# =========================
# FUNCIÓN PARA MOSTRAR EL AFD EN FORMA DE MATRIZ
# =========================

def mostrar_afd_como_matriz_con_sumidero(afd_resultado, alfabeto, titulo):
    """
    Muestra el AFD en forma de matriz con columnas alineadas.
    Identifica y muestra "sumidero" para transiciones que conducen a estados que no están definidos en el AFD.
    """
    print(f"\n============= {titulo} ================")

    # Ordenar el alfabeto alfabéticamente
    alfabeto_ordenado = sorted(list(alfabeto))

    # Crear encabezado con los nombres de las columnas: "Estado" + los símbolos del alfabeto
    encabezado = ["Estado"] + alfabeto_ordenado
    ancho_columna = 20  # Ancho fijo para cada columna
    fila_encabezado = "".join(celda.ljust(ancho_columna) for celda in encabezado)
    print(fila_encabezado)
    print("-" * len(fila_encabezado))  # Línea separadora

    # Procesar cada estado del AFD para generar sus transiciones
    for estado in afd_resultado['estados']:
        fila = [",".join(estado).ljust(ancho_columna)]  # Nombre del estado
        for simbolo in alfabeto_ordenado:
            siguiente_estado = afd_resultado['transiciones'].get(estado, {}).get(simbolo, frozenset())
            if not siguiente_estado or siguiente_estado not in afd_resultado['estados']:  # Verificar si es un sumidero
                fila.append("sumidero".ljust(ancho_columna))
            else:
                fila.append(",".join(siguiente_estado).ljust(ancho_columna))
        print("".join(fila))
    
    # Mostrar el estado inicial y los estados finales del AFD
    print(f"\nEstado inicial: {','.join(afd_resultado['estado_inicial'])}")
    print(f"Estados finales: {[','.join(s) for s in afd_resultado['estados_finales']]}\n")

# =========================
# MOSTRAR LOS RESULTADOS DE LOS EJEMPLOS
# =========================

mostrar_afd_como_matriz_con_sumidero(afd_resultado1, alfabeto1, "AFD Resultante para Ejemplo 1")
mostrar_afd_como_matriz_con_sumidero(afd_resultado2, alfabeto2, "AFD Resultante para Ejemplo 2")
mostrar_afd_como_matriz_con_sumidero(afd_resultado3, alfabeto3, "AFD Resultante para Ejemplo 3")
