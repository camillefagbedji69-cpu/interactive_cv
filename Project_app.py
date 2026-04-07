import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")

def afficher_projet():
    st.header('🌍 My Projects')
    try:
        project_df = pd.read_excel("Projects.xlsx")
        
        m = folium.Map(location=[9.21, 2.37], zoom_start=8)
        cluster = MarkerCluster().add_to(m)
        
        for index, p in project_df.iterrows():
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
            folium.Marker(location=[p['Lat'], p['Long']], popup=folium.Popup(popup_html, max_width=250),
            icon=folium.Icon(color="blue", icon="info-sign")).add_to(cluster)
        st_folium(m, width=1200, height=500)
    except Exception as e:
           st.error(f"Loading error: {e}")
