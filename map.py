import streamlit as st
import pandas as pd
 
## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [57.6263877],
    'longitude': [39.8933705]
})
 
## Create a map with the data
st.map(data)
