# scripts/verify_user.py
from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

with open("../config.json") as f:
    config = json.load(f)

with open("../build/IdentityVerification.json") as f:
    contract_data = json.load(f)

contract = w3.eth.contract(address=config["contract_address"], abi=contract_data["abi"])

admin = config["deployer"]
user = w3.eth.accounts[1]

tx_hash = contract.functions.verify_user(user).transact({"from": admin})
w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"✅ Admin verified user {user}")