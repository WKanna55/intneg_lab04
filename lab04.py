import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



"""
    1. Implemente funciones para generar gráficos lineales empleado variables 
"""





"""
    2. Implemente funciones para generar gráficos lineales tomando como fuente de datos archivos CSV
"""
# Children vs income
def CrearGrafico(df, x_col, y_col):
    sns.lineplot(data=df, x=x_col, y=y_col)
    plt.title(f'Gráfico lineal: {x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
     
#data01 = pd.read_csv('WEO_Data.csv', sep=';', encoding='latin')
data01 = pd.read_csv('WEO_Data.csv')
# Llamada a la función usando columnas del DataFrame
CrearGrafico(data01, 'Units', 'Country')