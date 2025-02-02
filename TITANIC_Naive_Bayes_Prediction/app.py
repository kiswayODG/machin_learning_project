import streamlit as st
from PIL import Image
import joblib
import pandas as pd
import os
dir_path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(dir_path, 'titanic_nbayes_model.pkl')


model = joblib.load(model_path)

def predict(data):
    result = model.predict(data)
    return result

# Charger l'image de la bannière
banner = Image.open(os.path.join(dir_path, 'banner.jpg'))
st.image(banner, use_container_width=True)


st.title("🌊 Seriez-vous un survivant du Titanic ? 🚢")
st.write("Voici quelques statistiques clés sur les passagers du Titanic :")

# Création de colonnes pour un affichage plus structuré
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Âge moyen", value="29,7 ans")

with col2:
    st.metric(label="Tarif moyen du billet", value="32,20 unités")

with col3:
    st.metric(label="Médiane de la classe", value="3ᵉ classe")


st.write("Remplissez les informations ci-dessous et découvrez vos chances de survie !")


with st.form(key="titanic_form"):
    col1, col2 = st.columns(2)  

    with col1:

        sexe = st.radio("Sexe", options=["Femme", "Homme"])
        sexe_value = 0 if sexe == "Femme" else 1
        
        male = 1 if sexe_value == 1 else 0
        female = 1 if sexe_value == 0 else 0
        

        pclass = st.selectbox("Classe du passager", options=[1, 2, 3])

    with col2:
        fare = st.number_input("Tarif du billet (€)", min_value=0.0, step=0.1)

        age = st.slider("Âge du passager", 0, 130, 25)

    
    submit_button = st.form_submit_button(label="🔍 Prédire la survie")

# Zone de résultat
st.subheader("📊 Résultat de la prédiction")
if submit_button:
    input_data = pd.DataFrame({
        "Pclass": [pclass],
        "Age": [age],
        "Fare": [fare],
        "female": [female],
        "male": [male]
    })
    result = predict(input_data)
    prediction = "Survivant 🟢" if result == 1  else "Non-Survivant 🔴"
    st.success(f"Selon notre modèle, vous seriez : **{prediction}**")
