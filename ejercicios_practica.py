#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "pllugo@gmail.com"
__version__ = "1.1"

import csv
import os

import bonobo
import time
import requests

# Install bonobo
#   pip3 install -U bonobo 
# Crear archivo "dot"
#   bonobo inspect --graph ejercicios_clase.py > ejercicios_clase.dot
# Graphviz online
#   http://dreampuf.github.io/GraphvizOnline/
# Graphviz (dot) extension
#    Abrir el archivo .dot y presionar CTRL + SHIF + V

archivo = 'archivo.csv'


def extract():
    # Realice un bucle que recorra una lista del 0 al 10 inclusive
    # En cada iteración de ese bucle realizar un "yield" del valor
    # tomado de la lista
    lista = list(range(0,11))
    for i in range(len(lista)):
        numero = lista[i]
        print(numero)
        yield numero


def transform(x):
    # Por cada número que ingrese a transform
    # multiplicarlo por 5
    print(x)
    yield 5*x


def load(result):
    # Cada resultado que ingrese a este punto
    # ingresarlo como una nueva linea a un archivo
    # de texto (usando open con 'a' y write)
    # o insertando a una base de datos a elección.
    # El objetivo es que quede almacenado en un archivo
    # o una base de datos la tabla del 5
    with open(archivo, 'a', newline='') as fo:
            fo.write(str(result))
            fo.write("\n")



def get_graph(**options):
    if os.path.isfile(archivo) is True:
        os.remove(archivo)
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)
    return graph


def get_services(**options):
    return {}


if __name__ == "__main__":
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
