# cs361microservice
Sends a request and returns inspirational exercise quotes

How to use the program:

1. Execute the client program, then the server program in that order.
2. Prompt the client program to execute.
    Request:
3. The code in main() will execute, sending a request to server.py through a socket.
    The code to request a quote is: 
    socket.send(b"Quote Request")
4. The server.py program will receive the request from the client.py program through a socket.
    Receive:
5. After a delay in the server.py program, the program will select a random quote from the quote list and send it back to client.py through a socket.

Diagram:
![Sequence_diagram](https://github.com/ngotheodore/cs361microservice/assets/83106444/bb2ee709-2eca-4537-b705-96baf7660e22)
