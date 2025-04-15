import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

def generar_histograma(df, columna, titulo, bins=10, color='skyblue'):
    """
    Genera un histograma a partir de una columna numérica.

    :param df: DataFrame con los datos
    :param columna: Nombre de la columna numérica
    :param titulo: Título del gráfico
    :param bins: Cantidad de intervalos (por defecto 10)
    :param color: Color del histograma
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=columna, bins=bins, kde=True, color=color)
    plt.title(titulo, fontsize=16, weight='bold')
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

# Cargar datos
df = pd.read_csv('BI_Clientes.csv', sep=';', encoding='latin')

generar_histograma(df, 'YearlyIncome', 'Distribución del Ingreso Anual', bins=20, color='coral')