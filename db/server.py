from http.server import BaseHTTPRequestHandler, HTTPServer
from db.utils.utils import get_parks_data, get_extended_park_data, get_ride_data
from connection import create_conn, close_db
from pg8000.native import literal
import json
import re


PORT = 8888
socket = ("", PORT)

REGEX_GET_RIDE_BY_ID = re.compile(r"/ride/(\d)")
REGEX_GET_PARK_BY_ID = re.compile(r"/parks/(\d)")
REGEX_POST_NEW_RIDE_PARK_ID = re.compile(r"/parks/(\d)/rides")
REGEX_PATCH_OR_DELETE_RIDE_ID = re.compile(r"/rides/(\d)")


class Handler(BaseHTTPRequestHandler):

    def create_response(self, response, body):
        self.send_response(response)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        if self.path == "/healthcheck":
            body = json.dumps({"message": "everything okay"})
            self.create_response(200, body)

        if self.path == "/parks":
            parks_data = get_parks_data()
            body = json.dumps({"parks": parks_data})
            self.create_response(200, body)

        if REGEX_GET_RIDE_BY_ID.search(self.path):
            ride_id = REGEX_GET_RIDE_BY_ID.search(self.path).group(1)
            body = json.dumps({"ride": get_ride_data(ride_id)})
            self.create_response(200, body)

        if REGEX_GET_PARK_BY_ID.search(self.path):
            park_id = REGEX_GET_PARK_BY_ID.search(self.path).group(1)
            body = json.dumps({"park": get_extended_park_data(park_id)})
            self.create_response(200, body)

    def do_POST(self):
        if REGEX_POST_NEW_RIDE_PARK_ID.search(self.path):
            park_id = REGEX_POST_NEW_RIDE_PARK_ID.search(self.path).group(1)
            content_length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(content_length).decode("utf-8")
            parsed_body = json.loads(request_body)
            db = create_conn()
            insert_query = f"""
                INSERT INTO rides 
                    ("park_id", "ride_name", "year_opened", "votes")
                VALUES 
                    ({park_id}, {literal(parsed_body["ride_name"])}, {literal(parsed_body["year_opened"])}, 0)
                RETURNING ride_id;
            """
            ride_id = db.run(sql=insert_query)[0][0]
            close_db(db)
            body = json.dumps({"ride": get_ride_data(ride_id)})
            self.create_response(201, body)

    def do_PATCH(self):
        if REGEX_PATCH_OR_DELETE_RIDE_ID.search(self.path):
            ride_id = REGEX_PATCH_OR_DELETE_RIDE_ID.search(self.path).group(1)
            content_length = int(self.headers["Content-Length"])
            request_body = self.rfile.read(content_length).decode("utf-8")
            parsed_body = json.loads(request_body)
            db = create_conn()
            update_query = f"""
                UPDATE rides
                SET ride_name = {literal(parsed_body["ride_name"])}
                WHERE ride_id = {literal(ride_id)};
            """
            db.run(sql=update_query)
            close_db(db)
            body = json.dumps({"ride": get_ride_data(ride_id)})
            self.create_response(200, body)

    def do_DELETE(self):
        if REGEX_PATCH_OR_DELETE_RIDE_ID.search(self.path):
            ride_id = REGEX_PATCH_OR_DELETE_RIDE_ID.search(self.path).group(1)
            db = create_conn()
            delete_query = f"""DELETE FROM rides WHERE ride_id = {literal(ride_id)}"""
            db.run(sql=delete_query)
            close_db(db)
            self.send_response(204)
            self.end_headers()


with HTTPServer(socket, Handler) as server:
    print(f"Serving at port {PORT}")
    server.serve_forever()