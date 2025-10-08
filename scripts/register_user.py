# scripts/register_user.py
from web3 import Web3
import json
from utils.hash_utils import get_file_hash

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

# Load config
with open("../config.json") as f:
    config = json.load(f)

# Load contract ABI
with open("../build/IdentityVerification.json") as f:
    contract_data = json.load(f)

contract = w3.eth.contract(address=config["contract_address"], abi=contract_data["abi"])

# User registers ID hash
user = w3.eth.accounts[1]
doc_hash = get_file_hash("../data/sample_id.txt")

tx_hash = contract.functions.register_identity(bytes.fromhex(doc_hash)).transact({"from": user})
w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"✅ {user} registered with hash {doc_hash}")