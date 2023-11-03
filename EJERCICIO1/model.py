import pandas as pd
import numpy as np

import re

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
        print(Fore.CYAN+"E X P L O R A C I O N    D E    L O S    D A T O S:"+Fore.WHITE)
        print()
        print(Fore.BLUE+"1.  Ver las primeras FILAS:" "\n"+Fore.WHITE,self.data.head())
        print()
        print(Fore.BLUE+"2.  Ver las COLUMNAS: ""\n"+Fore.WHITE,self.data.columns)
        print()
        print(Fore.BLUE+"3.  Ver los TIPOS DE DATOS: ""\n"+Fore.WHITE,self.data.dtypes)
        print()
        print(Fore.BLUE+"4.  Ver los VALORES UNICOS:""\n"+Fore.WHITE,self.data.nunique())
        print()
        print(Fore.BLUE+"5.  Ver el SIZE:""\n"+Fore.WHITE,self.data.size)
        print()
        print(Fore.BLUE+"6.  Ver el SHAPE:""\n"+Fore.WHITE,self.data.shape)
        print()
        print(Fore.BLUE+"7.  Ver los VALORES FALTANTES:""\n"+Fore.WHITE,self.data.isnull().sum().sum()/self.data.size*100,"%")
        print()
        print(Fore.BLUE+"8.  Ver los VALORES FALTANTES:""\n"+Fore.WHITE,self.data.isnull().sum()/len(self.data)*100)
        print()
        print(Fore.BLUE+"9.  Ver los VALORES NULOS:""\n"+Fore.WHITE,self.data[self.data==0].count()/len(self.data)*100)
        print()
        print(Fore.BLUE+"10.  Ver los VALORES DUPLICADOS:""\n"+Fore.WHITE,self.data.duplicated().sum()/len(self.data)*100,"%")
        print()
        print(Fore.BLUE+"11.  Ver los VALORES CATEGORICOS:""\n"+Fore.WHITE,self.data.select_dtypes(include=['object']).columns)
        print()
        print(Fore.BLUE+"12.  Ver los VALORES NUMERICOS:""\n"+Fore.WHITE,self.data.select_dtypes(include=['int64','float64']).columns)
        print()
        print(Fore.BLUE+"13.  Ver la CARDINALIDAD DE LAS VARIABLES CATEGORICAS:""\n"+Fore.WHITE,self.data.select_dtypes(include=['object']).nunique())
        print()
        print(Fore.BLUE +"14. Ver resumen estadistico de VARIABLES NUMÉRICAS:""\n"+Fore.WHITE,self.data.describe())
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
        #self.data = self.data.fillna(0) 
        self.data = self.data.replace(np.nan, 0)
        pass
    def tiempo_transcurrido(self):
        # Calculamos el tiempo transcurrido entre la inervencion y la solicitud
        self.data['Tiempo transcurrido'] = self.data['Hora Intervención'] - self.data['Hora Solicitud']
        # volVer a conVertir a formato de tiempo
        #self.data['Tiempo transcurrido'] = pd.to_timedelta(self.data['Tiempo transcurrido'], unit='s')
    
    def hora_intervencion_distrito(self):
        # Crear una columna nueva con la de hora de intervencion media por distrito que se llame "Hora Intervención Media"
        self.data['Hora Intervención Media'] = self.data.groupby('Distrito')['Hora Intervención'].transform('mean')

        # oordenar por hora de intervencion media
        self.data = self.data.sort_values('Hora Intervención Media')

    def incidentes_hospital(self):
        # Count incidents per hospital and pivot the data
        hospital_counts = self.data.groupby('Hospital').size().reset_index(name='Incidentes por Hospital')
        #hospital_counts = hospital_counts.sort_values('Incidentes por Hospital', ascending=False)
        self.data["Incidentes por Hospital"] = hospital_counts["Incidentes por Hospital"]
        print(self.data["Incidentes por Hospital"])

    def preprocesamiento(self):
        self.datatime()
        self.valores_faltantes()
        self.tiempo_transcurrido()
        self.hora_intervencion_distrito()

    def controller(self):
        self.clean_data()
        self.preprocesamiento()

    def show(self):
        self.clean_data()
        self.exploracion_datos()
        self.preprocesamiento()

def main():
    csv_url = "https://datos.madrid.es/egobfiles/MANUAL/300178/activaciones_samur_2023.csv"
    model = EmergenciasModel(csv_url)
    model.show()

if __name__ == "__main__":
    main()

  