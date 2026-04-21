from flask import Flask
import socket
import os
app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "DevOps App Running 🚀",
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "env": os.environ.get("ENV", "dev")
    }

@app.route("/health")
def health():
    return {"status": "ok"}

import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
