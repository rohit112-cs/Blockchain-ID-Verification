# utils/hash_utils.py
import hashlib

def get_file_hash(file_path):
    """Return SHA-256 hash of a given file."""
    with open(file_path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

if _name_ == "_main_":
    print(get_file_hash("../data/sample_id.txt"))