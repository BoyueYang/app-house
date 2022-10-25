import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

st.title('California Housing data(1990) by Boyue Yang')
house = pd.read_csv('housing.csv')
median_price = house['median_house_value']

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Median house price (Millions):', 0, 500001, 200000)  # min, max, default

proximity_filter = st.sidebar.multiselect(
     'choose the location type',
     house['ocean_proximity'].unique(),   #option
     house['ocean_proximity'].unique())   #default

ratio = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if ratio == "Low":
    house = house[house.median_income < 2.5]
elif ratio == 'High':
    house = house[house.median_income > 4.5]
else:
    house[(house.median_income < 4.5 ) & (house.median_income>2.5)]

# filter by population
house = house[house.median_house_value <= price_filter]

# filter by capital
df = house[house.ocean_proximity.isin(proximity_filter)]

st.map(house)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(40, 20))
sns.histplot(house['median_house_value'], bins = 30,color = [0,0,0.9])
st.pyplot(fig)