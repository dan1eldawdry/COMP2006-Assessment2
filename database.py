import hashlib
import secrets

SHARED_SECRET = "secret_key" # the shared secret stored in both server and database

def generate_challenge():
    challenge = secrets.token_hex(16)
    print("database: generated challenge", challenge)
    return challenge

def verify_response(challenge, server_hash):
    data = challenge + SHARED_SECRET
    expected_hash = hashlib.sha256(data.encode()).hexdigest()
    print("database: expected hash: ", expected_hash)
    print("database: recieved hash: ", server_hash)

    if expected_hash == server_hash:
        print("database: authentication SUCCESS")
        return True
    else:
        print("database: authentication FAILED")
        return False