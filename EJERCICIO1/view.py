import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


from abstract_factory import *
from model import *

import os
import subprocess

class EmergenciasVista:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("Mi Aplicación Tkinter")
        self.root.geometry("600x100")  # Ancho x Alto

        # Etiqueta de título
        title_label = Label(self.root, text="Análisis de Datos de Emergencias", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Marco para botones
        button_frame = Frame(self.root)
        button_frame.pack(pady=10)
        
        

        # Botón de Representación de Texto
        text_button = tk.Button(button_frame, text="Representación Texto", command=self.texto, width=20)
        text_button.pack(side="left", padx=10)

        # Botón de Representación Gráfica
        graph_button = tk.Button(button_frame, text="Representación Gráfica", command=self.grafica, width=20)
        graph_button.pack(side="left", padx=10)

    def texto(self):
        client = Client(ConcreteFactoryTexto())

        client.view_histograma("Distrito", self.model.data)
        client.view_sectores("Mes", self.model.data)
        client.view_de_barras("Distrito", self.model.data)

    def grafica(self):
        client = Client(ConcreteFactoryGrafica())
        
        client.view_histograma("Hora Intervención", self.model.data)

        client.view_sectores("Distrito", self.model.data)

        client.view_de_barras("Distrito", self.model.data)
    
   
    def actualizar(self, data):
        self.data = data
        self.root.mainloop()


