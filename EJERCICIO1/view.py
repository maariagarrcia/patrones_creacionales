import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


from abstract_factory import *
from model import *



class EmergenciasVista:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("Mi Aplicación Tkinter")
        self.root.geometry("600x300")  # Ancho x Alto


        # Etiqueta de título
        title_label = Label(self.root, text="ANÁLISIS DE ACTIVACIONES DEL SAMUR 2023", font=("Helvetica", 20, "bold","underline"),fg="lightblue")
        title_label.pack(pady=10)


        # Marco para botones
        button_frame = Frame(self.root)
        button_frame.pack(pady=5)
        
        text_button = tk.Button(button_frame, text="Exploración de Datos", command=self.exploracion_datos, width=30)
        text_button.pack(side="top", padx=15)

        # Botón de Representación de Texto
        text_button = tk.Button(button_frame, text="Representación Texto", command=self.texto, width=30)
        text_button.pack(side="top", padx=15)

        # Botón de Representación Gráfica
        graph_button = tk.Button(button_frame, text="Representación Gráfica", command=self.grafica, width=30)
        graph_button.pack(side="top", padx=15)

        text_button = tk.Button(button_frame, text="Conclusiones", command=self.conclusiones, width=30)
        text_button.pack(side="top", padx=15)
        
        # Marco para el resumen con borde
        text_frame = tk.Frame(self.root, relief="groove", borderwidth=2, bg="lightblue")
        text_frame.pack(pady=15)


        texto = "Se han analizado los datos de emergencias de Madrid de 2023 para ello," "\n" "se ha creado un abstract factory para poder representar""\n"" los datos tipo  texto o tipo gráfica."
        # Etiqueta de texto en la ventana principal
        self.text_label = tk.Label(text_frame, text=texto, font=("Helvetica", 16, "bold"), bg="lightblue")
        self.text_label.pack(pady=15)



    def exploracion_datos(self):
        messagebox.showinfo("Exploración de Datos", self.model.exploracion_datos())
        self.model.show()

    def texto(self):
        client = Client(ConcreteFactoryTexto())

        client.view_histograma("Hora Intervención Media", self.model.data)

        client.view_sectores("Mes", self.model.data)

        client.view_de_barras("Hospital", self.model.data)
        
        messagebox.showinfo("Los gráficos tipo texto se muestran en la consola")


    def grafica(self):
        client = Client(ConcreteFactoryGrafica())
        
        client.view_histograma("Hora Intervención Media", self.model.data)

        client.view_sectores("Mes", self.model.data)

        client.view_de_barras("Hospital", self.model.data)
    
    def conclusiones(self):
        text_window = tk.Toplevel(self.root)
        text_window.title("Texto de Inicio")
        texto="Como podemos observar en los gráficos, la hora de intervención ""\n" "media por distrito es más temprana en el distrito de Salamanca  ""\n" " y más tardía en el distrito de Villaverde.  ""\n" " En cuanto a los meses, el mes con más intervenciones   ""\n" "es el mes de julio/mayo  y el mes con menos intervenciones es el mes de febrero/agosto.""\n""Por último, el hospital con más intervenciones es el hospital de la Gregorio Marañón y 12 de Octubre y el hospital ""\n" " con menos intervenciones es el hospital de la Princesa."
        text_label = tk.Label(text_window, text=texto)
        text_label.pack(padx=20, pady=10)


    def actualizar(self, data):
        self.data = data
        self.root.mainloop()


