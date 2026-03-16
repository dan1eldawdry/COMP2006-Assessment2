import hashlib
import secrets

class PasswordVaultDatabase:
    def __init__(self, shared_secret):
        self.shared_secret = shared_secret

    def generate_challenge(self):
        challenge = secrets.token_hex(16)
        print("\n[Database] generated chllenge: ", challenge)
        return challenge
    
    def verify_server(self, challenge, server_hash):
        data = challenge + self.shared_secret
        expected_hash = hashlib.sha256(data.encode()).hexdigest()

        print("[Database] expected hash: ", expected_hash)
        print("[Database] recieved hash: ", server_hash)

        if expected_hash == server_hash:
            print("[Database] authentication success. server allowed access\n")
            return True
        else:
            print("[Database] authentication failed. access denied\n")
            return False
