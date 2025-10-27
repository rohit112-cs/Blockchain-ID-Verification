# SPDX-License-Identifier: MIT
# @version ^0.4.3

owner: public(address)
user_hashes: public(HashMap[address, bytes32])
verified: public(HashMap[address, bool])

@deploy
def __init__():
    self.owner = msg.sender

@external
def register_user(user_hash: bytes32):
    assert self.user_hashes[msg.sender] == empty(bytes32), "User already registered"
    self.user_hashes[msg.sender] = user_hash
    self.verified[msg.sender] = False

@external
def verify_user(user: address):
    assert msg.sender == self.owner, "Only owner can verify"
    assert self.user_hashes[user] != empty(bytes32), "User not registered"
    self.verified[user] = True

@external
def revoke_verification(user: address):
    assert msg.sender == self.owner, "Only owner can revoke"
    
    self.user_hashes[user] = empty(bytes32)
    self.verified[user] = False

@view
@external
def get_user_hash(user: address) -> bytes32:
    return self.user_hashes[user]

@view
@external
def is_verified(user: address) -> bool:
    return self.verified[user]
