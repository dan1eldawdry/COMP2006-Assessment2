import hashlib

class BackendServer:
    def __init__(self, shared_secret):
        self.shared_secret = shared_secret

    def respond_to_challenge(self, challenge):
        data = challenge + self.shared_secret
        response_hash = hashlib.sha256(data.encode()).hexdigest()

        print("[Server] worked out response hash: ", response_hash)

        return response_hash