#Code for handling setting up a local LAN server and networking etc.
#Being worked on by: Joe

from http.server import HTTPServer, BaseHTTPRequestHandler

ADDRESS = ("0.0.0.0", 8765)

def start_server():
    print("Starting Server...")
    httpd = HTTPServer(ADDRESS,Serv)
    httpd.serve_forever()

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
       if self.path == '/':
           self.path = '/Website/bobert.html'
       try:
           file_to_open = open(self.path[1:]).read()
           self.send_response(200)
       except:
           file_to_open = "File not found"
           self.send_response(404)
       self.end_headers()
       self.wfile.write(bytes(file_to_open, 'utf-8'))

start_server()