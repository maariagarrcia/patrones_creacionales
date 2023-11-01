import tkinter as tk
from tkinter import messagebox

from abstract_factory import *

from controller import *

class MiAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Aplicación Tkinter")
        
        self.root.geometry("400x100")  # Ancho x Alto

        self.boton_texto = tk.Button(self.root, text="Representación Texto", command=self.texto)
        self.boton_texto.pack()

        self.boton_grafico = tk.Button(self.root, text="Representación gráfica", command=self.grafica)
        self.boton_grafico.pack()


    def texto(self):
        client = Client(ConcreteFactoryTexto())
        client.view_histograma("Distrito",data_cleaned.data)
        client.view_sectores("Mes",data_cleaned.data)
        client.view_de_barras("Distrito",data_cleaned.data)

    def grafica(self):
        client = Client(ConcreteFactoryGrafica())
        client.view_histograma("Hora Intervención",data_cleaned.data)
        client.view_sectores("Distrito",data_cleaned.data)
        client.view_de_barras("Distrito",data_cleaned.data)



if __name__ == "__main__":
    root = tk.Tk()
    app = MiAplicacion(root)
    root.mainloop()
