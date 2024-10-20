import numpy as np
from collections import defaultdict

def cargar_datos(ruta):
    # Carga los datos del archivo CSV utilizando NumPy con el encabezado como nombres de columnas
    datos = np.genfromtxt(ruta, delimiter=',', dtype=None, encoding='utf-8', names=True)
    return datos

if __name__ == "__main__":
    ruta_archivo = './data/retail_sales_dataset.csv'  # Ruta del archivo en una variable
    datos = cargar_datos(ruta_archivo)  # Pasamos la ruta a la función

# Extraer las columnas necesarias utilizando los nombres de columna del archivo CSV
categorias = datos['Product_Category']  # Categoría del producto
total_ventas = datos['Total_Amount']  # Total de ventas
fechas = datos['Date']  # Fechas

# 1. Calcular el total de ventas por categoría
ventas_por_categoria = defaultdict(float)  # Usamos un diccionario para acumular las ventas por categoría

for i, categoria in enumerate(categorias):
    ventas_por_categoria[categoria] += total_ventas[i]

# Mostrar el total de ventas por categoría
print("Total de ventas por categoría:")
for categoria, total in ventas_por_categoria.items():
    print(f"{categoria}: {total}")

# 2. Calcular el promedio de ventas diarias por categoría
ventas_diarias_por_categoria = defaultdict(lambda: {'ventas_totales': 0.0, 'dias': set()})

for i, categoria in enumerate(categorias):
    fecha = fechas[i]
    ventas_diarias_por_categoria[categoria]['ventas_totales'] += total_ventas[i]
    ventas_diarias_por_categoria[categoria]['dias'].add(fecha)  # Se añade la fecha para contar los días únicos

print("\nPromedio de ventas diarias por categoría:")
for categoria, datos in ventas_diarias_por_categoria.items():
    total_ventas = datos['ventas_totales']
    dias_unicos = len(datos['dias'])  # Contar los días únicos
    promedio_ventas = total_ventas / dias_unicos
    print(f"{categoria}: {promedio_ventas:.2f}")

# 3. Identificar las categorías con mayores y menores ventas
max_categoria = max(ventas_por_categoria, key=ventas_por_categoria.get)
min_categoria = min(ventas_por_categoria, key=ventas_por_categoria.get)

print(f"\nCategoría con mayores ventas: {max_categoria} ({ventas_por_categoria[max_categoria]})")
print(f"Categoría con menores ventas: {min_categoria} ({ventas_por_categoria[min_categoria]})")
