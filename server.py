import time
import zmq
import random

quote_list = ["A goal is a wish. A standard holds you accountable. —Tunde Oyeneyin", 
              "Some people want it to happen, some wish it would happen, others make it happen. —Michael Jordan",
              "You just can’t beat the person who never gives up. —Babe Ruth",
              "You’ve survived 100 percent of your worst days. —Robin Arzón",
              "Today I will do what others won’t, so tomorrow I can accomplish what others can’t. —Jerry Rice",
              "If something stands between you and your success, move it. —Dwayne “The Rock” Johnson",
              "The hardest part is over. You showed up. —Jess Sims",
              "Allow yourself the opportunity to get uncomfortable. —Alex Toussaint",
              "Everyone's dream can come true if you just stick to it and work hard. —Serena Williams",
              "The vision of a champion is bent over, drenched in sweat, at the point of exhaustion, when nobody else is looking. —Mia Hamm"]
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

while True:
    message = socket.recv()
    print(f"Received request: {message}")

    time.sleep(1)

    quote = random.choice(quote_list)
    socket.send((quote))
