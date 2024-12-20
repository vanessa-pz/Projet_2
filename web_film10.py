import streamlit as st
import time
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Afficher un indicateur de chargement avant d'afficher la vidéo
with st.spinner('Chargement de la page...'):
    time.sleep(2)  # Simuler un délai pour l'exemple

# Charger les données
file_path = r'C:\Users\nessp\Downloads\last_df.csv'
data = pd.read_csv(file_path)

# Préparer les données
#st.set_page_config(page_title="Recommandation de Films", layout="wide")

# Fonction pour créer une page éphémère
def page_ephemere():
    video_file = "https://www.youtube.com/watch?v=rspzzsMRl-E&t=11s&ab_channel=20thCenturyStudios"
    video_component = st.video(video_file)

# Page d'accueil
def page_accueil():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>🎞️ "Bienvenue sur Cinéma Movie Time ! Le ciné ... chez vous." 🏡</h1>
            <h3>Les films de La Creuse présentent :</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image(
        "https://img.freepik.com/vecteurs-premium/fond-film-cinema-premiere_41737-251.jpg?w=900",
        caption="Ne ratez jamais une séance grâce à Cinéma Movie Time",
        use_container_width=True
    )
    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="text-align: center;">
            <h4>Une programmation proposée par :</h4>
            <p>👩‍💻 <b>Dalia</b>, 👨🏼‍💼 <b>Mourad</b>, 👨‍💻 <b>Adrien</b>, et 👩‍🏫 <b>Vanessa</b></p>
            <p><b>Bon film et bons pop corn ! 🍿 🎦</b></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Page pour choisir les films
def page_films():
    st.title("... Et voici votre recommandation minute 😎 ! Nous vous souhaitons un agréable visionnage 😊")

    # Extraction et nettoyage des genres
    def safe_parse_genres(genre_str):
        import ast
        try:
            parsed = ast.literal_eval(genre_str)
            if isinstance(parsed, list):
                return ', '.join(parsed)
            return str(parsed)
        except (ValueError, SyntaxError):
            return "Action"

    data['genres'] = data['genres'].apply(safe_parse_genres)

    # Normalisation des colonnes numériques
    numeric_columns = data.select_dtypes(include=['number'])
    scaler = StandardScaler()
    normalized_numeric_columns = pd.DataFrame(scaler.fit_transform(numeric_columns), columns=numeric_columns.columns)

    # Division des données pour RandomForestClassifier
    X = normalized_numeric_columns
    y = pd.Categorical(data['genres']).codes
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle Random Forest
    best_rf = RandomForestClassifier(n_estimators=100, max_depth=None, min_samples_split=2, random_state=42, n_jobs=-1)
    best_rf.fit(X_train, y_train)
    data['predicted_genres'] = pd.Categorical.from_codes(best_rf.predict(X), categories=pd.Categorical(data['genres']).categories)

    # Entraîner le modèle NearestNeighbors
    nn_model = NearestNeighbors(n_neighbors=6, metric='euclidean')
    nn_model.fit(X)

    # Fonction de recommandation
    def recommander_films(nom_film):
        matches = data[data['original_title'].str.contains(nom_film, case=False, na=False)]
        if matches.empty:
            return f"Aucun film trouvé correspondant à '{nom_film}'.", None

        film_index = matches.index[0]
        distances, indices = nn_model.kneighbors([X.iloc[film_index]])
        recommandations = data.iloc[indices[0][1:]]  # Ne pas inclure le film recherché ici
        film_selectionne = data.iloc[film_index]  # Film sélectionné
        return film_selectionne, recommandations

    # Afficher les recommandations
    film_cherche = st.text_input("Que voulez-vous regarder aujourd'hui ?", "")
    if film_cherche:
        film_selectionne, recommandations = recommander_films(film_cherche)
        if isinstance(film_selectionne, str):
            st.write(film_selectionne)
        else:
            # Afficher le film recherché
            st.write(f"### Film sélectionné : {film_selectionne['original_title']}")
            st.image(film_selectionne['poster_url'], width=200)
            st.write(f"Genres: {film_selectionne['genres']} | Popularité: {film_selectionne['popularity']}")
            st.write(f"[Voir la bande-annonce]({film_selectionne['video_link']})")

            # Afficher les recommandations
            st.write("### Recommandations basées sur ce film")
            col1, col2, col3 = st.columns(3)
            for idx, row in recommandations.iterrows():
                with [col1, col2, col3][idx % 3]:
                    st.image(row['poster_url'], width=150)
                    st.write(f"#### {row['original_title']}")
                    st.write(f"[Voir la bande-annonce]({row['video_link']})")
                    st.write(f"Genres: {row['genres']} | Popularité: {row['popularity']}")
    else:
        # Bouton de film aléatoire
        if st.button("🎲 >Pas d'idées ?"):
            random_film = data.sample(1).iloc[0]
            st.image(random_film['poster_url'], width=200)
            st.write(f"### {random_film['original_title']}")
            st.write(f"Genres: {random_film['genres']} | Popularité: {random_film['popularity']}")
            st.write(f"[Voir la bande-annonce]({random_film['video_link']})")

# Fonction de recherche multi-critères
def rechercher():
    # Sélectionner le critère de recherche via un bouton
    critere = None
    if st.button("Nom du film"):
        critere = "Nom du film"
    elif st.button("Nom de l'acteur"):
        critere = "Nom de l'acteur"
    elif st.button("Année"):
        critere = "Année"
    elif st.button("Genre"):
        critere = "Genre"
    
    # Champ de saisie pour la valeur à rechercher
    if critere:
        valeur = st.text_input(f"Entrez la valeur pour {critere.lower()}")
        if critere == 'Nom du film' and valeur:
            resultats = data[data['original_title'].str.contains(valeur, case=False, na=False)]
        elif critere == 'Nom de l\'acteur' and valeur:
            resultats = data[data['primaryName'].str.contains(valeur, case=False, na=False)]
        elif critere == 'Année' and valeur:
            # Validation si l'année est un entier
            try:
                valeur = int(valeur)
                resultats = data[data['start_year'] == valeur]
            except ValueError:
                resultats = pd.DataFrame()
                st.error("Veuillez entrer une année valide.")
        elif critere == 'Genre' and valeur:
            resultats = data[data['genres'].str.contains(valeur, case=False, na=False)]
        else:
            resultats = pd.DataFrame()

        # Affichage des résultats ou message d'erreur
        if resultats.empty:
            st.write(f"Aucun résultat trouvé pour le critère '{critere}' avec la valeur '{valeur}'.")
        else:
            st.write(f"Résultats pour '{valeur}' dans le critère '{critere}' :")

            # Affichage sous forme de cartes, similaire à la recherche par titre
            col1, col2, col3 = st.columns(3)
            for idx, row in resultats.iterrows():
                with [col1, col2, col3][idx % 3]:
                    st.image(row['poster_url'], width=150)
                    st.write(f"#### {row['original_title']}")
                    st.write(f"[Voir la bande-annonce]({row['video_link']})")
                    st.write(f"Genres: {row['genres']} | Popularité: {row['popularity']}")

# Navigation entre les pages via des boutons
if st.button("Vidéo de Présentation"):
    page_ephemere()
elif st.button("Qui sommes-nous"):
    page_accueil()
elif st.button("Votre cinéma en un clic"):
    page_films()
elif st.button("Recherche Avancée"):
    rechercher()

