from __future__ import annotations
from abc import ABC, abstractmethod

# Definición de las clases abstractas
class AbstractFactory(ABC):
    @abstractmethod
    def view_histograma(self) :
        pass

    @abstractmethod
    def view_sectores(self)  :
        pass

    @abstractmethod
    def view_de_barras(self) :
        pass

# ------------------------------------------------------
# Definición de las fábricas concretas para diferentes materiales
class ConcreteFactoryTexto(AbstractFactory):
    def view_histograma(self) :
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

# ------------------------------------------------------
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
    def view_histograma(self):
        print("HistogramaTexto")

class SectoresTexto(AbstractProductSectores):
    def view_sectores(self):
        print("SectoresTexto")

class DeBarrasTexto(AbstractProductDeBarras):
    def view_de_barras(self):
        print("DeBarrasTexto")

# ------------------------------------------------------
# Definición de las clases de productos de GRAFICA
class HistogramaGrafica(AbstractProductHistograma):
    def view_histograma(self):
        print("HistogramaGrafica")

class SectoresGrafica(AbstractProductSectores):
    def view_sectores(self):
        print("SectoresGrafica")

class DeBarrasGrafica(AbstractProductDeBarras):
    def view_de_barras(self):
        print("DeBarrasGrafica")

# ------------------------------------------------------

def client_code(factory: AbstractFactory) -> None:

    product_a = factory.view_histograma()
    product_b = factory.view_sectores()
    product_c = factory.view_de_barras()

    product_a.view_histograma()
    product_b.view_sectores()
    product_c.view_de_barras()

# ------------------------------------------------------

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactoryTexto())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactoryGrafica())
    