#Code for handling setting up a local LAN server and networking etc.
#Being worked on by: Joe

from http.server import HTTPServer, BaseHTTPRequestHandler

#0.0.0.0 will make the website available for anyone on the local network on port 8765
ADDRESS = ("0.0.0.0", 8765)

def start_server():
    print("Starting Server...")
    httpd = HTTPServer(ADDRESS,Serv)
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