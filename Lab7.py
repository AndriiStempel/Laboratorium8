import pandas as pd
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
print("a) Pracownicy z pensją > 5000:\n", większą_pensja, "\n")

# b) 
sorted_by_age = df.sort_values(by="Wiek")
print("b) Posortowane wg wieku:\n", sorted_by_age, "\n")

# c) 
avg_salary_by_position = df.groupby("Stanowisko")["Pensja"].mean().reset_index()
print("c) Średnia pensja wg stanowiska:\n", avg_salary_by_position, "\n")

# d)
promotion_data = {
    "ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Team Leader"]
}
promotions = pd.DataFrame(promotion_data)
merged_data = df.merge(promotions, on="ID", how="left")
print("d) Dane po dodaniu awansów:\n", merged_data, "\n")

'''
# e)
csv_file_path = "...."
merged_data.to_csv(csv_file_path, index=False)

# f)
loaded_data = pd.read_csv(csv_file_path)
print("f) Wczytane dane z CSV:\n", loaded_data.head())
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
#loaded_data = pd.read_csv()

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
#updated_df = pd.([merged_df, new_student_df])

# h)
unique_oceny = df['Ocena'].unique()
print(unique_oceny)
# i)
students_with_5 = df[df['Ocena'] == 5].shape[0]
print(students_with_5)
