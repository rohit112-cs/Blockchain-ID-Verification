from web3 import Web3
from colorama import Fore, init
from hexbytes import HexBytes
from pathlib import Path
import json
from utils.hash_utils import get_file_hash

init(autoreset=True)

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config.json"
BUILD = ROOT / "build" / "IdentityVerification.json"

def load_contract(w3):
    with open(CONFIG) as f:
        cfg = json.load(f)
    with open(BUILD) as f:
        build = json.load(f)
    address = cfg["contract_address"]
    abi = build["abi"]
    return w3.eth.contract(address=address, abi=abi)

def register_user(w3, contract):
    user = w3.eth.accounts[1]  
    doc_path = ROOT / "data" / "sample_id.txt"
    doc_hash_hex = get_file_hash(str(doc_path))
    doc_hash_bytes32 = HexBytes("0x" + doc_hash_hex)

    if len(doc_hash_bytes32) != 32:
        raise ValueError("Hash must be 32 bytes!")

    tx = contract.functions.register_user(doc_hash_bytes32).transact({"from": user})
    w3.eth.wait_for_transaction_receipt(tx)
    print(Fore.GREEN + f"✅ Registered user: {user}")
    print(Fore.YELLOW + f"🧾 Hash: {doc_hash_hex}")

def verify_user(w3, contract):
    admin = w3.eth.accounts[0]
    user = w3.eth.accounts[1]
    tx = contract.functions.verify_user(user).transact({"from": admin})
    w3.eth.wait_for_transaction_receipt(tx)
    print(Fore.GREEN + f"✅ Verified user: {user}")

def check_status(w3, contract):
    user = w3.eth.accounts[1]
    verified = contract.functions.is_verified(user).call()
    if verified:
        print(Fore.GREEN + f"✅ User {user} is VERIFIED")
    else:
        print(Fore.RED + f"❌ User {user} is NOT verified")

def revoke_user(w3, contract):
    admin = w3.eth.accounts[0]
    user = w3.eth.accounts[1]
    tx = contract.functions.revoke_verification(user).transact({"from": admin})
    w3.eth.wait_for_transaction_receipt(tx)
    print(Fore.YELLOW + f"🚫 Verification revoked and registration cleared for: {user}")


def main():
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    assert w3.is_connected(), "❌ Ganache not connected"
    contract = load_contract(w3)

    while True:
        print(Fore.CYAN + "\n=== Blockchain ID Verification CLI ===")
        print(" 1️⃣ Register user")
        print(" 2️⃣ Verify user")
        print(" 3️⃣ Check user status")
        print(" 4️⃣ Revoke verification")
        print(" 5️⃣ Exit")

        choice = input("👉 Enter choice (1/2/3/4/5): ").strip()
        try:
            if choice == "1":
                register_user(w3, contract)
            elif choice == "2":
                verify_user(w3, contract)
            elif choice == "3":
                check_status(w3, contract)
            elif choice == "4":
                revoke_user(w3, contract)
            elif choice == "5":
                print("👋 Exiting...")
                break
            else:
                print("⚠️ Invalid option.")
        except Exception as e:
            print(Fore.RED + f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
