# vamos a representar los datos de la tabla de la base de datos
# en un diagrama de barras, en un diagrama de sectores, histograma  diagrama de cajas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

URL= "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"
data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')


class DiagramasGraficos:
    def __init__(self,data):
        self.data = data

    def diagrama_barras(self,variable):
        plt.figure(figsize=(10, 6))
        data[variable].value_counts().plot(kind='bar')
        plt.title(f'Diagrama de Barras para la variable "{variable}"')
        plt.xlabel(variable)
        plt.ylabel('Frecuencia')
        plt.show()

    def diagrama_sectores(self, variable):
        # Diagrama de sectores
        plt.figure(figsize=(6, 6))
        data[variable].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(f'Diagrama de Sectores para la variable "{variable}"')
        plt.show()

    def histograma(self, variable):
        # Histograma
        plt.figure(figsize=(10, 6))
        plt.hist(data[variable], bins=20, edgecolor='k')
        plt.title(f'Histograma para la variable "{variable}"')
        plt.xlabel(variable)
        plt.ylabel('Frecuencia')
        plt.show()





if __name__ == '__main__':
    diagramas = DiagramasGraficos(data)
    diagramas.diagrama_barras('Mes')
    diagramas.diagrama_sectores('Hospital')
    diagramas.histograma('Distrito')

