import streamlit as st
import pandas as pd
import folium
import plotly.express as px

st.set_page_config(page_title="Geospatial Portfolio - Boris", layout="wide")

def afficher_experience():
    st.header('🌍 My skills')
    @st.cache_data
    def load_data(file_path):
        return pd.read_excel(file_path)
    try:
        skills_df = load_data("Skills.xlsx")
        
        fig = px.bar(skills_df, y = "Skills", x = "Level", color = "Category", orientation='h', text='Level')
        fig.update_traces(texttemplate='%{text}%', textposition='outside')
        fig.update_layout(showlegend=False, yaxis={'categoryorder':'total ascending'})
        st.subheader("Technical Proficiency")
        st.plotly_chart(fig, use_container_width=True)
    except : 
        st.error("Check anything are good") 
