
   
import streamlit as st
import pandas as pd
import numpy as np
import time



# Using "with" notation
with st.sidebar:

    st.image("images/coins.jpeg")

    budget = st.slider('How much do you have?', 
    min_value=0, max_value=1000)

with st.sidebar:  


        if budget in range(500,1001):
            st.image('images/tickets.png')

        if budget in range(300,1001):
            st.image('images/jacket.jpeg')     

        if budget in range(150,1001):
            st.image('images/basketball.jpeg') 

        if budget in range(100,1001):
            st.image('images/hoodie.jpeg') 
      
    


st.title(" Welcome to the Fandom Cash Marketplace")

df = pd.read_csv("Resources/Fandom_items.csv", index_col = "item", parse_dates=True, infer_datetime_format = True)

def color_negative(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

df.sort_index(inplace=True, ascending = False)

start = st.selectbox("Select a Fan Experience item:", df.index)

st.table(df)

title = st.text_input('Please enter your wallet address.', 'Life of Brian')
st.write('Please confirm your address', title)


