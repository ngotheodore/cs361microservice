import zmq

context = zmq.Context()

print("Connecting to server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")

def main():
    print(f"Requesting Quote…")
    socket.send(b"Quote Request")

    message = socket.recv()
    message = message.decode()
    print(f"Received Quote [ {message} ]")

while True:
    choice = input("Press 1 to request a quote. Press 2 to quit")
    if choice == "1":
        main()
    elif choice == "2":
        break
    else:
        print("Invalid input")