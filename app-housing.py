import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990) by Eric')

df = pd.read_csv('housing.csv')

# add a slider

house_price_filter = st.slider('Median House Price', 0, 500001, 200000)

# add a capital multi select

location_filter = st.sidebar.multiselect('Choose the location type', df.ocean_proximity.unique(), df.ocean_proximity.unique())

# create a  radio button selection to diversify income

income_filter = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

# filter by house price

df = df[df.median_house_value <= house_price_filter]

# filter by location

df = df[df.ocean_proximity.isin(location_filter)]

# filter by income

if income_filter is None:
    pass
elif income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income < 4.5) & (df.median_income > 2.5)]
else:
    df = df[df.median_income > 4.5]

# show data on map
st.subheader('See more filters in the sidebar:')
st.map(df)

# show median house value by index
st.subheader('Histogram of the Median House Value')
fig, ax =  plt.subplots()
median_house_price = df.median_house_value
median_house_price.hist(ax=ax, bins=30)
st.pyplot(fig)

