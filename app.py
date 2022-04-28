from flask import Flask

app=Flask(__name__)

@app.route('/sharks')
def mint_sharks():
	# call mint function with web3
	# contract=web3.contract.....
	# contract.functions.mint().call()
	return 'Thanks for interacting with Sharks'

@app.route('/lakers')
def mint_lakers():
	# call mint function with web3
	# contract=web3.contract.....
	# contract.functions.mint().call()
	return 'Thanks for interacting with Lakers'

if __name__=='__main__': 
	app.run()