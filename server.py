from src.http_server import HTTPServer 
import sys 

host = sys.argv[1]
port = int(sys.argv[2])

server = HTTPServer(host, port) 
server.start()