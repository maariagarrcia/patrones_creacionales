# Análisis de datos de las activaciones del SAMUR-Protección Civil en Madrid
# La activación se define como encargos de asistencia sanitaria 
# que supone la activación de un recurso sanitario u otro tipo de vehículo.


# PATRÓN ABSTRACT FACTORY PARA EL ANÁLISIS DE DATOS
# ----------------------------------------------------
# - El patrón "Abstract Factory" permite dividir el proceso 
# de análisis de datos en módulos independientes
# - Cada fábrica y producto concreto se encarga de una tarea específica
# - Facilita la incorporación de nuevos tipos de análisis en el futuro.

# LEEREMOS EL CSV ATRAVES DE ESTE LINK:https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv

import csv
import pandas as pd

URL= "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"

data = pd.read_csv(URL, sep=';', encoding='ISO-8859-1')

print(data.head(10))  # Mostrar las primeras filas para visualizar los datos

