# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Charger le modèle et le scaler
with open('model_accident.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler_accident.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Interface Streamlit
st.title("🚴 Prédiction du Risque d'Accident de Vélo")

st.write("\nRemplissez les informations ci-dessous pour estimer votre risque d'accident.")

# Formulaire utilisateur
age = st.slider("Quel est votre âge ?", 16, 100, 30)
heure = st.slider("A quelle heure prévoyez-vous de conduire ?", 0, 23, 14)
sexe = st.selectbox("Quel est votre sexe ?", ("Homme", "Femme"))
trajet = st.selectbox("Type de trajet", ("Domicile-Travail", "Professionnel", "Loisirs", "Autre"))
catr = st.selectbox("Type de route", ("Autoroute", "Route Nationale", "Route Départementale", "Ville", "Autre"))
surf = st.selectbox("Etat de la chaussée", ("Sèche", "Mouillée", "Verglacée", "Neige"))
atm = st.selectbox("Conditions météo", ("Normale", "Pluie", "Brouillard", "Neige", "Autre"))

# Encodage manuel des inputs utilisateur
data = {
    'age': age,
    'heure': heure,
    'sexe': 1 if sexe == "Homme" else 0,
    'trajet_2.0': 1 if trajet == "Professionnel" else 0,
    'trajet_3.0': 1 if trajet == "Loisirs" else 0,
    'trajet_4.0': 1 if trajet == "Autre" else 0,
    'trajet_5.0': 1 if trajet == "Domicile-Travail" else 0,
    'catr_2': 1 if catr == "Route Nationale" else 0,
    'catr_3': 1 if catr == "Route Départementale" else 0,
    'catr_4': 1 if catr == "Ville" else 0,
    'catr_5': 1 if catr == "Autre" else 0,
    'surf_2.0': 1 if surf == "Mouillée" else 0,
    'surf_3.0': 1 if surf == "Verglacée" else 0,
    'surf_4.0': 1 if surf == "Neige" else 0,
    'atm_2.0': 1 if atm == "Pluie" else 0,
    'atm_3.0': 1 if atm == "Brouillard" else 0,
    'atm_4.0': 1 if atm == "Neige" else 0,
    'atm_5.0': 1 if atm == "Autre" else 0
}

input_df = pd.DataFrame([data])

# Ajouter les colonnes manquantes si besoin
expected_cols = scaler.feature_names_in_
for col in expected_cols:
    if col not in input_df.columns:
        input_df[col] = 0

# Remettre dans l'ordre
input_df = input_df[expected_cols]

# Prédiction
input_scaled = scaler.transform(input_df)
prediction = model.predict_proba(input_scaled)[0,1]

if st.button("Prédire le risque"):
    st.success(f"Votre probabilité estimée d'accident grave est de {prediction*100:.1f}%")
