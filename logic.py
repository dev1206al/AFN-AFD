# logic.py
def clausura_epsilon(estados, transiciones):
    """
    Calcula la clausura-epsilon de un conjunto de estados.
    La clausura-epsilon incluye todos los estados alcanzables desde un conjunto dado
    mediante transiciones epsilon ((''), es decir, transiciones sin consumir un símbolo de entrada).
    """

    clausura = set(estados)  # Inicializamos la clausura con los estados dados
    pila = list(estados)   # Pila para explorar los estados alcanzables

    # Mientras haya estados en la pila
    while pila:
        estado_actual = pila.pop()  # Sacamos el estado actual
        # Si hay transiciones epsilon desde el estado actual
        if (estado_actual, '') in transiciones:
            for siguiente_estado in transiciones[(estado_actual, '')]:
                # Si el siguiente estado aún no está en la clausura
                if siguiente_estado not in clausura:
                    clausura.add(siguiente_estado)  # Añadimos a la clausura
                    pila.append(siguiente_estado)  # Añadimos a la pila para continuar explorando

    return clausura


def construccion_subconjuntos(estados, alfabeto, transiciones, estado_inicial, estados_finales):
    """
    Implementa el algoritmo de la teoría del subconjunto para convertir un AFND en un AFD.
    Este algoritmo utiliza la clausura-epsilon para manejar las transiciones epsilon.

    Parámetros:
    - estados: Conjunto de estados del AFND.
    - alfabeto: Alfabeto del AFND (conjunto de símbolos de entrada).
    - transiciones: Diccionario de transiciones del AFND.
    - estado_inicial: Estado inicial del AFND.
    - estados_finales: Conjunto de estados finales del AFND.

    Retorna:
    - Un diccionario que representa el AFD resultante con las claves:
        - "estados": Conjunto de estados del AFD.
        - "transiciones": Diccionario de transiciones del AFD.
        - "estado_inicial": Estado inicial del AFD.
        - "estados_finales": Conjunto de estados finales del AFD.
    """
    estados_afd = []  # Lista para almacenar los estados del AFD
    transiciones_afd = {}  # Diccionario para las transiciones del AFD

    # Calcular la clausura-epsilon del estado inicial del AFND
    estado_inicial_afd = frozenset(clausura_epsilon({estado_inicial}, transiciones))
    estados_afd.append(estado_inicial_afd)  # Añadir el estado inicial del AFD
    estados_finales_afd = set()  # Conjunto para los estados finales del AFD

    # Cola para procesar nuevos estados generados
    estados_no_procesados = [estado_inicial_afd]
    
    # Mientras haya estados no procesados
    while estados_no_procesados:
        estado_actual = estados_no_procesados.pop(0)  # Tomamos el siguiente estado de la cola

        # Para cada símbolo en el alfabeto
        for simbolo in alfabeto:
            estados_alcanzables = set()  # Conjunto de estados alcanzables con el símbolo actual

            # Para cada estado en el conjunto actual
            for estado in estado_actual:
                # Si hay transiciones definidas para el símbolo actual
                if (estado, simbolo) in transiciones:
                    estados_alcanzables.update(transiciones[(estado, simbolo)])  # Añadir estados alcanzables
            
            # Calcular la clausura-epsilon de los estados alcanzables
            siguiente_estado = frozenset(clausura_epsilon(estados_alcanzables, transiciones))
            
            # Si el estado resultante no está ya en los estados del AFD, lo añadimos
            if siguiente_estado not in estados_afd and siguiente_estado:
                estados_afd.append(siguiente_estado)  # Añadir a la lista de estados del AFD
                estados_no_procesados.append(siguiente_estado)  # Añadir a la cola de procesamiento
            
            # Añadir la transición al diccionario del AFD
            if estado_actual not in transiciones_afd:
                transiciones_afd[estado_actual] = {}
            transiciones_afd[estado_actual][simbolo] = siguiente_estado  # Transición actual

    # Identificar los estados finales del AFD
    for estado in estados_afd:
        if estado & estados_finales:  # Si el conjunto de estados incluye algún estado final del AFND
            estados_finales_afd.add(estado)

    # Retornar la definición del AFD
    return {
        "estados": estados_afd,            # Conjunto de estados del AFD
        "transiciones": transiciones_afd,  # Transiciones del AFD
        "estado_inicial": estado_inicial_afd,  # Estado inicial del AFD
        "estados_finales": estados_finales_afd    # Estados finales del AFD
    }
