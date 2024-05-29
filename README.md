# cs361microservice
Sends a request and returns inspirational exercise quotes

How to use the program:

    Request:

    In order to request data, the user needs to send a request to the server program through a socket with the socket.send() command, found in line 11 of client.py.

    socket.send(b"Quote Request")

    Receive:

    In order to receive data, the user needs to receive the request from the server program through the socket.recv() command, found in line 13 of client.py.

    socket.recv()

Diagram:
![Sequence_diagram](https://github.com/ngotheodore/cs361microservice/assets/83106444/bb2ee709-2eca-4537-b705-96baf7660e22)
