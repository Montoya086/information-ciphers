import socket
import sys
# tcp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind to all interfaces on port 9876
server_address = ('0.0.0.0', 9876)
server_socket.bind(server_address)

#start listening for connections
server_socket.listen(1)

print('Waiting for connections on {}:{}'.format(*server_address))

while True:
    try:
        connection, client_address = server_socket.accept()
        try:
            while True:
                data = connection.recv(1024)
                if data:
                    print('Received: {!r}'.format(data), "from", client_address)
                else:
                    print('No more data from', client_address)
                    break
                
        except socket.error as e:
            print(f"Socket error: {e}")
        finally:
            print('Closing connection with', client_address)
            connection.close()
            
    except KeyboardInterrupt:
        print("\nClosing server...")
        server_socket.close()
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}") 