import socket

s = socket.socket()
s.connect(('localhost', 8000))
print("Connected to server on port 8000.")

try:
    while True:
        ip = input("Enter the website you want to ping (or 'exit' to quit): ")
        if ip.lower() == 'exit':
            break
        s.send(ip.encode())
        response = s.recv(1024).decode()
        print(f"Server response:\n{response}")
finally:
    s.close()
    print("Connection closed.")
