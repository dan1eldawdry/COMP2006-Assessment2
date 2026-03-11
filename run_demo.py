import database
import server

print("server: requesting access to password vault")

challenge = database.generate_challenge # database sends challenge

response = server.work_out_response(challenge) # server works out response

database.verify_response(challenge, response) # database verifies
