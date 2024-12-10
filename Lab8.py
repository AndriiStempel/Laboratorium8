import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Zadanie 1

data = {
    "Kategoria": ["Komputery", "Monitory", "Klawiatury", "Myszy", "laptopy"],
    "Sprzedane Produkty": [150, 200, 290, 250, 50]
}
'''
df = pd.DataFrame(data)
plt.figure(figsize=(10, 5))
plt.bar(df["Kategoria"], df["Sprzedane Produkty"], color="black", edgecolor="black")
for index, value in enumerate(df["Sprzedane Produkty"]):
    plt.text(index, value + 5, str(value), ha="center", fontsize=10)
plt.tight_layout()
plt.show()

#Zadanie 2
labels = data["Kategoria"]
sizes = data["Sprzedane Produkty"]

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
'''
data1 = {
    "czas" : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "predkosc" : [0, 5, 10, 15, 20, 25, 30, 28, 25, 20]  
 }
df1 = pd.DataFrame(data1)

plt.figure(figsize=(8, 6))
plt.scatter(df1["czas"], df1["predkosc"])

plt.xlabel("Czas [s]", fontsize=12)
plt.ylabel("Prędkość [m/s]", fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=12)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()

