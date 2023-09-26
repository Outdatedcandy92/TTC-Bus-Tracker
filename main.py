import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
from streamlit_option_menu import option_menu


page_title = "TTC BUS TRACKER"
page_icon = "💸"
layout = "centered"
# -----
st.set_page_config(page_title=page_title,layout=layout)
st.title(page_title)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


selected = option_menu(
    menu_title=None,
    options=["Brentcliff", "Hanna"],
    orientation="horizontal",
)

if selected == "Brentcliff":
    st.title("To Brentcliff (54)")
    val = st.empty()
    speed= st.empty()
    while True:
        webreq = requests.get('https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=2247&routeTag=54')
        soup = BeautifulSoup(webreq.content)
        arrival = int((soup.find('prediction').attrs)['seconds'])
        vehicalid = (soup.find('prediction').attrs)['vehicle']
        inforeq = requests.get('https://retro.umoiq.com/service/publicXMLFeed?command=vehicleLocations&a=ttc&r=54&t=0')
        soupinfo = BeautifulSoup(inforeq.content)
        vehinfo = (soupinfo.find(id=f'{vehicalid}').attrs)['speedkmhr']
        if arrival > 60:
            min = (soup.find('prediction').attrs)['minutes']
            val.write(f"Arriving In {min} Minutes")
            speed.write(f"Speed: {vehinfo} Km/H")
            time.sleep(10)
        elif arrival <= 60:
            val.write(f"Arriving In {arrival} Seconds")
            speed.write(f"Speed: {vehinfo} Km/H")
            time.sleep(10)

         
if selected == "Hanna":
    st.title("To Hanna (54)")
    val = st.empty()
    speed = st.empty()
    while True:
        webreq = requests.get('https://retro.umoiq.com/service/publicXMLFeed?command=predictions&a=ttc&stopId=2251&routeTag=54')
        soup = BeautifulSoup(webreq.content)
        arrival = int((soup.find('prediction').attrs)['seconds'])
        vehicalid = (soup.find('prediction').attrs)['vehicle']
        inforeq = requests.get('https://retro.umoiq.com/service/publicXMLFeed?command=vehicleLocations&a=ttc&r=54&t=0')
        soupinfo = BeautifulSoup(inforeq.content)
        vehinfo = (soupinfo.find(id=f'{vehicalid}').attrs)['speedkmhr']
        
        if arrival > 60:
            min = (soup.find('prediction').attrs)['minutes']
            val.write(f"Arriving In {min} Minutes")
            speed.write(f"Speed: {vehinfo} Km/H")
            time.sleep(10)
        elif arrival <= 60:
            val.write(f"Arriving In {arrival} Seconds")
            speed.write(f"Speed: {vehinfo} Km/H")
            time.sleep(10)    
