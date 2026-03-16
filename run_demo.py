from database import PasswordVaultDatabase
from server import BackendServer

SHARED_SECRET = "secret_shared_key"

database = PasswordVaultDatabase(SHARED_SECRET)
server = BackendServer(SHARED_SECRET)

print("==SERVER AUTHENTICATION DEMO==")

print("\n[Server] requesting authentication with password vault") # server requests database access
challenge = database.generate_challenge() # database sends challenge
response = server.respond_to_challenge(challenge) # server works out response
database.verify_server(challenge, response)

print("==FAILED AUTH EXAMPLE==")
fake_server = BackendServer("wrong_secret")
challenge = database.generate_challenge()
fake_response = fake_server.respond_to_challenge(challenge)
database.verify_server(challenge, fake_response)
