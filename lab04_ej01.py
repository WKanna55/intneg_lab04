import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
  1. Implemente funciones para generar gráficos lineales empleado variables 
"""

def grafica_lineal(x, y, xlabel, ylabel, title):
    # Estilo general
    sns.set_theme(style="darkgrid")

    # Crear DataFrame temporal
    df_plot = pd.DataFrame({xlabel: x, ylabel: y})

    # Figura
    plt.figure(figsize=(12, 6))

    # Colores
    color = sns.color_palette("Set2")[0]

    # Graficar línea con puntos
    ax = sns.lineplot(data=df_plot, x=xlabel, y=ylabel, marker="o", linewidth=2.5, color=color)

    # Agregar etiquetas sobre los puntos
    for i in range(len(df_plot)):
        x_val = df_plot[xlabel][i]
        y_val = df_plot[ylabel][i]
        ax.text(x=x_val, y=y_val + (df_plot[ylabel].max() * 0.02), s=f"${x_val:,.0f}", ha='center', 
                va='bottom', fontsize=9, weight='bold', color='black')

    # Titulos y formato
    plt.title(title, fontsize=16, weight='bold')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(df_plot[xlabel], fontsize=10)
    plt.yticks(fontsize=10)

    # Ajustar limites para dejar espacio a las etiquetas
    max_y = df_plot[ylabel].max()
    plt.ylim(0, max_y * 1.15)

    plt.tight_layout()
    plt.show()

df = pd.read_csv('BI_Clientes.csv', sep=';', encoding='latin')
#print(df.columns)

df_grouped = df.groupby('TotalChildren')['YearlyIncome'].mean().reset_index()
print(df_grouped)

grafica_lineal(df_grouped['YearlyIncome'], df_grouped['TotalChildren'], 'Ingreso Anual', 
               'Total de Hijos', 'Relación entre Ingreso Anual y Total de Hijos')