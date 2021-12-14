import cgi
import http.server
import socketserver

port = 8080 
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), handler) as httpd:
    print("Servidor web disponível na porta", port)
    httpd.serve_forever()
