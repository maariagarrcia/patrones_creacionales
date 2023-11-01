import pandas as pd
import numpy as np

import re

from colorama import Fore


from abstract_factory import *
from model import *




# Ejemplo de uso:
csv_url = "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"

data_cleaned = EmergenciasModel(csv_url)
data_cleaned.show()




