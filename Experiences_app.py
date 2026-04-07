import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

def afficher_experience ():
    st.header('🌍 My Experiences')
    @st.cache_data
    def load_data(file_path):
        return pd.read_excel(file_path)
    try:
        degree_df = load_data("Experiences.xlsx")
        ## Map initialization 
        m = folium.Map(location=[9.34, 2.62], zoom_start=6)
        cluster = MarkerCluster().add_to(m)
        # Loop for point
        for index, p in degree_df.iterrows():
            ## Popup_construction
            popup_html = f"""
        <div style="font-family: Arial; width: 200px;">
            <b style="color: #2E86C1;">{p['Title']} - {p['Duration']}</b><br>
            <small><b>Institution or Location :</b> {p['Institution']}</small><br>
        </div>
        """
            folium.Marker(
                location=[p['Lat'], p['Long']], popup=folium.Popup(popup_html, max_width=250),
                icon=folium.Icon(color="green", icon="info-sign")).add_to(cluster)
            st_folium(m, width=1200, height=500)
    except Exception as e:
        st.error(f"Erreur de chargement : {e})
