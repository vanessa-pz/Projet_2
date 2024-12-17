import streamlit as st
import pandas as pd

# Fonction pour charger les données
@st.cache_data
def load_data(filepath):
    """
    Charge les données depuis un fichier CSV et retourne un DataFrame.
    """
    try:
        data = pd.read_csv(filepath)
        st.success("Les données ont été chargées avec succès !")
        return data
    except Exception as e:
        st.error(f"Erreur lors du chargement des données : {e}")
        return pd.DataFrame()

# Chemin vers le fichier CSV
csv_path = r"C:\\Users\\dassi\\OneDrive\\Documents\\Wid C School\\Projet 2 Système de recommandation de films\\Df nettoyé\\table_finale_final_df (7).csv"

# Chargement des données
df = load_data(csv_path)

# Vérification et affichage des données
if not df.empty:
    st.write("**Aperçu des données :**")
    st.dataframe(df)
else:
    st.error("Aucune donnée n'a été chargée. Vérifiez le chemin du fichier.")
