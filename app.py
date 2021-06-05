import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
import folium


st.title('2028 Summer Olympics')

DATA_URL = ('data.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'center_lat': 'lat', 'center_lon': 'lon'}, inplace=True)
    return data


st.sidebar.title("Filters")
house_types = st.sidebar.multiselect("Type",["Condo", "Single Family Residence"], default=["Single Family Residence", "Condo"])
cities = st.sidebar.multiselect("City",["INGLEWOOD CA", "LONG BEACH CA"], default=["INGLEWOOD CA", "LONG BEACH CA"])

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.write('You selected:', ', '.join([i for i in house_types]))
filter_df = data[(data['house_type'].isin(house_types) & data['city'].isin(cities))]

st.subheader('2028 Olympic Venues')
# center on compton
m = folium.Map(location=[33.958226, -118.341981], zoom_start=10)

folium.Marker(
    location=[33.7637, -118.1927],
    popup="Long Beach Sports Park",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.Marker(
    location=[33.9582, -118.3419],
    popup="The Great Western Forum",
    icon=folium.Icon(color="red"),
).add_to(m)


for k,v in filter_df.iterrows():
  tooltip = v.propertylocation
  popup_txt = f"{v.propertylocation}<br>Price per sqft: ${round(v.pricepersqft, 3)}<br>{v.house_type}"
  popup = folium.Popup(popup_txt, max_width=350,min_width=300)
  folium.Marker([v.lat, v.lon], popup=popup, tooltip=tooltip).add_to(m)

# call to render Folium map in Streamlit
folium_static(m)