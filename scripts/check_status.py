# scripts/check_status.py
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

with open("../config.json") as f:
    config = json.load(f)

with open("../build/IdentityVerification.json") as f:
    contract_data = json.load(f)

contract = w3.eth.contract(address=config["contract_address"], abi=contract_data["abi"])

user = w3.eth.accounts[1]
status = contract.functions.is_verified(user).call()
print(f"🔎 User {user} verified status: {status}")