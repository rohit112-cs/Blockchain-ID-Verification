# IdentityVerification.vy
# Vyper smart contract for identity registration and verification

owner: public(address)
verified_users: public(HashMap[address, bool])
user_hashes: public(HashMap[address, bytes32])

@deploy
def __init__():
    self.owner = msg.sender

@external
def register_identity(doc_hash: bytes32):
    assert self.user_hashes[msg.sender] == empty(bytes32), "User already registered"
    self.user_hashes[msg.sender] = doc_hash

@external
def verify_user(user: address):
    assert msg.sender == self.owner, "Only admin can verify"
    self.verified_users[user] = True

@external
def revoke_verification(user: address):
    assert msg.sender == self.owner, "Only admin can revoke"
    self.verified_users[user] = False

@view
@external
def is_verified(user: address) -> bool:
    return self.verified_users[user]
