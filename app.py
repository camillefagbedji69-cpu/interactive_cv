import streamlit as st
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from Parcours_app import afficher_parcours
from Skills_app import afficher_competences
from streamlit_option_menu import option_menu 

# 1. Configuration de la page
st.set_page_config(page_title="Interactive CV - FAGBEDJI G. Camille Boris", layout="wide")

def afficher_accueil():
    st.title("👋 Welcome on my Interactive CV.")
    st.write("""Graduate student in Water and Soil Engineering with strong quantitative training in probability theory, 
    linear algebra, statistical inference and dynamical systems modeling. Research interests lie at the
    intersection of mathematical modeling, AI for scientific discovery, and complex ecological systems. 
    I'm particularly motivated by the use of nonlinear systems, probabilistic modeling and machine learning to
    understand climate–ecosystem interactions in African contexts.""")
    col1, col2 = st.columns(2)
    col1.metric("Experience", "2+ ans")
    col2.metric("Projets IA", "10+")

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
            </a> </div>
        """
            folium.Marker(location=[p['Lat'], p['Long']], popup=folium.Popup(popup_html, max_width=250),
                       icon=folium.Icon(color="blue", icon="info-sign")).add_to(cluster)
        st_folium(m, width=1200, height=500)
    except Exception as e:
           st.error(f"Loading error: {e}")

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
        st.error(f"Loading error : {e}")

## Menu 
selected = option_menu(menu_title = None, 
    options = ["Home", "Education", "Skills", "Projects", "Experience"], 
                      icons = ["house", "book", "bar-chart", "map", "briefcase"])
if selected == "Home":
  afficher_accueil()
elif selected == "Education":
  afficher_parcours()
elif selected == "Skills":
  afficher_competences()
elif selected == "Projects":
    afficher_projet()
else : 
  afficher_experience()

st.sidebar.markdown("---")
st.caption("Developped with ❤ by FAGBEDJI G. Camille Boris")
