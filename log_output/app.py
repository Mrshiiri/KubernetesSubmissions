import os
import uuid
import threading
import time
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8000))
random_string = str(uuid.uuid4())

def log_loop():
    while True:
        timestamp = datetime.now(timezone.utc).isoformat()
        print(f"{timestamp}: {random_string}", flush=True)
        time.sleep(5)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            timestamp = datetime.now(timezone.utc).isoformat()
            body = f"{timestamp}: {random_string}"
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(body.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    threading.Thread(target=log_loop, daemon=True).start()
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server started in port {PORT}", flush=True)
    server.serve_forever()