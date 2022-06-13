#import pip
#pip.main(['uninstall'] + ['rtree'])
#pip.main(['install'] + ['rtree'])

#import rtree
import geopandas as gpd
import sklearn.linear_model as sk
import matplotlib as mpl
import requests
import seaborn as sns
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from string import ascii_letters



st.title("Перекошена ли Москва на запад?")

st.write ("Москва — большой и разнообразный город, в котором есть как более зажиточные, так и достаточно бедные районы. Если вы москвич, то вы наверняка слышали про бесконечные давки в метро в Выхино, преступников из Гольяново и этническую напряженность в Бирюлево. В целом есть представление о том, что самые неблагополучные районы — на востоке. Этот проект немного проверяет стереотип с помощью простых прокси: мы сравниваем, больше ли на западе или на востоке дорогих кафе и магазинов? В качестве образцов я взял Азбуку Вкуса, Кофеманию и Синнабон. С выбором можно спорить, но на мой вкус, достаточно дорого :) Сначала давайте посмотрим на их расположение на карте Москвы")

districts = gpd.read_file ("http://gis-lab.info/data/mos-adm/mo.geojson")

entrypoint = "https://nominatim.openstreetmap.org/search"
mon = gpd.read_file (requests.get (entrypoint, params = {'q': 'Москва, Кофемания', 'format': 'geojson', 'limit': '50', 'viewbox' : '37.834178, 55.586639, 37.372537, 55.907720', 'bounded': '1'}).url)
azb = gpd.read_file (requests.get (entrypoint, params = {'q': 'Москва, Азбука Вкуса', 'format': 'geojson', 'limit': '50', 'viewbox' : '37.834178, 55.586639, 37.372537, 55.907720', 'bounded': '1'}).url)
cnb  = gpd.read_file (requests.get (entrypoint, params = {'q': 'Москва, Cinnabon', 'format': 'geojson', 'limit': '50', 'viewbox' : '37.834178, 55.586639, 37.372537, 55.907720', 'bounded': '1'}).url)

choice = st.multiselect ("Что показать?", ["Кофемания", "Азбука", "Синнабон"], default = ["Азбука"])
fig, ax = plt.subplots(figsize = (5, 5))
districts.plot (ax = ax, color = 'Lightgrey')
for i in choice:
    if (i == "Кофемания"):
        azb.plot (ax = ax, color = 'Brown', markersize = 0.8)  
    if (i == "Азбука"): 
        mon.plot (ax = ax, color = 'Green', markersize = 0.8)
    if (i == "Синнабон"):    
        cnb.plot (ax = ax, color = 'Teal', markersize = 0.8)

st.pyplot(fig)

st.write ("На первый взгляд, кажется, что на западе, действительно, больше всего. Предлагаю построить логистические регрессии, чтобы убедиться в этом") 

"""
А дальше у меня несколько дней ничего не получалось. Извините :( на этом, я боюсь, все...
Имплементированы API, визуализацию, использование geopandas.
Небольшой имеющийся код на гитхабе здесь: https://github.com/bananagoat/project_public/blob/main/main.py
"""
