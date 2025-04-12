import streamlit as st

# Titre de l’appli
st.title("🚴‍♀️ Prédiction du risque d'accident de vélo")

# Formulaire utilisateur
sexe = st.selectbox("Sexe", ["Homme", "Femme"])
age = st.slider("Âge", 10, 80, 30)
moment = st.selectbox("Moment de la journée", ["Matin", "Après-midi", "Soir", "Nuit"])

# Convertir les inputs en features utilisables par le modèle
# Exemple simplifié : encodage manuel
sexe_num = 1 if sexe == "Homme" else 0
moment_num = {"Nuit": 0, "Matin": 1, "Après-midi": 2, "Soir": 3}[moment]
# gravite_num = {"Indemne": 0, "Blessé léger": 1, "Blessé hospitalisé": 2, "Tué": 3}[gravite]
