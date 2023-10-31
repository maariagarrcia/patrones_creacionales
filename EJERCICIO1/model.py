import pandas as pd
import numpy as np

from colorama import Fore

# EmergenciasModel
class EmergenciasModel:
    def __init__(self, csv_url: str):
        self.data = pd.read_csv(csv_url, sep=';', encoding='ISO-8859-1') 

    def clean_data(self):
        # Realiza la limpieza de datos si es necesario
        # Puedes agregar aquí las transformaciones y limpiezas necesarias
        
        # Limpiar caracteres con acentos y letras "ñ" en los nombres de las columnas
        self.data.columns = [self.clean_text(column) for column in self.data.columns]
        
        # Limpiar caracteres con acentos y letras "ñ" en los datos
        for column in self.data.columns:
            if self.data[column].dtype == 'O':
                self.data[column] = self.data[column].apply(self.clean_text)

    def clean_text(self, text: str):
        # Función para limpiar caracteres con acentos y letras "ñ"
        if pd.notna(text):
            text = text.replace("Ã¡", "á").replace("Ã©", "é").replace("Ã­", "í").replace("Ã³", "ó").replace("Ãº", "ú")
            text = text.replace("Ã±", "ñ").replace("Ã¼", "ü").replace("Ã€", "À").replace("ÃŠ", "Ê").replace("ÃŠ", "Ê")
            # Agregar más reemplazos según tus necesidades
            text = text.replace("Ã€", "À").replace("Ã‰", "É").replace("ÃŒ", "Ì").replace("Ã’", "Ò").replace("Ãš", "Ù")
            text= text.replace("ï»¿"," ")
            return text
        return text
    
    def exploracion_datos(self):
        print()
        print(Fore.GREEN+"E X P L O R A C I O N    D E    L O S    D A T O S:"+Fore.WHITE)
        print(Fore.YELLOW+"1.  ver las primeras filas"+Fore.WHITE,self.data.head())
        print()
        print(Fore.YELLOW+"2.  ver las COLUMNAS"+Fore.WHITE,self.data.columns)
        print()
        print(Fore.YELLOW+"3.  ver los TIPOS DE DATOS"+Fore.WHITE,self.data.dtypes)
        print()
        print(Fore.YELLOW+"4.  ver los VALORES UNICOS"+Fore.WHITE,self.data.nunique())
        print()
        print(Fore.YELLOW+"5.  ver el SIZE"+Fore.WHITE,self.data.size)
        print()
        print(Fore.YELLOW+"6.  ver el SHAPE"+Fore.WHITE,self.data.shape)
        print()
        print(Fore.YELLOW+"7.  ver los VALORES FALTANTES"+Fore.WHITE,self.data.isnull().sum().sum()/self.data.size*100,"%")
        print()
        print(Fore.YELLOW+"8.  ver los VALORES FALTANTES"+Fore.WHITE,self.data.isnull().sum()/len(self.data)*100)
        print()
        print(Fore.YELLOW+"9.  ver los VALORES 0"+Fore.WHITE,self.data[self.data==0].count()/len(self.data)*100)
        print()
        print(Fore.YELLOW+"10.  ver los VALORES DUPLICADOS"+Fore.WHITE,self.data.duplicated().sum()/len(self.data)*100,"%")
        print()
        print(Fore.YELLOW+"11.  ver los VALORES CATEGORICOS"+Fore.WHITE,self.data.select_dtypes(include=['object']).columns)
        print()
        print(Fore.YELLOW+"12.  ver los VALORES NUMERICOS"+Fore.WHITE,self.data.select_dtypes(include=['int64','float64']).columns)
        print()
        print(Fore.YELLOW+"13.  ver la CARDINALIDAD DE LAS VARIABLES CATEGORICAS"+Fore.WHITE,self.data.select_dtypes(include=['object']).nunique())
        print()
        print(Fore.YELLOW +"14. ver resumen estadistico de vbles numericas "+Fore.WHITE,self.data.describe())
        print()

    def datos_categoricos(self):
        # Dividir en columnas categóricas y numéricas
        categorical_cols = []
        numerical_cols = []

        for col in self.data.columns:
            if self.data[col].dtype == 'object':
                categorical_cols.append(col)
            else:
                numerical_cols.append(col)

        # Realizar la codificación one-hot de las columnas categóricas
        self.data = pd.get_dummies(self.data, columns=categorical_cols, drop_first=True)
        return self.data

    def tiempo_a_segundos(self,tiempo_str):
        try:
            horas, minutos, segundos = map(int, tiempo_str.split(':'))
            segundos_totales = horas * 3600 + minutos * 60 + segundos
            return segundos_totales
        except:
            return np.nan  # En caso de errores, marcamos como NaN

    def datatime(self):
        self.data['Hora Intervención'] = self.data['Hora Intervención'].apply(self.tiempo_a_segundos)
        self.data['Hora Solicitud'] = self.data['Hora Solicitud'].apply(self.tiempo_a_segundos)
        
    def valores_faltantes(self):
        # todos loos huecos que esten vacio lso rellebamos por 0
        self.data = self.data.fillna(0) 

    def tiempo_transcurrido(self):
        # Calculamos el tiempo transcurrido entre la inervencion y la solicitud
        self.data['Tiempo transcurrido'] = self.data['Hora Intervención'] - self.data['Hora Solicitud']
        # volver a convertir a formato de tiempo
        self.data['Tiempo transcurrido'] = pd.to_timedelta(self.data['Tiempo transcurrido'], unit='s')

    def preprocesamiento(self):
        self.datatime()
        self.valores_faltantes()
        self.tiempo_transcurrido()
        self.datos_categoricos()  




# Ejemplo de uso:
csv_url = "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"

data_cleaned = EmergenciasModel(csv_url)


# Realizar la limpieza
data_cleaned.clean_data()

# Imprimir nombres de las columnas después de la limpieza
print(Fore.GREEN+"\nDATASET:"+Fore.WHITE)
print(data_cleaned.data.head())

# E X P L O R A C I O N    D E    L O S    D A T O S  ####
data_cleaned.exploracion_datos()

# P R E P R O C E S A M I E N T O    D E    L O S    D A T O S  ####
data_cleaned.preprocesamiento()

# quiero ver la columna de tiempo transcurrido

print(data_cleaned.data["Hora Solicitud"].head())
print(data_cleaned.data["Hora Intervención"].head())
print(data_cleaned.data['Tiempo transcurrido'].head())

# ver columnas
print(data_cleaned.data.columns)

