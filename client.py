import zmq

context = zmq.Context()

print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")


print(f"Requesting Quote…")
socket.send(b"Quote Request")

message = socket.recv()
message = message.decode()
print(f"Received Quote [ {message} ]")
