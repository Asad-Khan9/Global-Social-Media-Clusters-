import json
import pandas as pd
import streamlit as st

path = "data\\Instagram accounts dataset(0-500).json"
df = pd.read_json(path)
temp = []

# Filtering out None or NaN values
for i in range(500):
    if pd.notna(df.business_address[i]):
        temp.append(df.business_address[i])

# Create a DataFrame with 'LATITUDE' and 'LONGITUDE' columns
data = pd.DataFrame(temp, columns=['lat', 'long'])

# Extract latitudes and longitudes from the DataFrame
latitudes = data['lat'].tolist()
longitudes = data['long'].tolist()

# # Print the resulting lists211111111
# print("Latitudes:", latitudes)
# print("Longitudes:", longitudes)

# Display the map, explicitly specifying the key parameter

data = pd.DataFrame({
    'latitude': latitudes,
    'longitude': longitudes
})
 
## Create a map with the data
st.map(data)