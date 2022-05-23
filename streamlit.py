
from web3 import Web3   
import streamlit as st
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import time


load_dotenv("_.env")

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

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

accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
wallet_balance_wei = w3.eth.getBalance(address)
wallet_balance_fan_token = int(wallet_balance_wei/100000000000000000)
st.write(f"Your wallet contains {wallet_balance_fan_token} FAN tokens." )

private_key = st.text_input("Your Private Key")


st.button("PURCHASE")
