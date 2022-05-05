import streamlit as st
import pandas as pd
import numpy as np
import time
import sqlalchemy as sql
from datetime import datetime

@st.cache(allow_output_mutation=True)
def setup(): 
    connection_url='sqlite:///Resources/market.db'
    engine=sql.create_engine(connection_url)
    return engine

engine=setup()

df=pd.read_sql('select * from items', con=engine)
# st.write(df)

st.title(" Welcome to the Fandom Cash Exchange: Building the Brand One Token at a Time!")

# df = pd.read_csv("Fandom_items.csv", index_col = "item", parse_dates=True, infer_datetime_format = True)

def color_negative(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

# df.sort_index(inplace=True, ascending = False)

start = st.selectbox("Select a Fan Experience item:", df.index)

st.table(df)

if st.button('Purchase'): 
    now = datetime.now()
    current_time = now.strftime("%y-%m-%d@%H:%M:%S")
    # update database
    query_string=f"""
    insert into transactions
    values ('Kevin', 'Card', '{current_time}')
    """
    # print(query_string)
    engine.execute(query_string)
