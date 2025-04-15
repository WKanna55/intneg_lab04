import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
    2. Implemente funciones para generar gráficos lineales tomando como fuente de datos archivos CSV
"""
# Tema seaborn
sns.set_theme(style="darkgrid")

def CrearGrafico(df_melted, x_col, y_col, hue_col, title_chart, paises=None):
    plt.figure(figsize=(16, 9))

    # Filtrar paises si se pasa
    if paises:
        df_melted = df_melted[df_melted[hue_col].isin(paises)]

    # Crear grafico
    sns.lineplot(data=df_melted, x=x_col, y=y_col, hue=hue_col, marker="o", 
                 palette="tab10", linewidth=1)
    plt.title(title_chart, fontsize=16, weight='bold')
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)

     # Leyenda al costado derecho
    plt.legend(title=hue_col, loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=9, frameon=True)

    # Ajuste de layout para no cortar la leyenda
    plt.tight_layout(rect=[0, 0, 0.95, 1])
    plt.show()

# Cargar CSV
data01 = pd.read_csv('WEO_Data.csv')

# Identificar columnas de año
columnas_anio = [str(a) for a in range(2000, 2025)]

# Transformar a formato largo
data01_melted = data01.melt(id_vars='Country', value_vars=columnas_anio, 
                            var_name='Año',value_name='Valor')

# Limpiar datos
data01_melted['Año'] = data01_melted['Año'].astype(int)
data01_melted['Valor'] = pd.to_numeric(data01_melted['Valor'], errors='coerce')

# Listamos paises que queramos ver
paises_destacados = ['Peru', 'Brazil', 'Chile', 'Argentina', 'Mexico', 'Panama', 'Colombia', 'Venezuela']

# usamos funciona para crear grafico
CrearGrafico(data01_melted, 'Año', 'Valor', 'Country', 'Evolución económica (2000–2025)', paises=paises_destacados)

