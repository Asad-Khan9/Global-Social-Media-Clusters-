import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from plotly import graph_objects as go
import random 
data = pd.read_pickle("dashboard_data\\try_data.pkl")




# st.set_page_config(layout="centered")
title = "<h1 style = 'text-align: center;'>Global Instagram Centers of Influence - Bubble Map</h1>"
st.markdown(title, unsafe_allow_html=True)
with st.sidebar:
    clusters = st.select_slider(label="Number of clusters", options= range(1,11), value=3)
    weighting = st.selectbox(label= "Select the weight criteria",options=["account_count","followers", "is_verified","posts_count", "category_encoded", "avg_engagement"])
if weighting == "account_count":
    finaal_weighting = None
else:
    finaal_weighting = data[weighting]
#ml algo 
# ml_algo = KMeans(n_clusters=clusters).fit(X = data[["latitudes", 'longitudes']], sample_weight= data["followers"])
ml_algo = KMeans(n_clusters=clusters).fit(X = data[["latitudes", 'longitudes']], sample_weight= finaal_weighting)
cluster_labels = ml_algo.labels_
plot_dataframe = data.copy()
plot_dataframe["clusters"] = cluster_labels

colors = [
    "Aqua", "Aquamarine", "Azure", "Beige", "Black", "Blue", "Blueviolet", "Brown", "Burlywood", "Cadetblue",
    "Chartreuse", "Chocolate", "Coral", "Cornflowerblue", "Crimson", "Cyan", "Darkblue", "Darkcyan",
    "Darkgoldenrod", "Darkgray", "Darkgreen", "Darkkhaki", "Darkmagenta", "Darkolivegreen", "Darkorange",
    "Darkorchid", "Darkred", "Darksalmon", "Darkseagreen", "Darkslateblue", "Darkslategray", "Darkslategrey",
    "Darkturquoise", "Darkviolet", "Deeppink", "Deepskyblue", "Dimgray", "Dodgerblue", "Firebrick", "Forestgreen",
    "Fuchsia", "Gold", "Goldenrod", "Gray", "Grey", "Green", "Greenyellow", "Hotpink", "Indianred", "Indigo",
    "Khaki", "Lavender", "Lavenderblush", "Lawngreen", "Lemonchiffon", "Lightblue", "Lightcoral", "Lightcyan",
    "Lightgoldenrodyellow", "Lightgray", "Lightgreen", "Lightpink", "Lightsalmon", "Lightseagreen", "Lightskyblue",
    "Lightslategray", "Lightslategrey", "Lightsteelblue", "Lime", "Limegreen", "Magenta", "Maroon", "Mediumaquamarine",
    "Mediumblue", "Mediumorchid", "Mediumpurple", "Mediumseagreen", "Mediumslateblue", "Mediumspringgreen",
    "Mediumturquoise", "Mediumvioletred", "Midnightblue", "Navy", "Olive", "Olivedrab", "Orange", "Orangered",
    "Orchid", "Palegoldenrod", "Palegreen", "Paleturquoise", "Palevioletred", "Papayawhip", "Peachpuff", "Peru",
    "Pink", "Plum", "Powderblue", "Purple", "Red", "Rosybrown", "Royalblue", "Rebeccapurple", "Saddlebrown",
    "Salmon", "Sandybrown", "Seagreen", "Sienna", "Silver", "Skyblue", "Slateblue", "Slategray", "Slategrey", "Snow",
    "Springgreen", "Steelblue", "Tan", "Teal", "Thistle", "Tomato", "Turquoise", "Violet", "Yellow", "Yellowgreen"
]

counter = 0  # Initialize counter
fig = go.Figure()

for cluster in plot_dataframe["clusters"].unique():
    temp = plot_dataframe[plot_dataframe["clusters"] == cluster]
    fig.add_trace(go.Scattermapbox(
        lat=temp["latitudes"],
        lon=temp["longitudes"],
        mode='markers',
        marker=dict(
            size=8,  # Use influence level to determine marker size
            color = random.choice(colors)
        ),
        name=f'Cluster {cluster}'
    ))
    counter += 1

fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=0,
    mapbox_center_lat=0,
    mapbox_center_lon=0,
    height=800,
    width = 2000,
)
st.plotly_chart(fig, theme=None, use_container_width=True)
# st.plotly_chart(fig)
