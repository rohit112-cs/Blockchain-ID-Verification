# 🧾 Blockchain-Based Identity Verification System (Vyper + Web3.py)

A decentralized **Identity Verification System** leveraging **blockchain technology** to ensure secure, transparent, and tamper-proof identity verification using **Vyper smart contracts** and **Python (Web3.py)**.  
This project was developed as part of the **Phase 2 & 3 Academic Project** by **The Solution Seekers (Team ID: ISB-III-T033)**.

---

## 🧠 Project Abstract

In traditional systems, identity verification often suffers from privacy risks, data tampering, and centralized control.  
This project introduces a **blockchain-based decentralized identity verification system** that securely registers, verifies, and revokes user identities on an **Ethereum-like blockchain**.

Each user’s identity document is hashed using **SHA-256** and stored on the blockchain through a **Vyper smart contract**.  
Only the contract owner (admin) has the authority to verify or revoke a user’s verification status, ensuring authenticity and privacy.  
Python scripts built using **Web3.py** provide an easy-to-use CLI for interaction with the deployed contract on a **local Ganache blockchain**.

This system demonstrates how blockchain can eliminate third-party intermediaries and provide a **transparent and immutable** record of identity validation.

---

## 🚀 Features

✅ **Secure Registration** – Register user identity as a unique SHA-256 hash.  
✅ **Admin Verification** – Only contract owner can verify/revoke identities.  
✅ **Revoke Access** – Revoke a verified user and allow re-registration.  
✅ **CLI Interface** – Manage users directly from command-line interface.  
✅ **Ganache Local Blockchain** – Quick local deployment and testing.  

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Smart Contract** | Vyper (`v0.4.3`) |
| **Blockchain** | Ganache (Ethereum Local Network) |
| **Programming Language** | Python 3.12 |
| **Libraries Used** | Web3.py, Colorama, Hexbytes |
| **Hashing Algorithm** | SHA-256 |
| **IDE Used** | VS Code |

---

## 🏗️ Project Structure

Blockchain-ID-Verification/
│
├── contracts/
│ └── IdentityVerification.vy # Vyper smart contract
│
├── scripts/
│ ├── deploy_cont.py # Deploys contract to Ganache
│ └── manage_user.py # CLI for registration & verification
│
├── utils/
│ ├── init.py
│ └── hash_utils.py # File hashing function
│
├── build/ # ABI & Bytecode generated on deployment
├── config.json # Contract metadata (address, owner)
├── venv/ # Virtual environment
└── README.md # Documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/rohit112-cs/Blockchain-ID-Verification.git
cd Blockchain-ID-Verification
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
# On Windows (PowerShell)
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install web3 vyper colorama hexbytes
4️⃣ Start Local Blockchain (Ganache)
Ensure Ganache is running on:

cpp
Copy code
http://127.0.0.1:8545
🧱 Deploy Smart Contract
Compile and deploy the contract to Ganache:

bash
Copy code
python scripts/deploy_cont.py
The deployed contract address will be saved automatically in config.json.

ABI and Bytecode will be stored in the build/ directory.

💻 CLI Interface – Manage Users
Run the CLI tool:

bash
Copy code
python scripts/manage_user.py
Menu Options
Option	Action
1️⃣	Register a User
2️⃣	Verify a User
3️⃣	Check User Status
4️⃣	Revoke Verification
5️⃣	Exit

🔐 Smart Contract Overview
python
Copy code
@external
def register_user(user_hash: bytes32):
    assert self.user_hashes[msg.sender] == empty(bytes32), "User already registered"
    self.user_hashes[msg.sender] = user_hash
    self.verified[msg.sender] = False
verify_user() → Admin-only function to mark a user as verified.

revoke_verification() → Admin-only function to reset verification status.

get_user_hash() / is_verified() → View user’s hash & verification status.

🧩 Future Enhancements
🔗 Deploy contract on Ethereum Testnet (Sepolia or Goerli)
🌐 Develop a web-based front-end with MetaMask integration
📦 Use IPFS for decentralized storage of documents
🧰 Add multi-user access control and logging

👨‍💻 Team – The Solution Seekers (Team ID: ISB-III-T033)
Name	Role	Email
Himanshi Negi (Team Lead)	Smart Contract Deployment & Logic	hnegiii15@gmail.com
Rohit Pandey	Hashing Implementation & Blockchain Integration	iamrohitpandey2000@gmail.com
Krish Joshi	Web Portal Development (Python)	joshikrish2606@gmail.com
Swayam Gupta	System Testing & Validation	gswayam971@gmail.com

📊 Project Progress
✅ Smart Contract Development – Completed
✅ Blockchain Integration (Web3.py) – Completed
⚙️ Frontend Portal – Under Development
📘 Testing & Documentation – In Progress

📜 License
This project is licensed under the MIT License.

🌐 Repository
🔗 GitHub – rohit112-cs/Blockchain-ID-Verification