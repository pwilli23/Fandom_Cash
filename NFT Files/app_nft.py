import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
import time

# from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json

load_dotenv("SAMPLE.env")

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
print(w3)

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/abi_json_nft.txt')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

def toggle_minting(status):
    tx_hash = contract.functions.toggleIsMintEnabled(status
    ).transact({'from': accounts[0], 'gas': 1000000})
    
    return tx_hash

contract = load_contract()

st.title("Fandom Super Pass NFT Mint")
st.write("Choose an account to get started")
accounts = w3.eth.accounts
address = st.selectbox("Select Account", options=accounts)
st.markdown("---")

st.sidebar.image('https://gateway.pinata.cloud/ipfs/QmdtM8P5334BWYr1t9TGC1RXRch61UkZs2zu7HZQQyAENf')

mint_price_wei = contract.functions.mintPrice().call()
mint_price_ether = w3.fromWei(mint_price_wei, 'ether')
st.write(f"The current price for a Fandom Super Pass is {mint_price_ether} ether.")

st.markdown("#### To purchase a Fandom Super Pass, please make sure your wallet account is selected above. Then enter the correct number of Super Passes to purchase, and click 'MINT'. Your transaction receipts will print below")

####################
# MINTING FUNCTION #
####################

# Convert 
#value_ether = st.number_input("Ether to send", value=0.1)
#value_wei = w3.toWei(value_ether, 'ether')

# Slider for number of NFT's to purchase - max is 10 per wallet
quantity_purchase = st.slider("Number of Super Pass NFT's to purchase:",min_value=1, max_value=10, step=1)

# Calculate the total purchase based on quantity and mint price
total_purchase_eth = quantity_purchase * mint_price_ether

# Confirm total purchase with output to user 
st.write(f"Your total for {quantity_purchase} Super Pass NFT is {total_purchase_eth} ETH.")

# Hitting the 'MINT' button will call the mint function
if st.button("MINT"):
    for i in range(1,quantity_purchase+1):
        tx_hash = contract.functions.mint().transact({'from':address, 'gas':1000000, 'value': mint_price_wei})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.success(f"Transaction receipt mined for Super Pass #{i}:")
        st.write(dict(receipt))
        time.sleep(4)
        st.balloons()

# Options available only to owner to make changes in Sidebar
st.sidebar.markdown("#### Settings that can be changed by contract owner only:")

# Load the contract
with st.sidebar:
    with st.spinner("Loading Smart Contract info..."):
        time.sleep(2)
        #contract = load_contract()
    
        # Include radio buttons to Enable or Disable the Minting function
        enabled = st.radio("Select Minting status:", ('Enabled', 'Disabled'), index=1)
        
        if enabled == 'Enabled':
            tx_hash = toggle_minting(True)
            #st.write("Minting Enabled.")
        else:
            tx_hash = toggle_minting(False)
            #st.write("Minting Disabled")


# Call the totalSupply function from the Smart Contract
current_supply = contract.functions.totalSupply().call()

# Display the total supply (minted) NFT's.
st.sidebar.write(f"The current minted supply is {current_supply}.")

new_max_supply = st.sidebar.number_input("Enter a number to change the Maximum Supply:", step=1, min_value=current_supply)
if st.sidebar.button("Update Max Supply"):
    contract.functions.setMaxSupply(new_max_supply
    ).transact({'from':accounts[0], 'gas': 1000000})
    
max_supply = contract.functions.maxSupply().call()
st.sidebar.write(f"The maximum supply is set at {max_supply} tokens.")
