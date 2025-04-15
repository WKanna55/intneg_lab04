import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# leer archivo
df = pd.read_excel("BI_Clientes.xlsx")

# tabla frecuencias
frecuencia_abs = df['TotalChildren'].value_counts().sort_index()
frecuencia_abs_acum = frecuencia_abs.cumsum()
frecuencia_rel = (frecuencia_abs / frecuencia_abs.sum()).round(4)
frecuencia_rel_acum = frecuencia_rel.cumsum().round(4)

tabla_frecuencia = pd.DataFrame({
    'TotalChildren': frecuencia_abs.index,
    'Frecuencia Absoluta': frecuencia_abs.values,
    'Frecuencia Absoluta Acumulada': frecuencia_abs_acum.values,
    'Frecuencia Relativa (%)': (frecuencia_rel.values * 100).round(2),
    'Frecuencia Relativa Acumulada (%)': (frecuencia_rel_acum.values * 100).round(2)
}).reset_index(drop=True)

print(tabla_frecuencia)

sns.set_theme(style="whitegrid")

# paleta personalizada
palette = sns.color_palette("rocket", as_cmap=False)

# Gráfico de barras
plt.figure(figsize=(10, 6))
barplot = sns.barplot(
    data=tabla_frecuencia,
    x='TotalChildren',
    y='Frecuencia Absoluta',
    palette=palette
)

# añadir etiquetas encima de cada barra
for index, row in tabla_frecuencia.iterrows():
    barplot.text(
        x=index,
        y=row['Frecuencia Absoluta'] + 5,  # un poco mas arriba de la barra
        s=f"{row['Frecuencia Absoluta']}",
        ha='center',
        fontsize=10,
        weight='bold'
    )

# titulos y ejes
plt.title('Distribución de Total de Hijos', fontsize=16, weight='bold')
plt.xlabel('Total de Hijos', fontsize=12)
plt.ylabel('Frecuencia Absoluta', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()