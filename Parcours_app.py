import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")
def afficher_parcours():
    st.header('🌍 My Education')
    @st.cache_data
    def load_data(file_path):
        return pd.read_excel(file_path)
    try:
        degree_df = load_data("Degree.xlsx")
        m = folium.Map(location=[9.34, 2.62], zoom_start=8)
        cluster = MarkerCluster().add_to(m)
        
        for index, p in degree_df.iterrows():
            popup_html = f"""
        <div style="font-family: Arial; width: 200px;">
            <b style="color: #2E86C1;">{p['Degree']} - {p['Duration']}</b><br>
            <small><b>School:</b> {p['School']}</small><br>
            <p style="font-size: 12px;">{p['Honors']}</p>
        </div>
        """
            folium.Marker(location=[p['Lat'], p['Long']], popup=folium.Popup(popup_html, max_width=250), 
                          icon=folium.Icon(color="purple", icon="info-sign")).add_to(cluster)
        st_folium(m, width=1200, height=500)
    except Exception as e:
        st.error(f"Loading error : {e}")
    
