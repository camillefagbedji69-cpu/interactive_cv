import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Interactive CV - FAGBEDJI G. Camille Boris", layout="wide")

from streamlit_option_menu import option_menu 

def afficher_accueil():
    st.title("👋 Welcome on my Interactive CV.")
    st.write("""Graduate student in Water and Soil Engineering with strong quantitative training in probability theory, 
    linear algebra, statistical inference and dynamical systems modeling. Research interests lie at the
    intersection of mathematical modeling, AI for scientific discovery, and complex ecological systems. 
    I'm particularly motivated by the use of nonlinear systems, probabilistic modeling and machine learning to
    understand climate–ecosystem interactions in African contexts.""")
    st.image("Boris_Fagbedji.jpg")
    col1, col2 = st.columns(2)
    col1.metric("Experience", "2+ ans")
    col2.metric("Projets IA", "10+")

## Menu 
selected = option_menu(menu_title = None, 
    options = ["Home", "Education", "Skills", "Projects", "Experience"], 
                      icons = ["home", "book", "bar-chart", "map", "briefcase"])

# 4. Logique d'affichage
if selected == "Home":
  afficher_accueil()
elif selected == "Education":
  from Parcours_app import afficher_parcours
  afficher_parcours()
elif selected == "Skills":
  from Skills_app import afficher_competences
  afficher_competences()
elif selected == "Projects":
  from Project_app import afficher_projet
  afficher_projet()
else : 
  from Experiences_app import afficher_experience
  afficher_experience()

st.sidebar.markdown("---")
st.caption("Developped with ❤ by FAGBEDJI G. Camille Boris")
