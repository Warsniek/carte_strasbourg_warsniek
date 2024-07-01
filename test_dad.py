import folium
 

# Créer la carte centrée sur Strasbourg

carte = folium.Map(location=[48.5830, 7.7455], zoom_start=14)

 

# Points d'intérêt historique

points_interet = {

    "Cathédrale Notre-Dame": [48.5814, 7.7503],

    "Maison Kammerzell": [48.5811, 7.7498],

    "Palais Rohan": [48.5803, 7.7519],

    "Église Saint-Thomas": [48.5792, 7.7446],

    "Église Saint-Pierre-le-Jeune": [48.5844, 7.7457],

    "Place Kléber": [48.5830, 7.7455],

    "Petite France": [48.5796, 7.7393],

    "Ponts Couverts": [48.5790, 7.7377],

    "Barrage Vauban": [48.5778, 7.7361]

}

 

# Ajouter les points d'intérêt à la carte

for nom, coord in points_interet.items():

    folium.Marker(location=coord, popup=nom, icon=folium.Icon(color='blue')).add_to(carte)

 

# Ajouter l'hôtel Novotel Centre Halles

folium.Marker(location=[48.5856, 7.7428], popup="Novotel Centre Halles", icon=folium.Icon(color='red')).add_to(carte)

 

# Ajouter la brasserie Kooma

folium.Marker(location=[48.5851, 7.7437], popup="Brasserie Kooma", icon=folium.Icon(color='green')).add_to(carte)

 

# Enregistrer la carte

carte.save('carte_strasbourg_warsniek.html')

