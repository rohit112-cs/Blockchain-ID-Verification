from web3 import Web3
from vyper import compile_code
import json, os, pathlib

def main():
    ROOT = pathlib.Path(__file__).resolve().parents[1]
    BUILD_DIR = ROOT / "build"
    CONFIG_PATH = ROOT / "config.json"
    CONTRACT_PATH = ROOT / "contracts" / "IdentityVerification.vy"

    os.makedirs(BUILD_DIR, exist_ok=True)

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    assert w3.is_connected(), "❌ Failed to connect to Ganache"

    owner = w3.eth.accounts[0]
    print(f"Using owner: {owner}")

    
    with open(CONTRACT_PATH, "r") as f:
        source_code = f.read()

    compiled = compile_code(source_code, output_formats=["abi", "bytecode"])
    abi = compiled["abi"]
    bytecode = compiled["bytecode"]


    build_data = {"abi": abi, "bytecode": bytecode}
    with open(BUILD_DIR / "IdentityVerification.json", "w") as f:
        json.dump(build_data, f, indent=2)

    
    contract = w3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = contract.constructor().transact({"from": owner})
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    contract_address = tx_receipt.contractAddress

    print("✅ Contract deployed successfully!")
    print(f"📜 Contract Address: {contract_address}")

   
    config = {
        "provider": "http://127.0.0.1:8545",
        "deployer": owner,
        "contract_address": contract_address,
    }
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print("🧱 Build + config files saved.")

if __name__ == "__main__":
    main()
