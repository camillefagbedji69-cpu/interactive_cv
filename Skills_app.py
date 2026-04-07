import streamlit as st
import pandas as pd
import folium
import plotly.express as px

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")
st.header('🌍 My skills')

# Correction du cache (Streamlit a mis à jour sa syntaxe)
@st.cache_data
def load_data(file_path):
    # Assure-toi que ton fichier s'appelle bien Projects.xlsx
    return pd.read_excel(file_path)

# Chargement (ajoute un try/except pour éviter les crashs si le fichier manque)
try:
    skills_df = load_data("Skills.xlsx")

    fig = px.bar(skills_df, y = "Skills", x = "Level", color = "Category", orientation='h', text='Level')
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    st.subheader("Technical Proficiency")
    st.plotly_chart(fig, use_container_width=True)
except : 
    st.error("Check anything are good") 
