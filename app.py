import os
import urllib.request
import zipfile
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer

url = "https://github.com/XTLS/Xray-core/releases/download/v1.8.24/Xray-linux-64.zip"
urllib.request.urlretrieve(url, "app.zip")
with zipfile.ZipFile("app.zip", 'r') as z:
    z.extractall()
os.rename("xray", "web_server")
os.chmod("web_server", 0o755)

config_data = '{"log":{"loglevel":"warning"},"inbounds":[{"port":8000,"protocol":"vless","settings":{"clients":[{"id":"83132cd9-67d9-4014-8b7d-8b5b2c86960e"}],"decryption":"none"},"streamSettings":{"network":"ws","wsSettings":{"path":"/"}}}],"outbounds":[{"protocol":"freedom"}]}'
with open("config.json", "w") as f:
    f.write(config_data)

subprocess.Popen(["./web_server", "-c", "config.json"])

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Active Server")

HTTPServer(('0.0.0.0', 8000), H).serve_forever()
