import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

st.title("My First Place")

st.subheader('Raw Data')

st.write("This shows the Scatter plot")

data = pd.read_csv("https://raw.githubusercontent.com/qurat-azim/instructionaldatasets/refs/heads/main/data/penguins.csv")

st.scatter_chart(data, x="flipper_length_mm", y="body_mass_g", color="species")

st.sidebar.header("Filter the Options")

selected_category = st.sidebar.selectbox('Select Category', options=['All', 'Adeilade', 'Gento', 'Chinstrap'])

if selected_category != "All":
    filtered_data = data[data['species'] == selected_category]
    st.scatter_chart(filtered_data, x="flipper_length_mm", y="body_mass_g", color="sex")
else:
    st.scatter_chart(data, x="flipper_length_mm", y="body_mass_g", color="sex")


st.write(data)

species_count = data['species'].value_counts()

st.bar_chart(species_count)




