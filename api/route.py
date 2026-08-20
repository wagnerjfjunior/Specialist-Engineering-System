import json
from http.server import BaseHTTPRequestHandler

from runtime.specialist_gateway.http_api import route_request

MAX_BODY_BYTES = 65536


class handler(BaseHTTPRequestHandler):
    def _write_json(self, status_code, payload):
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        raw_length = self.headers.get("Content-Length")
        try:
            content_length = int(raw_length or "0")
        except ValueError:
            self._write_json(400, {"status": "error", "error": "INVALID_REQUEST"})
            return

        if content_length <= 0 or content_length > MAX_BODY_BYTES:
            self._write_json(400, {"status": "error", "error": "INVALID_REQUEST"})
            return

        try:
            payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self._write_json(400, {"status": "error", "error": "INVALID_REQUEST"})
            return

        result = route_request(payload, self.headers.get("X-SES-Gateway-Key"))
        self._write_json(result.status_code, result.body)

    def do_GET(self):
        self.send_response(405)
        self.send_header("Allow", "POST")
        self.end_headers()
