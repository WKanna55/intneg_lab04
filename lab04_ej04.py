import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Estilo general
sns.set_theme(style="whitegrid", palette="pastel")

def generar_grafico_barras(df, x_col, y_col, titulo, color_palette='viridis', orient='v'):
    plt.figure(figsize=(14, 8))
    # Ordenar por valor
    df_sorted = df.sort_values(by=y_col, ascending=True if orient == 'h' else False)
    # Elegir paleta de colores
    colores = sns.color_palette(color_palette, n_colors=len(df_sorted))
    # Crear gráfico de barras con orientación opcional
    if orient == 'v':
        barplot = sns.barplot(
            data=df_sorted, x=x_col, y=y_col,
            palette=colores
        )
        plt.xticks(rotation=45, ha='right')
        # Añadir etiquetas de valor encima de cada barra
        for i, bar in enumerate(barplot.patches):
            y_val = bar.get_height()
            barplot.annotate(f'{y_val:,.0f}', 
                             (bar.get_x() + bar.get_width() / 2, y_val), 
                             ha='center', va='bottom', fontsize=9, fontweight='bold')
    else:
        barplot = sns.barplot(
            data=df_sorted, y=x_col, x=y_col,
            palette=colores
        )
        # Añadir etiquetas de valor al final de cada barra
        for i, bar in enumerate(barplot.patches):
            x_val = bar.get_width()
            barplot.annotate(f'{x_val:,.0f}', 
                             (x_val, bar.get_y() + bar.get_height() / 2), 
                             ha='left', va='center', fontsize=9, fontweight='bold')
    # Estética general
    plt.title(titulo, fontsize=18, fontweight='bold', color='navy')
    plt.xlabel(y_col if orient == 'v' else '')
    plt.ylabel(x_col if orient == 'h' else '')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

# Leer archivo WEO
data = pd.read_csv("WEO_Data.csv")
# Filtrar solo el descriptor del PBI
filtro_pbi = data['Subject Descriptor'].str.contains('Gross domestic product', case=False, na=False)
data_pbi = data[filtro_pbi]
# Año a mostrar
año = '2022'
# Armar DataFrame de País y su valor en ese año
df_barras = data_pbi[['Country', año]].copy()
df_barras[año] = pd.to_numeric(df_barras[año], errors='coerce')
df_barras = df_barras.dropna().head(15)
# Crear gráfico bonito
generar_grafico_barras(df_barras, 'Country', año, f'Top 15 países por PBI en {año}', color_palette='mako', orient='h')
