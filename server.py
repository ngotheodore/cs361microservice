import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv()
    print(f"Received request: {message}")

    time.sleep(1)

    socket.send(b"World")
