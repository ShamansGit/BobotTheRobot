#Code for handling setting up a local LAN server and networking etc.
#Being worked on by: Joe

import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

#IMPORTANT: Make sure the firewall is off when running this code!

#0.0.0.0 will make the website available for anyone on the local network on port 80
IPV4 = "0.0.0.0"
#note: non-standard ports outside the range of 10~100 will be blocked by the network unless you use an ethernet connection.
PORT = 80

def start_server():
    print("Starting Server...")
    httpd = HTTPServer((IPV4,PORT),ServerHandler)
    print("HTTP starting on Address:",socket.gethostbyname(socket.gethostname()),"Port:",PORT)
    httpd.serve_forever()

#this class handles the HTTP server functionality
#for documentation on the various different response codes see: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            #If path is empty (i.e. page just opened) then redirect the user to the main page.
            file_to_open = "Redirecting..."
            #code 301 is the 'permanent redirect' code response.
            self.send_response(301)
            self.send_header('Location','/Website/bobert.html')
        elif self.path.startswith("/Website/") == False:
            #Forbids access to non-website files outside the directory e.g. stuff in the data folder
            file_to_open = "Error 403: Forbidden."
            self.send_response(403)
        else:
            try:
                #reads the requested file and sends a response code of 200 (success)
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
            except:
                #send 404 response code otherwise
                file_to_open = "Error 404: File not found."
                self.send_response(404)
        #sends the data back to the client
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

#placeholder! This will run from main.py in the future.
start_server()