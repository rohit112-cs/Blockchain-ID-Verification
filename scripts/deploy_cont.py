# scripts/deploy_cont.py
from web3 import Web3
import json
import os
import sys

# 1️⃣ Connect to local blockchain (Ganache)
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

if not w3.is_connected():
    print("❌ Unable to connect to Ganache. Check your blockchain node.")
    sys.exit(1)

print("✅ Connected to Ganache")

# 2️⃣ Load compiled contract JSON (ABI + bytecode)
build_path = os.path.join("build", "IdentityVerification.json")
if not os.path.exists(build_path):
    print(f"❌ Build file not found: {build_path}")
    sys.exit(1)

with open(build_path) as f:
    contract_data = json.load(f)

abi = contract_data.get("abi")
bytecode = contract_data.get("bytecode") or contract_data.get("bytecode_runtime")

if not abi or not bytecode:
    print("❌ ABI or bytecode missing in build file!")
    sys.exit(1)

# 3️⃣ Choose deployer account (Ganache first account)
deployer = w3.eth.accounts[0]
print(f"👤 Deploying from account: {deployer}")

# 4️⃣ Deploy contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)

print("⏳ Deploying contract...")
tx_hash = contract.constructor().transact({"from": deployer})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"✅ Contract deployed at: {tx_receipt.contractAddress}")

# 5️⃣ Save deployed contract info
config_path = os.path.join("config.json")
with open(config_path, "w") as f:
    json.dump({"contract_address": tx_receipt.contractAddress, "deployer": deployer}, f)

print(f"💾 Contract info saved to {config_path}")
