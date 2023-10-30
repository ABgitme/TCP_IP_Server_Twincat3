# Import the socket module.
import socket

# Create a socket object.
s = socket.socket()

# Define the server's IP address and port number.
host = '127.0.0.1' 
port = 2000

# Connect to the server.
s.connect((host, port))

print("Connection established")

# Get the user's input for the mode they want to use.
mode = str(input('Enter 1 to see Bit-0 Status.\nEnter 2 to see 100ms data packet.\n'))

# Define a function to get the Bit-0 status from the server.
def Bit_Status():
    # Send the "BIT-0" command to the server.
    s.send('BIT-0'.encode('utf8'))
    
    # Receive the response from the server.
    dataOut = s.recv(1024)
    
    # Decode the response and print it to the console.
    print(dataOut.decode('utf8'))
   
while(1):

 if mode == '1':
     for i in range(30):
         Bit_Status()
     break

   

      	
	
	