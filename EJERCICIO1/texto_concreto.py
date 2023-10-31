import plotext as plt
import pandas as pd

import pandas as pd
import termcharts 
from rich import print
from rich.layout import Layout
from rich.panel import Panel


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def create_bar_chart(self, variable):
        totals = self.data[variable].value_counts()
        plt.bar(totals.index, totals, width=0.5)
        plt.title("Diagrama de Barras")
        plt.xlabel(variable)
        plt.ylabel("TOTAL")

        # Ajustar el tamaño de fuente para los nombres de las variables (más pequeño)
        plt.font_size = (10, 10)  # Puedes ajustar el tamaño de fuente según tus preferencias

        plt.show()

    def create_histogram(self, variable):
        # Asignar un número único a cada categoría categórica
        categories = self.data[variable].unique()
        category_mapping = {category: i for i, category in enumerate(categories)}
        data_as_numbers = self.data[variable].map(category_mapping)

        # Crear un histograma con los números asignados
        plt.hist(data_as_numbers, bins=len(categories))
        plt.xticks(list(category_mapping.values()), list(category_mapping.keys()))
        plt.title(f"Histograma para {variable}")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.show()

    def create_grafico_de_sectores(self, variable):
        frecuencias = self.data[variable].value_counts()
        total = len(self.data)
        porcentajes = (frecuencias / total) * 100

        data_dict = dict(porcentajes)  # Convertir porcentajes a un diccionario

        chart_donut = termcharts.doughnut(data_dict, title=f"Diagrama de Sectores para la variable '{variable}'", rich=True)
        print(Panel(chart_donut, title="Diagrama de Sectores"))
        

        
   