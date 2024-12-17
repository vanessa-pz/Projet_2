import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Charger les données
# Remplacez ceci par le chemin de votre fichier ou votre DataFrame
# Par exemple : df = pd.read_csv('movies.csv')
df = pd.DataFrame({
    'averageRating': [6.4, 6.9, 7.0, 5.3, 8.2],
    'votes': [300, 150, 200, 100, 400],
    'runtime': [118, 103, 90, 105, 110],
    'start_year': [2001, 1990, 2019, 2022, 2000],
    'category': ['actor', 'director', 'actor', 'actor', 'producer'],
    'genres': ['Romance, Fantasy', 'Comedy, Drama', 'Drama', 'Action', 'Comedy'],
    'titles': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']
})

# Fonction de recommandation
def recommend_knn(movie_title, df, knn_model, X):
    try:
        movie_index = df[df['titles'] == movie_title].index[0]
        distances, indices = knn_model.kneighbors([X[movie_index]])
        recommended_movies = df.iloc[indices[0]]
        return recommended_movies[['titles', 'averageRating', 'votes', 'runtime', 'category', 'genres']]
    except IndexError:
        st.error("Le film choisi n'existe pas dans la base de données.")
        return pd.DataFrame()

# Streamlit UI
st.title("Système de Recommandation de Films")
st.sidebar.header("Options")

# Sélectionner les colonnes pertinentes
features = ['averageRating', 'votes', 'runtime', 'start_year']
scaler = StandardScaler()
X = scaler.fit_transform(df[features])

# Entraîner le modèle KNN
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(X)

# Liste des films disponibles
movie_list = df['titles'].tolist()
selected_movie = st.sidebar.selectbox("Sélectionnez un film pour les recommandations :", movie_list)

# Recommandation
if st.sidebar.button("Recommander"):
    recommendations = recommend_knn(selected_movie, df, knn, X)
    if not recommendations.empty:
        st.write("**Films recommandés :**")
        st.table(recommendations)

# Affichage des données de base
st.write("**Base de données de films :**")
st.dataframe(df)
