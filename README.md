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
│ └── IdentityVerification.vy # Vyper smart contract for identity logic
│
├── scripts/
│ ├── deploy_cont.py # Deploys contract to Ganache, saves config
│ └── manage_user.py # CLI for registration, verification & revocation
│
├── utils/
│ ├── init.py # Marks utils as a Python package
│ └── hash_utils.py # Generates SHA-256 hash for ID files
│
├── build/ # Auto-generated folder after deployment
│ └── IdentityVerification.json # ABI and Bytecode from Vyper compiler
│
├── data/
│ └── sample_id.txt # Example user document (for hashing demo)
│
├── config.json # Stores deployed contract address & owner info
├── venv/ # Python virtual environment folder
└── README.md # Project documentation
---

## ⚙️ Setup Instructions
Follow these steps to set up and run the project locally 👇

---

### 🧩 1️⃣ Clone the Repository

Clone the repository from GitHub:
```bash
git clone https://github.com/rohit112-cs/Blockchain-ID-Verification.git
cd Blockchain-ID-Verification

🧱 2️⃣ Create and Activate Virtual Environment
🪟 For Windows (PowerShell):
    python -m venv venv
    venv\Scripts\activate

📦 3️⃣ Install Required Dependencies

Install all Python libraries needed for running and deploying the project.

    pip install web3 vyper colorama hexbytes

🔗 4️⃣ Start Local Blockchain (Ganache)

Make sure Ganache is running and configured properly.

Open Ganache GUI or run Ganache CLI

Confirm that it’s using the default RPC endpoint:

http://127.0.0.1:8545

Ensure at least 10 pre-funded accounts are visible (Ganache default).

🚀 5️⃣ Deploy the Smart Contract

Compile and deploy the Vyper contract to your local blockchain.

python scripts/deploy_cont.py


✅ This script will:

Compile the smart contract using Vyper

Deploy it on the Ganache blockchain via Web3.py

Create:

   build/IdentityVerification.json → ABI & Bytecode
   config.json → Contract address & admin account

🧮 7️⃣ CLI Menu Options
Option	Description
1️⃣	Register a new user (stores document hash)
2️⃣	Verify a user (admin-only)
3️⃣	Check verification status
4️⃣	Revoke verification (admin-only)
5️⃣	Exit CLI


🧠 Example Workflow

1️⃣ Run Ganache
2️⃣ Deploy contract → python scripts/deploy_cont.py
3️⃣ Register a user → Choose option 1
4️⃣ Verify the same user → Choose option 2
5️⃣ Check status → Option 3
6️⃣ Revoke and re-register → Option 4 then 1


🧱 8️⃣ Folder Artifacts After Successful Setup

Blockchain-ID-Verification/
├── build/IdentityVerification.json   # Compiled contract ABI + bytecode
├── config.json                       # Contract address & admin info
├── contracts/                        # Vyper contract source
├── scripts/                          # Deployment & management scripts
├── utils/                            # Hashing functions
└── venv/                             # Virtual environment

🧩 9️⃣ Troubleshooting

Issue	Fix
ModuleNotFoundError: No module named 'web3'	Run pip install web3 inside your virtual environment
Cannot connect to Ganache	Make sure Ganache is running at http://127.0.0.1:8545
invalid opcode error	Redeploy the contract — delete build/ and config.json, then rerun deploy_cont.py
ModuleNotFoundError: No module named 'utils'	Ensure utils/__init__.py exists (even empty)

✅ Once all steps are done, your system will be ready to:

Register identities

Verify or revoke users

View verification status

Interact fully via blockchain on Ganache

## 👨‍💻 Team – The Solution Seekers  
**Team ID:** ISB-III-T033  

| Name | Role / Responsibility | Email |
|------|------------------------|--------|
| **Himanshi Negi** *(Team Lead)* | Smart Contract Deployment & Logic | [hnegiii15@gmail.com](mailto:hnegiii15@gmail.com) |
| **Rohit Pandey** | Hashing Implementation & Blockchain Integration | [iamrohitpandey2000@gmail.com](mailto:iamrohitpandey2000@gmail.com) |
| **Krish Joshi** | Web Portal Development (Python) | [joshikrish2606@gmail.com](mailto:joshikrish2606@gmail.com) |
| **Swayam Gupta** | System Testing & Validation | [gswayam971@gmail.com](mailto:gswayam971@gmail.com) |



📊 Project Progress

✅ Smart Contract Development – Completed
✅ Blockchain Integration (Web3.py) – Completed
⚙️ Frontend Portal – Under Development
📘 Testing & Documentation – In Progress