from flask import Flask, request, redirect
import fandom

app=Flask(__name__)

@app.route('/')
def home(): 
	instructions="""
	use /reward_token \n
	or \n
	use /reward_token?recipient_add=[recipient_address]
	"""
	return instructions

@app.route('/reward_token')
def mint_sharks():
	args=request.args
	recipient_add=args['recipient_add']
	txn_hash=fandom.reward_token(recipient_add)
	# return f'Token Hash {txn_hash}'
	return redirect("/")

# @app.route('/lakers')
# def mint_lakers():
# 	# call mint function with web3
# 	# contract=web3.contract.....
# 	# contract.functions.mint().call()
# 	return 'Thanks for interacting with Lakers'

if __name__=='__main__': 
	app.run()