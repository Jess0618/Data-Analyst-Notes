import pandas as pd
import matplotlib.pyplot as plt

file = 'Zara_sales_EDA.csv'
df = pd.read_csv(file, delimiter=';').copy()

print("Primeras filas del dataset:")
print(df.head())

print("\nEstadísticas descriptivas:")
print(df.describe().round(2))

print("\nForma del dataset (filas, columnas):", df.shape)

df = df.drop_duplicates(subset=['name', 'price'])
df.to_csv('zara_sales_clean.csv', index=False)

print("\nDataset limpio guardado como 'zara_sales_clean.csv'")
print(df.head())

plt.figure(figsize=(8,5))
plt.hist(df["price"], bins=30, edgecolor='black')
plt.title("Distribución de precios de productos Zara")
plt.xlabel("Precio (USD)")
plt.ylabel("Frecuencia")
plt.grid(axis='y', alpha=0.3)
plt.show()

plt.figure(figsize=(7,3))
plt.boxplot(df["price"], vert=False, patch_artist=True)
plt.title("Rango y outliers de precios de Zara")
plt.xlabel("Precio (USD)")
plt.show()

plt.figure(figsize=(7,5))
plt.scatter(df["price"], df["Sales Volume"], alpha=0.6)
plt.title("Relación entre precio y volumen de ventas")
plt.xlabel("Precio (USD)")
plt.ylabel("Volumen de ventas")
plt.grid(True, alpha=0.3)
plt.show()

ventas_por_producto = (
    df.groupby("name")["Sales Volume"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

plt.figure(figsize=(9,5))
ventas_por_producto.plot(kind="bar", color="royalblue", edgecolor='black')
plt.title("Top 5 productos más vendidos")
plt.xlabel("Nombre del producto")
plt.ylabel("Volumen total de ventas")
plt.xticks(rotation=45, ha="right")
plt.grid(axis='y', alpha=0.3)
plt.show()

mean_price = df["price"].mean()
mean_sales = df["Sales Volume"].mean()

print("\nPrecio promedio: {:.2f} USD".format(mean_price))
print("Volumen promedio de ventas: {:.2f}".format(mean_sales))
