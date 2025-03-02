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
L'algorithme de **Naïve Bayes** repose sur la règle de Bayes :

$$
P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)}
$$

Dans notre contexte, cela devient :

$$
P(\text{Survived} | \text{Pclass}, \text{Sex},\text{Age}, \text{Fare}) = \frac{P(\text{Pclass}, \text{Sex},\text{Age}, \text{Fare} | \text{Survived}) \cdot P(\text{Survived})}{P(\text{Pclass}, \text{Sex},\text{Age}, \text{Fare})}
$$

Où :

- \(P(\text{Survived} | \text{Pclass}, \text{Sex}, \text{Fare})\) est la probabilité qu'un passager ait survécu en fonction de sa classe, de son sexe et du prix du billet.
- \(P(\text{Pclass}, \text{Sex}, \text{Fare} | \text{Survived})\) est la probabilité d'observer ces caractéristiques sachant que le passager a survécu.
- \(P(\text{Survived})\) est la probabilité qu'un passager ait survécu dans l'ensemble du dataset.
- \(P(\text{Pclass}, \text{Sex}, \text{Fare})\) est la probabilité d'observer ces caractéristiques dans l'ensemble des données.




Le modèle est entraîné avec **scikit-learn**, et les prédictions sont faites sur la base des distributions des variables.  

## 📂 Fichiers du projet

- **app.py** : Script principal contenant l'interface Streamlit et la logique de prédiction.
- **notebook.pdf** : Le code notebook du model (sa version ipynb disponible NaiveBayes_Titanic_prediction.ipynb).
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
📧 [**Contact**](mailto:ou.kiswendsida@gmail.com)  
🌍 [**LinkedIn**](https://www.linkedin.com/in/o-kiswendsida) 


