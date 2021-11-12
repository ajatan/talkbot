import streamlit as st
import folium
from streamlit_folium import folium_static
import requests as req
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
text = req.get(url).json()
Cities = []
for city in text:
    Cities.append(city["name"])
place = st.selectbox(
    '場所',
    Cities
)
places = [ [43.01639831137239, 144.31722788052014],[43.91069634592847, 142.39680151210288],[43.077604221521526, 141.36057699051048],[40.839887116076795, 140.75492053862052] ]
option = st.selectbox(
    '情報',
    ('天気','波','風'))
days = ["今日","明日","明後日"]

for i,day in enumerate(days):
    
    if(option=="天気"):
        st.write(f"{day}の{option}：" + text[0]["srf"]["timeSeries"][0]["areas"]["weathers"][i])
    if(option=="波"):
        st.write(f"{day}の{option}：" + text[0]["srf"]["timeSeries"][0]["areas"]["waves"][i])
    if(option=="風"):
        st.write(f"{day}の{option}：" + text[0]["srf"]["timeSeries"][0]["areas"]["winds"][i])
m = folium.Map(location=places[Cities.index(place)], zoom_start=6)
folium_static(m)