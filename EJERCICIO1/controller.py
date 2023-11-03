from abstract_factory import *
from model import *
from view import *


## controlador

# Ejemplo de uso:
csv_url = "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"

class EmergenciasController:
    def __init__(self) -> None:
        self.model = EmergenciasModel(csv_url)
        self.view = EmergenciasVista(tk.Tk(),self.model)

    def run(self):
        self.model.controller()
        self.view.actualizar(self.model)

  
if __name__ == "__main__":
    controller = EmergenciasController()
    controller.run()

