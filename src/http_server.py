#
# HTTP SERVER
# 
import socket

class HTTPServer:
    
    def __init__(self, host, port): 
        
        # Server Address #
        self.host = host 
        self.port = port

        # Server Object # 
        self.server = None

    def start(self):
        self.instantiate()
        self.bind()
        self.listen()

    def instantiate(self):
        print("@HTTPServer : Creating instance.")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def bind(self): 
        host = self.host 
        port = self.port
        print(f"@HTTPServer : Binding instance to {host}:{port}")
        self.server.bind((host, port)) 
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    def listen(self): 
        host = self.host 
        port = self.port
        print(f"@HTTPServer : Starting listener...") 
        self.server.listen(1)
        print(f"@HTTPServer : Listening on {host}:{port}")
        self.handle_connections()

    def handle_connections(self):
        # Accept Many Connections Successively
        while True: 
            # Accept Incoming Connection
            client_conn, client_addr = self.server.accept() 
            self.handle_connection(client_conn, client_addr)

    def handle_connection(self, client_conn, client_addr): 
        # Get the Client Request 
        request = client_conn.recv(1234).decode() 
        print("<=== Received:")
        print(request) 

        # Send HTTP Response # 
        response = "HTTP/1.0 200 OK\nContent-Type:text/html\n\n" + content
        client_conn.sendall(response.encode())
        client_conn.close() 

    def close(self):
        print("@HTTPServer: Closing socket...")
        self.server.close()
        print("@HTTPServer: Successfully closed socket.")
        




    