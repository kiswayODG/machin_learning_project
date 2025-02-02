# 🌊 Seriez-vous un survivant du Titanic ? 🚢

![Bannière](banner.jpg)

## 📝 Description du projet  
Ce projet est une application interactive développée avec Streamlit qui permet de prédire la survie d'un passager du Titanic en fonction de plusieurs caractéristiques :  
- **Classe du passager** (1ʳᵉ, 2ᵉ ou 3ᵉ classe)  
- **Âge**  
- **Tarif du billet**  
- **Sexe** (Homme ou Femme)  

Le modèle utilisé pour la prédiction est un **Naïve Bayes Gaussien**, entraîné avec `sklearn` et exporté avec `pickle`.  

## 🎯 Modèle de Machine Learning : Naïve Bayes  
L'algorithme de Naïve Bayes repose sur la règle de Bayes : 
\[ P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)} \]

Dans notre contexte, cela correspond à :

\[ P(Survived | Pclass, Sex, Fare) = \frac{P(Pclass, Sex, Fare | Survived) \cdot P(Survived)}{P(Pclass, Sex, Fare)} \] 


Dans notre contexte :  
- \( P(Survived | Pclass, Sex, Fare) \) est la probabilité qu'un passager ait survécu en fonction de sa classe, son sexe et le prix du billet.  
- \( P(Pclass, Sex, Fare | Survived) \) est la probabilité d'observer ces caractéristiques sachant que le passager a survécu.  
- \( P(Survived) \) est la probabilité qu'un passager ait survécu dans l'ensemble du dataset.  
- \( P(Pclass, Sex, Fare) \) est la probabilité d'observer ces caractéristiques dans l'ensemble des données.  

Le modèle est entraîné avec **scikit-learn**, et les prédictions sont faites sur la base des distributions des variables.  

## 📂 Fichiers du projet

- **app.py** : Script principal contenant l'interface Streamlit et la logique de prédiction.
- **titanic_nbayes_model.pkl** : Modèle entraîné et exporté au format pickle.

## 🔧 Technologies utilisées

- **Python** : Langage de prog
- **pandas** : Manipulation et prétraitement des données
- **scikit-learn** : Entraînement du modèle (GaussianNB)
- **pickle** : Sauvegarde et chargement du modèle
- **Streamlit** : Développement de l'interface utilisateur

## 📦 Installation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/votre-repo/titanic-survival.git
cd titanic-survival
```

### 2️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application
```bash
streamlit run app.py
```

---
💡 **Auteur** : Kiswendsida OUEDRAOGO  
📧 **Contact** : [ou.kiswendsida@gmail.com]  
🌍 **LinkedIn** : [www.linkedin.com/in/o-kiswendsida]  


