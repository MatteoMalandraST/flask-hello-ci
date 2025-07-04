import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify(msg="hello devops")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)