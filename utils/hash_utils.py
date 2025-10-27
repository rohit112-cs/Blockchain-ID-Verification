# utils/hash_utils.py
import hashlib

def get_file_hash(file_path: str) -> str:
    with open(file_path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()

if __name__ == "__main__":
    print(get_file_hash("data/sample_id.txt"))
