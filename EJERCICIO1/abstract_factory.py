from __future__ import annotations
from abc import ABC, abstractmethod

import plotext as plt
import matplotlib.pyplot as mathplot

import pandas as pd
import numpy as np

import termcharts
from rich import print
from rich.layout import Layout
from rich.panel import Panel


# Definición de las clases abstractas
class AbstractFactory(ABC):
    @abstractmethod
    def view_histograma(self):
        pass

    @abstractmethod
    def view_sectores(self):
        pass

    @abstractmethod
    def view_de_barras(self):
        pass

# ------------------------------------------------------
# Definición de las fábricas concretas para diferentes materiales


class ConcreteFactoryTexto(AbstractFactory):
    def view_histograma(self):
        return HistogramaTexto()

    def view_sectores(self):
        return SectoresTexto()

    def view_de_barras(self):
        return DeBarrasTexto()


class ConcreteFactoryGrafica(AbstractFactory):
    def view_histograma(self):
        return HistogramaGrafica()

    def view_sectores(self):
        return SectoresGrafica()

    def view_de_barras(self):
        return DeBarrasGrafica()

#  ------------------------------------------------------
# Definición de la clase abstracta de productos


class AbstractProductHistograma(ABC):
    @abstractmethod
    def view_histograma(self):
        pass


class AbstractProductSectores(ABC):
    @abstractmethod
    def view_sectores(self):
        pass


class AbstractProductDeBarras(ABC):
    @abstractmethod
    def view_de_barras(self):
        pass

# ------------------------------------------------------
# Definición de las clases de productos de TEXTO


class HistogramaTexto(AbstractProductHistograma):
    def view_histograma(self, variable, data):
        # Asignar un número único a cada categoría categórica
        categories = data[variable].unique()
        category_mapping = {category: i for i,
                            category in enumerate(categories)}
        data_as_numbers = data[variable].map(category_mapping)

        # Crear un histograma con los números asignados
        plt.hist(data_as_numbers, bins=len(categories))
        plt.xticks(list(category_mapping.values()),
                   list(category_mapping.keys()))
        plt.title(f"Histograma para {variable}")
        plt.xlabel(variable)
        plt.ylabel("Frecuencia")
        plt.show()


class DeBarrasTexto(AbstractProductDeBarras):
    def view_de_barras(self, variable, data):
        plt.clear_figure()
        totals = data[variable].value_counts()
        plt.bar(totals.index, totals.values, width=0.3)
        plt.title("Diagrama de Barras")
        plt.xlabel(variable)
        plt.ylabel("TOTAL")
        # Ajustar el tamaño de fuente para los nombres de las variables (más pequeño)
        # plt.font_size = (10, 10)  # Puedes ajustar el tamaño de fuente según tus preferencias
        plt.show()


class SectoresTexto(AbstractProductSectores):
    def view_sectores(self, variable, data):
        frecuencias = data[variable].value_counts()
        total = len(data)
        porcentajes = (frecuencias / total) * 100

        data_dict = dict(porcentajes)  # Convertir porcentajes a un diccionario

        chart_donut = termcharts.doughnut(
            data_dict, title=f"Diagrama de Sectores para la variable '{variable}'", rich=True)
        print(Panel(chart_donut, title="Diagrama de Sectores"))


# ------------------------------------------------------
# Definición de las clases de productos de GRAFICA
class HistogramaGrafica(AbstractProductHistograma):
    def view_histograma(self, variable, data):
        # Histograma
        mathplot.figure(figsize=(10, 6))
        mathplot.hist(data[variable], bins=60, edgecolor='k')
        mathplot.title(f'Histograma para la variable "{variable}"')
        mathplot.xlabel(variable)
        mathplot.ylabel('Frecuencia')
        mathplot.show()


class SectoresGrafica(AbstractProductSectores):
    def view_sectores(self, variable, data):
       # Diagrama de sectores
        mathplot.figure(figsize=(6, 6))
        data[variable].value_counts().plot(kind='pie', autopct='%1.1f%%')
        mathplot.title(f'Diagrama de Sectores para la variable "{variable}"')
        mathplot.show()


class DeBarrasGrafica(AbstractProductDeBarras):
    def view_de_barras(self, variable, data):
        # Calcular el número de incidentes por hospital
        hospital_counts = data[variable].value_counts()

        # Crear el gráfico de barras
        fig, ax = mathplot.subplots(figsize=(10, 6))
        hospital_counts.plot(kind='bar', ax=ax)

        # Etiquetas y título
        ax.set_title(f'Diagrama de Barras para la variable "{variable}"')
        ax.set_xlabel(variable)
        ax.set_ylabel('Frecuencia')

        mathplot.show()


# ------------------------------------------------------
# Definición de la clase cliente
class Client:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def view_histograma(self, variable, data):
        product = self.factory.view_histograma()
        product.view_histograma(variable, data)

    def view_sectores(self, variable, data):
        product = self.factory.view_sectores()
        product.view_sectores(variable, data)

    def view_de_barras(self, variable, data):
        product = self.factory.view_de_barras()
        product.view_de_barras(variable, data)

# ------------------------------------------------------
