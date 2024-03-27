import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles.csv')

st.title("Vehicles Data Explorer")

hist_button = st.button('Create a Histogram')

if hist_button:
    st.write('Price histogram by types.')
    # Creating a histogram with plotly.express to analyze the price by car types.
    fig1 = px.histogram(df, x='price', color='type', nbins=40, title='Prices by Types',
                   color_discrete_map={'SUV': 'green', 'truck': 'red', 'sedan': 'deepskyblue', 'pickup': 'yellow', 'coupe': 'chocolate', 
                                      'wagon': 'cyan', 'mini-van': 'lightblue', 'hatchback': 'turquoise', 'van': 'springgreen', 
                                      'convertible': 'lime', 'other': 'goldenrod', 'offroad': 'violet', 'bus': 'purple'})
    st.plotly_chart(fig1, use_container_width=True)

scatter_button = st.button('Create a Scatter Plot')

if scatter_button:
    st.write('Scatterplot of mileage by model year.')
    # Creating a scatterplot to analyze mileage and condition by model year.
    fig2 = px.scatter(df, x='model_year', y='odometer', title='Odometer by Model Year', color='condition', 
                 color_discrete_map={'good': 'green', 'like new': 'deepskyblue', 'fair': 'crimson', 'excellent': 'goldenrod', 
                                     'salvage': 'red', 'new': 'mediumseagreen'})
    st.plotly_chart(fig2, use_container_width=True)

check_types = df['type'].unique().tolist()
selected_types = [type for type in check_types if st.sidebar.checkbox(type)]
df_types = df[df['type'].isin(selected_types)]

if selected_types:
    fig = px.histogram(df_types, x='type', title='Number of Cars by Type')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write('Select a car type in the bar on the left to generate a count.')
