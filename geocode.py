# Import the required library
from geopy.geocoders import Nominatim
import streamlit as st
import pandas as pd
# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")



cities = ["Иркутский Авиационный завод"]


lat = []
long = []
for i in cities:  
    location = geolocator.geocode(i)
    lat.append(location.latitude)
    long.append(location.longitude)

    
    # print("The latitude of the location is: ", location.latitude)
    # print("The longitude of the location is: ", location.longitude)
    # print("\n----\n")
print(lat)
print(long)
 
## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': lat,
    'longitude': long
})
 
## Create a map with the data
st.map(data) 
st.write(cities[0])
st.write("lat",str(lat))
st.write("long",str(long))
st.write("\n")
st.write("\n")
st.write("\n")
st.write(f"""
"business_address": {{
  "lat": {lat[0]},
  "long": {long[0]}
}}
""")
print(f"""
"business_address": {{
  "lat": {lat[0]},
  "long": {long[0]}
}}
""")