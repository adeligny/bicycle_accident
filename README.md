# Description du projet
Ce projet consiste en l'analyse exploratoire des données (EDA) d'un fichier de données relatif aux accidents de vélo. L'objectif est d'examiner, nettoyer, et comprendre les caractéristiques du jeu de données pour en extraire des informations utiles.

Le projet inclut plusieurs étapes de prétraitement et d'analyse afin de comprendre les tendances, les patterns et les relations présentes dans les données. Ces étapes incluent :

Chargement des données : Importation et visualisation initiale des données depuis un fichier.  
Nettoyage des données : Traitement des valeurs manquantes, conversion des types de données et gestion des valeurs aberrantes.  
Analyse des variables : Exploration de la répartition des accidents en fonction de différentes variables (âge, sexe, département, conditions de lumière, etc.).  
Visualisations : Création de graphiques pour une meilleure compréhension des tendances et des relations dans les données, incluant des histogrammes, des diagrammes en barres, et des boxplots.

# Objectifs de l'EDA
L'objectif principal de cette analyse exploratoire des données (EDA) est de fournir un aperçu clair des accidents de vélo en examinant les variables clés comme :

La répartition des accidents en fonction du sexe des individus impliqués.  
La fréquence des accidents selon la tranche d'âge.  
Les conditions de lumière et leur impact sur la fréquence des accidents.  
La répartition des accidents par département et leur corrélation avec des facteurs géographiques.  
L'évolution des accidents sur une période donnée.

# Structure du projet
notebook/ : Dossier contenant le fichier Jupyter Notebook principal (eda.ipynb) avec toutes les étapes de l'analyse exploratoire.  
data/ : Dossier contenant le fichier de données des accidents de vélo (bicycle_accident.csv).  
README.md : Ce fichier, qui fournit des informations sur le projet.  
doc.pdf : Fichier contenant le descriptif des variables ainsi que le contexte de la collecte des données.

# Comment utiliser ce projet
Clone ce projet sur ton ordinateur : git clone https://github.com/adeligny/bicycle_accident.git

Installe les dépendances nécessaires : pip install -r requirements.txt

Ouvre le fichier eda.ipynb dans Jupyter Notebook ou un autre environnement Python compatible.

Exécute les cellules pour voir les résultats de l'analyse.