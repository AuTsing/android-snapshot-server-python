import os
from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)


@app.route("/")
def snapshot():
    cmd_snapshot = "adb shell screencap -p /data/local/tmp/snapshot.png"
    cmd_pull = "adb pull /data/local/tmp/snapshot.png ./snapshot.png"

    os.system(cmd_snapshot)
    os.system(cmd_pull)

    return send_file("./snapshot.png")


CORS(app)
app.run(host="0.0.0.0", port=5050)
