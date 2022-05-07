import streamlit as st
import pandas as pd
import numpy as np
import time

st.title(" Welcome to the Fandom Cash Exchange: Building the Brand One Token at a Time!")

df = pd.read_csv("Resources/Fandom_items.csv", index_col = "item", parse_dates=True, infer_datetime_format = True)

def color_negative(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

df.sort_index(inplace=True, ascending = False)

start = st.selectbox("Select a Fan Experience item:", df.index)

st.table(df)


