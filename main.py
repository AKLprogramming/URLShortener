import SimpleHTTPServer
import SocketServer

PORT_NUMBER = 4555

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT_NUMBER), Handler)

print ("serving at port", PORT_NUMBER)
httpd.serve_forever()

