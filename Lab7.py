import pandas as pd
#Zadanie 1

df = pd.read_csv('demografia.csv')
print(df)

#Zadanie 2

plik = 'demografia.csv'

plik = 'demografia.csv'
dane = pd.read_csv(
    plik,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)
index_max = dane['2022'].idxmax(skipna=True)
kraj = dane.loc[index_max, 'KRAJE']
print ("max przyrost ludnosci w 2022r jest w:", kraj,"z przyrostem:",index_max)

#Zadanie 3
plik = 'demografia.csv'

dane = pd.read_csv(plik, decimal=',', na_values=['NA', 'n/a', 'Nan'])
dane_bezkraju = dane.drop(columns=["KRAJE"])
max_przyrost = dane_bezkraju.max().max()
rok_max_przyrost = dane_bezkraju.max().idxmax()
index_max_przyrost = dane_bezkraju[rok_max_przyrost].idxmax()
kraj = dane.loc[index_max_przyrost, "KRAJE"]
print("\n",kraj)

#Zadanie 4
data = {
    "ID": [1, 2, 3, 4, 5],
    "Imię": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "Nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "Stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "Wiek": [35, 28, 40, 30, 45],
    "Pensja": [8000, 4500, 6000, 5500, 7000]
}
df = pd.DataFrame(data)

# a) 

większą_pensja = df[df["Pensja"] > 5000]
print(większą_pensja,"\n")

# b) 
sorted_by_age = df.sort_values(by="Wiek")
print(sorted_by_age,"\n")

# c)
avg_salary_by_position = df.groupby("Stanowisko")["Pensja"].mean().reset_index()
print(avg_salary_by_position,"\n")

# d) 
promotion_data = {
    "ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Team Leader"]
}
promotions = pd.DataFrame(promotion_data)
merged_data = df.merge(promotions, on="ID", how="left")
print(merged_data,"\n")

'''
csv_file_path = ".csv"
merged_data.to_csv(csv_file_path, index=False)

f) 
csv_file_path, loaded_data.head()
'''
#Zadanie 5
data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
#a)
df = pd.DataFrame(data)
większa= df[df['Ocena'] > 4]
print(większa, "\n")

#b)
posortowane_wiekom = df.sort_values(by='Wiek')
print(posortowane_wiekom, "\n")

#c)
zgrupowane_studencie = df.groupby('Ocena')['Wiek'].mean()
print(zgrupowane_studencie)

#d)
data_poprawy = {
    'Nr_albumu': [1, 2, 3],
    'Ocena_poprawa': [5.0, 4.5, 5.0]
}
df_poprawa = pd.DataFrame(data_poprawy)
print(df_poprawa)
merged_df = pd.merge(df,df_poprawa, on='Nr_albumu', how='left')

#e)
merged_df.to_csv("Poprawka", index=False)

#f)

#g)
new_student = {
    'Nr_albumu': 6,
    'Imię': 'Alicja',
    'Nazwisko': 'Kwiatkowska',
    'Ocena': 4.7,
    'Wiek': 22,
    'Ocena_poprawa': None
}
new_student_df = pd.DataFrame([new_student])
updated_df = pd.new_studnet_df([merged_df, new_student_df])

# h)
unique_oceny = df['Ocena'].unique()
print(unique_oceny)
# i)
students_with_5 = df[df['Ocena'] == 5].shape[0]
print(students_with_5)