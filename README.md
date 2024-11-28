# Conversión de AFND a AFD utilizando la Teoría de Subconjuntos

Este proyecto implementa un programa para convertir un Autómata Finito No Determinista (AFND) en un Autómata Finito Determinista (AFD) utilizando el algoritmo de la **teoría de subconjuntos**. Además, muestra los resultados en forma de matriz, indicando transiciones hacia estados sumideros cuando es necesario.

## Contenido del Proyecto

El proyecto incluye dos archivos principales:

### 1. `logic.py`
Contiene las funciones principales para la conversión y manipulación de autómatas:
- **`clausura_epsilon(estados, transiciones)`**:
  Calcula la clausura-epsilon de un conjunto de estados, considerando transiciones epsilon (transiciones sin consumir un símbolo).
- **`construccion_subconjuntos(estados, alfabeto, transiciones, estado_inicial, estados_finales)`**:
  Convierte un AFND en un AFD utilizando el algoritmo de la teoría de subconjuntos.

### 2. `main.py`
Configura varios ejemplos de AFND, define sus transiciones, estados iniciales y finales, y utiliza `construccion_subconjuntos` para convertirlos en AFD. Finalmente, muestra los resultados en una tabla con transiciones claramente definidas.

## Ejemplos Incluidos

### Ejemplo 1: Lenguaje Simple
#### Descripción:
Reconoce cadenas sobre el alfabeto `{a, b}` que contienen la subcadena `ab`.
#### Lenguaje Formal:
```math
L = (a|b)*ab(a|b)*
# AFN-AFD
