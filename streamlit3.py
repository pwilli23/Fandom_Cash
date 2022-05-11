
from web3 import Web3   
import streamlit as st
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import time

load_dotenv("_.env")

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

from crypto_wallet import generate_account, get_balance, send_transaction


item_database = {
    "Signed Basketball": ["Signed Basketball",100 , "Images/basketball.jpeg"],
    "Season Tickets": ["Season Tickets", 500, "Images/tickets.jpng"],
    "Signed Jacket": ["Signed Jacket", 100, "Images/Jacket.jpeg"],
    "Signed Hoodie": ["Signed Hoodie", 150, "Images/hoodie.jpeg"],
    "Vote": ["Vote", 100, "Images/tickets.jpng"],
    "Topshots NFT": ["Topshots NFT", 100, "Images/kendall.jpeg"],
    "Playercard NFT": ["Playercard NFT", 100, "Images/kendall.jpeg"]
}


items = ["Signed Basketball", "Season Tickets", "Signed Jacket", "Signed Hoodie", "Vote", "Topshots NFT", "Playercard NFT"]

def get_items(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(item_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Fandom Cash Items", db_list[number][0])
        st.write("Price Per Fandom Item: ", db_list[number][3], "eth")
        st.text(" \n")
        
# Streamlit application headings



################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Fandom Cash Rewards Marketplace")



#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3,account.address))

##########################################

# Create a select box to chose a FinTech Hire candidate
select_item = st.sidebar.selectbox('Select a Item', items)

# Create a input field to record the number of hours the candidate worked
quantity = st.sidebar.number_input("Quantity")

st.sidebar.markdown("## Buy Your Fandom Cash Items Here!")

# Identify the FinTech Hire candidate
selected_item = item_database[select_item][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(selected_item)

# Identify the FinTech Finder candidate's hourly rate
price = item_database[select_item][1]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(price)


# Write the Fintech Finder candidate's name to the sidebar



# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
total = item_database[select_item][1]* quantity

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.
st.sidebar.write('The Items You Have Selected Cost:')
st.sidebar.write(total)


# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page


st.title(" Welcome to the Fandom Cash Marketplace: Building the Brand One Token at a Time")


df = pd.read_csv("Resources/Fandom_items.csv", index_col = "item", parse_dates=True, infer_datetime_format = True)

def color_negative(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

df.sort_index(inplace=True, ascending = False)

start = st.selectbox("Select a Fan Experience item:", df.index)

st.table(df)

accounts = w3.eth.accounts
address = st.sidebar.selectbox("Select Account", options=accounts)
wallet_balance_wei = w3.eth.getBalance(address)
wallet_balance_fan_token = int(wallet_balance_wei/100000000000000000)
st.sidebar.write(f"Your wallet contains {wallet_balance_fan_token} FAN tokens." )

private_key = st.sidebar.text_input("Your Private Key")


st.sidebar.button("PURCHASE")
