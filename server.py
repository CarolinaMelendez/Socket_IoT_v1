#----- A simple TCP based server program in Python using send() function -----   
  
import socket   
import time
from tkinter import Message 

LED_WHITE = "13"
LED_BLUE = "12"
LED_YELLOW = "14"

def action_on_Led(led_color,action,clientConnected):
    led_pin = 0
    if led_color == "white":
        led_pin = LED_WHITE
    elif led_color == "blue":
        led_pin = LED_BLUE
    elif led_color == "yellow":
        led_pin = LED_YELLOW
    
    if action == "turn off":
        led_pin+="0"
    elif action == "turn on":
        led_pin+="1"
    message = "LED " + led_pin
    clientConnected.send(message.encode())  

def ask_distance(clientConnected):
    message = "DISTANCE"
    clientConnected.send(message.encode())
    dataFromClient = clientConnected.recv(1024)    
    distance = dataFromClient.decode() 
    print("Distance = " + distance)
    return distance

def action_on_Led_distance(clientConnected):
    client_answer = ask_distance (clientConnected)
    time.sleep(5)
    if (client_answer): 
        distance = int(client_answer) 
        if(distance <=  10): 
            action_on_Led_dist = False 
        else: 
            action_on_Led_dist = True   
        if(action_on_Led_dist): 
            print("You have to turn on White Led") 
            num_port = str(131)  
        else: 
            print("You have to turn off White Led") 
            num_port = str(130) 
        #Send data to client
        message = "LED " + num_port
        clientConnected.send(message.encode())

def create_server ():
    ini_time = time.time()
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);   
    
    # Bind and listen   
    serverSocket.bind(("192.168.0.111",10000));   
    serverSocket.listen();   
    
    # Accept connections  
    (clientConnected, clientAddress) = serverSocket.accept();   
    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
    print("Time passed in setting conecction " ,   (time.time()- ini_time)*1000)
    return clientConnected