import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("BI_Alumnos.xlsx")

# tabla frecuencias
frecuencia_abs = df['Nota'].value_counts().sort_index()
frecuencia_rel = frecuencia_abs / frecuencia_abs.sum()
frecuencia_abs_acum = frecuencia_abs.cumsum()
frecuencia_rel_acum = frecuencia_rel.cumsum()

tabla_frecuencia = pd.DataFrame({
    'Nota': frecuencia_abs.index,
    'Frecuencia Absoluta': frecuencia_abs.values,
    'Frecuencia Absoluta Acumulada': frecuencia_abs_acum.values,
    'Frecuencia Relativa': frecuencia_rel.values.round(4),
    'Frecuencia Relativa Acumulada': frecuencia_rel_acum.values.round(4)
}).reset_index(drop=True)

print(tabla_frecuencia)

# grafico seaborn
sns.set_theme(style="whitegrid")
colors = sns.color_palette("Set2")
plt.figure(figsize=(14, 8))

sns.barplot(
    x='Nota',
    y='Frecuencia Absoluta',
    data=tabla_frecuencia,
    color=colors[0],
    label='Frecuencia Absoluta'
)

sns.barplot(
    x='Nota',
    y='Frecuencia Absoluta Acumulada',
    data=tabla_frecuencia,
    color=colors[1],
    alpha=0.7,
    label='Frecuencia Absoluta Acumulada'
)

for index, row in tabla_frecuencia.iterrows():
    plt.text(index - 0.2, row['Frecuencia Absoluta'] + 0.5, int(row['Frecuencia Absoluta']), color='black', fontweight='bold')
    plt.text(index + 0.1, row['Frecuencia Absoluta Acumulada'] + 0.5, int(row['Frecuencia Absoluta Acumulada']), color='black', fontweight='bold')

plt.title('Distribución de Frecuencia de Notas', fontsize=18, weight='bold')
plt.xlabel('Nota', fontsize=14)
plt.ylabel('N° Estudiantes', fontsize=14)
plt.legend(loc='upper left', fontsize=12, frameon=True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
