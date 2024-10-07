from http.server import BaseHTTPRequestHandler, HTTPServer
import json


PORT = 8888
socket = ("", PORT)


class Handler(BaseHTTPRequestHandler):
    def create_response(self, body):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        if self.path == "/healthcheck":
            body = json.dumps({"message": "everything okay"})
            self.create_response(body)


with HTTPServer(socket, Handler) as server:
    print(f"Serving at port {PORT}")
    server.serve_forever()