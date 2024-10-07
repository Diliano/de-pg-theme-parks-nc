from http.server import BaseHTTPRequestHandler, HTTPServer
from db.utils.format_rides import get_parks_data, get_ride_data
import json
import re


PORT = 8888
socket = ("", PORT)

REGEX_RIDE_ID = re.compile(r"/ride/(\d)")


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

        if self.path == "/parks":
            parks_data = get_parks_data()
            body = json.dumps({"parks": parks_data})
            self.create_response(body)

        if REGEX_RIDE_ID.search(self.path):
            id = REGEX_RIDE_ID.search(self.path).group(1)
            body = json.dumps({"ride": get_ride_data(id)})
            self.create_response(body)


with HTTPServer(socket, Handler) as server:
    print(f"Serving at port {PORT}")
    server.serve_forever()