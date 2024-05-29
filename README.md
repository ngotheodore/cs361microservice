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
![Sequence diagram 2](https://github.com/ngotheodore/cs361microservice/assets/83106444/9adcee48-8be8-4554-bf1b-dd72c2bc5cd0)

