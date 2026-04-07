import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")
st.header('🌍 My Geospatial Projects')

# Correction du cache (Streamlit a mis à jour sa syntaxe)
@st.cache_data
def load_data(file_path):
    # Assure-toi que ton fichier s'appelle bien Projects.xlsx
    return pd.read_excel(file_path)

# Chargement (ajoute un try/except pour éviter les crashs si le fichier manque)
try:
    project_df = load_data("Projects.xlsx")
    
    # Initialisation de la carte sur Parakou
    m = folium.Map(location=[9.21, 2.37], zoom_start=8)
    cluster = MarkerCluster().add_to(m)

    # Correction de la boucle : iterrows() renvoie (index, row)
    for index, p in project_df.iterrows():
        # Construction du popup HTML propre
        popup_html = f"""
        <div style="font-family: Arial; width: 200px;">
            <b style="color: #2E86C1;">{p['Project_name']}</b><br>
            <small><b>Model:</b> {p['Model_type']}</small><br>
            <p style="font-size: 12px;">{p['Key_results']}</p>
            <p style="font-size: 10px; color: gray;">{p['Tech_stack']}</p>
            <a href="{p['GitHub']}" target="_blank" style="color: #E67E22; text-decoration: none; font-weight: bold;">
                See the project 🚀
            </a>
        </div>
        """
        
        # ATTENTION : Folium prend [Latitude, Longitude]. Vérifie l'ordre dans ton Excel !
        folium.Marker(
            location=[p['Lat'], p['Long']], 
            popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(cluster)

    # Affichage optimisé pour Streamlit
    st_folium(m, width=1200, height=500)

except Exception as e:
    st.error(f"Erreur de chargement : {e}")
    st.info("Vérifie que ton fichier 'Projects.xlsx' est bien dans le dossier et contient les colonnes : Project_name, Lat, Long, Model_type, Key_results, Tech_stack, Github.")
