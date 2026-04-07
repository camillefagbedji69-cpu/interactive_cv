import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")
st.header('🌍 My Experiences')

# Correction du cache (Streamlit a mis à jour sa syntaxe)
@st.cache_data
def load_data(file_path):
    # Assure-toi que ton fichier s'appelle bien Projects.xlsx
    return pd.read_excel(file_path)

# Chargement (ajoute un try/except pour éviter les crashs si le fichier manque)
try:
    degree_df = load_data("Experiences.xlsx")
    
    # Initialisation de la carte sur Parakou
    m = folium.Map(location=[9.34, 2.62], zoom_start=6, tiles="CartoDB dark_matter")
    cluster = MarkerCluster().add_to(m)

    # Correction de la boucle : iterrows() renvoie (index, row)
    for index, p in degree_df.iterrows():
        # Construction du popup HTML propre
        popup_html = f"""
        <div style="font-family: Arial; width: 200px;">
            <b style="color: #2E86C1;">{p['Title']} - {p['Location']}</b><br>
            <small><b>Institution or Location :</b> {p['Institution']}</small><br>
        </div>
        """
        
        # ATTENTION : Folium prend [Latitude, Longitude]. Vérifie l'ordre dans ton Excel !
        folium.Marker(
            location=[p['Lat'], p['Long']], 
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color="green", icon="info-sign")
        ).add_to(cluster)

    # Affichage optimisé pour Streamlit
    st_folium(m, width=1200, height=500)

except Exception as e:
    st.error(f"Erreur de chargement : {e}")
