from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.Wallet_model import Wallet

all_coins = {'BTC','ETH','LTC','BNB','USDT','XRP'}

class get_wallet(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
	def get(self):
		data=self.parser.parse_args()
		email=data['email']
		wallet, code = Wallet.get_wallet(email)
		if wallet is None:
			return {"error":"User doesn't exist"}, 400
		else:
			return {
				'email':wallet.email,
				'balance': wallet.balance,
				'fixed_balance': wallet.fixed_balance
			}, 200


class get_wallet_currency(Resource):
	parser=reqparse.RequestParser()
	parser.add_argument('email',type=str,required=True)
	
	def get(self, coin):
		data=self.parser.parse_args()
		email=data['email']
		if coin not in all_coins:
			return {
				'error':"Invalid coin"
			}, 400
		balance, fixed_balance, code = Wallet.get_wallet_currency(email, coin)
		if balance is None:
			return {"error":"User doesn't exist"},400
		else:
			return {
				'coin': coin,
				'balance': balance,
				'fixed_balance': fixed_balance

			},200
