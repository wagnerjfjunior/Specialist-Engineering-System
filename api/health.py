import json
from http.server import BaseHTTPRequestHandler

from runtime.specialist_gateway.http_api import health_check


class handler(BaseHTTPRequestHandler):
    def _write_json(self, status_code, payload):
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        result = health_check()
        self._write_json(result.status_code, result.body)

    def do_POST(self):
        self.send_response(405)
        self.send_header("Allow", "GET")
        self.end_headers()
