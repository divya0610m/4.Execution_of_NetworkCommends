import socket
from pythonping import ping

s = socket.socket()
s.bind(('localhost', 8000))  # Fix: comma was missing
s.listen(5)
print("Server listening on port 8000...")

c, addr = s.accept()
print(f"Connection from {addr}")

while True:
    hostname = c.recv(1024).decode()
    if not hostname: 
        break
    try:
        response = ping(hostname, verbose=False)
        c.send(str(response).encode())
    except Exception as e:  
        c.send(f"Error: {e}".encode())