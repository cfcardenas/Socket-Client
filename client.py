import socket

#Client Configuration
# This client connects to a server, sends messages, and receives responses.
# It handles connection errors and unexpected exceptions.

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Server port

def start_client():
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")

            
            while True:
                message = input("Enter message (type 'exit' to quit): ")

                if not message:
                    print("Empty message. Try again.")
                    continue

                
                s.sendall(message.encode())

                if message.lower() == "exit":
                    print("Disconnected from server.")
                    break

                
                data = s.recv(1024)
                if not data:
                    print("Server closed the connection.")
                    break

                print(f"Received from server: {data.decode()}")

    except ConnectionRefusedError:
        print(f"Connection failed: Server is not running at {HOST}:{PORT}")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    start_client()