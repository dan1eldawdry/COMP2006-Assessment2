import hashlib

SHARED_SECRET = "secret_key" # same shared secret stored on server

def work_out_response(challenge):
    data = challenge + SHARED_SECRET
    response_hash = hashlib.sha256(data.encode()).hexdigest()
    print("server: worked out response hash: ", response_hash)
    return response_hash