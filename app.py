import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium


st.title('FLOR REAL ESTATE')

DATA_URL = ('data.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'center_lat': 'lat', 'center_lon': 'lon'}, inplace=True)
    return data


st.sidebar.title("Specific Use Type")
add_selectbox = st.sidebar.selectbox("Type",("Condo", "Single Family Home"))

st.sidebar.title("City Filter")
add_selectbox = st.sidebar.selectbox("City",("INGLEWOOD CA", "LONG BEACH CA"))

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Real Estate Map')
# center on los angeles
m = folium.Map(location=[33.8958, -118.2201], zoom_start=10)

for k,v in data.iterrows():
  tooltip = v.propertylocation
  folium.Marker([v.lat, v.lon], popup=f"<i>{v.propertylocation}</i> <i>Price per sqft: ${round(v.pricepersqft, 3)}</i>", tooltip=tooltip).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)