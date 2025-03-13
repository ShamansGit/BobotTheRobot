#Code for handling setting up a local LAN server and networking etc.
#Being worked on by: Joe

from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

#0.0.0.0 will make the website available for anyone on the local network on port 80
#note: non-standard ports outside the range of 10~100 will be blocked by the network unless you use an ethernet connection.
IPV4 = "0.0.0.0"
PORT = 80

def start_server():
    print("Starting Server...")
    httpd = HTTPServer((IPV4,PORT),Serv)
    print("HTTP starting on Address:",socket.gethostbyname(socket.gethostname()),"Port:",PORT)
    httpd.serve_forever()

#this class handles the HTTP server functionality
class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            #sets default path to main page
            self.path = '/Website/bobert.html'
        try:
            #reads the HTML file and sends a response code of 200 (success)
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            #send 404 response code otherwise
            file_to_open = "Error 404: File not found."
            self.send_response(404)
        #send file back to client
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

#placeholder! This will run from main.py in the future.
start_server()