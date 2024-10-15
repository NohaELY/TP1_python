import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
cities = pd.read_csv('C:/Users/NohailaELYASSARI/Desktop/Python/cities.csv')
print(cities.head())
 
cities.columns = [col.replace('"', '').strip() for col in cities.columns]
print(cities.columns)
 
cities["LaTotal"] = cities["LatD"] + (cities["LatM"] / 60) + (cities["LatS"] / 3600)
print(cities["LaTotal"])
 
cities["LoTotal"] = cities["LonD"] + (cities["LonM"] / 60) + (cities["LonS"] / 3600)
print(cities["LoTotal"])
 
# Q2: 
cities["NS"] = cities["NS"].str.replace('"N"', 'N') 
print(cities["NS"])
 
df_cities = cities[cities["NS"] == 'N']
print(df_cities)
 
# Q3: 
pop = pd.read_csv('C:/Users/NohailaELYASSARI/Desktop/Python/Population_data.csv')

df = pd.merge(pop, df_cities, on="City", how="left")
 
# Q4: 
df_regroup = df.groupby("City").agg({
    "Population_2020": "first",
    "Growth_rate": "first"
}).reset_index()  
 
df_regroup["pop_2025"] = df_regroup["Population_2020"] * (1 + df_regroup["Growth_rate"] / 100) ** 5
print(df_regroup)
 
# Q5: 
df_cities_1 = df_regroup[df_regroup["pop_2025"] > 1000000]
print(df_cities_1)
 
# Q6: 
population_projetee = df_cities_1.sort_values(by='pop_2025', ascending=False)
top_10_villes = population_projetee.head(10)
 
plt.figure(figsize=(10, 6))
plt.bar(top_10_villes["City"], top_10_villes['pop_2025'], color='red')  # Correction du nom de la colonne
plt.title('10 Villes avec la Population Projetée la Plus Élevée en 2025')
plt.xlabel('Ville')
plt.ylabel('Population Projetée en 2025')
plt.xticks(rotation=45)
plt.tight_layout()
 
# Afficher le graphique
plt.show()
#Q7
np.random.seed(0)
df["Area"] = np.random.randint(100, 1001, size=len(df))
df['Densité_population'] = df['Population_2020'] / df['Area']
print(df_regroup)
#Q8
dfMax=df.max(axis=0)['Densité_population']
dfMin=df.min(axis=0)['Densité_population']
#Q9
villes_densite_elevee = df[df['Densité_population'] > 5000]
print(villes_densite_elevee)
#Q10
dfMoyen = np.average(df["Population_2020"])
dfMedian = np.median(df["Population_2020"])
#Q11
df["Pop_norm"]=(df["Population_2020"]-dfMin)/(dfMax-dfMin)
#Q12
moyenne = np.mean(df['Population_2020'])
ecart_type = np.std(df['Population_2020'])
minimum = np.min(df['Population_2020'])
maximum = np.max(df['Population_2020'])
 
# Créer un tableau des statistiques descriptives
statistiques = {
    'Moyenne': moyenne,
    'Écart-type': ecart_type,
    'Minimum': minimum,
    'Maximum': maximum
}
 
# Convertir le dictionnaire en DataFrame pour un affichage propre
statistiques_df = pd.DataFrame(statistiques, index=[0])
 
# Afficher le tableau des statistiques descriptives
print(statistiques_df)

