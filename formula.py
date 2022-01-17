import csv
import plotly.express as py

rows=[]
with open("brown_dwarfs.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        rows.append(row)






planet_masses = []
planet_radiuses = []
planet_names = []
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity = []
for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

low_gravity_planets = []
for index, gravity in enumerate(planet_gravity):
  if gravity < 10:
    low_gravity_planets.append(planet_data_rows[index])

print(len(low_gravity_planets))

planet_type_values=[]
for planet_data in planet_data_rows:
    planet_type_values.append(planet_data[6])
print(list(set(planet_type_values)))


planet_masses=[]
planet_radiuses=[]
planet_types=[]

for planet_data in low_gravity_planets:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])
    planet_types.append(planet_data[6])

fig = px.scatter(x=planet_radiuses, y=planet_masses, title="Brown dwarfs", color=planet_types)
fig.show()

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

X=[]
for index,planet_mass in enumerate(planet_masses):
    temp_list=[
                planet_radiuses[index],
                planet_mass
    ]
    X.append(temp_list)

wcss=[]
for i in range (1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.lineplot(range(1,11),wcss,marker='o',color='red')
plt.title('Brown dwarfs')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()