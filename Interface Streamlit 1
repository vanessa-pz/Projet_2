import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Application Multi-pages", layout="wide")

# Créer un menu de navigation avec une barre latérale
pages = ["Accueil", "Interface graphique", "Programmation", "Recommandations"]
page = st.sidebar.radio("Navigation", pages)

# Page 1 : Accueil
if page == "Accueil":
    st.title("🏠 Accueil")
    st.write("""
    Bienvenue dans l'application Streamlit multi-pages.
    
    Naviguez dans la barre latérale pour explorer les différentes sections :
    - **Interface graphique** : Visualisation des données.
    - **Programmation** : Contenu lié au code et à la programmation.
    - **Recommandations** : Système de recommandations interactif.
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Bienvenue+sur+l%27Accueil", caption="Accueil")

# Page 2 : Interface graphique
elif page == "Interface graphique":
    st.title("📊 Interface Graphique")
    st.write("Cette page est dédiée à la visualisation des graphiques et des données.")

    # Exemple : Importation de données et affichage graphique
    import pandas as pd
    import matplotlib.pyplot as plt

    # Données d'exemple
    data = {"Catégorie": ["A", "B", "C", "D"], "Valeurs": [10, 20, 15, 30]}
    df = pd.DataFrame(data)

    # Affichage des données
    st.write("### Données Exemple")
    st.dataframe(df)

    # Graphique
    st.write("### Graphique Exemple")
    fig, ax = plt.subplots()
    ax.bar(df["Catégorie"], df["Valeurs"])
    ax.set_xlabel("Catégories")
    ax.set_ylabel("Valeurs")
    st.pyplot(fig)

# Page 3 : Programmation
elif page == "Programmation":
    st.title("💻 Programmation")
    st.write("Cette page présente des exemples de code et des informations liées à la programmation.")

    st.code("""
    import streamlit as st

    # Exemple de fonction
    def addition(a, b):
        return a + b

    # Utilisation de la fonction
    result = addition(5, 3)
    st.write("Le résultat est :", result)
    """, language="python")

    st.write("L'exemple ci-dessus montre une simple fonction d'addition en Python.")

# Page 4 : Recommandations
elif page == "Recommandations":
    st.title("🎥 Recommandations")
    st.write("Cette page contient un système de recommandations interactif.")

    # Exemple : Liste de films pour recommandations
    movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Pulp Fiction"]
    selected_movie = st.selectbox("Choisissez un film :", movies)

    st.write(f"### Vous avez sélectionné : {selected_movie}")
    st.write("Voici quelques films similaires que vous pourriez aimer :")
    recommendations = {
        "Inception": ["Shutter Island", "Tenet", "Memento"],
        "Interstellar": ["Gravity", "The Martian", "Arrival"],
        "The Matrix": ["Equilibrium", "Blade Runner", "Ghost in the Shell"],
        "The Dark Knight": ["Batman Begins", "Joker", "Logan"],
        "Pulp Fiction": ["Reservoir Dogs", "Kill Bill", "Snatch"],
    }

    st.write(", ".join(recommendations.get(selected_movie, ["Pas de recommandations disponibles"])))

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**© 2024 - Application Streamlit Multi-pages**")
