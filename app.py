from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_track():
    base_lat = 22.5431
    base_lng = 114.0579

    path = []
    for i in range(10):
        path.append([
            base_lat + i * 0.01,
            base_lng + i * 0.01
        ])
    return path

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/track", methods=["GET"])
def get_track():
    plate = request.args.get("plate")

    if not plate:
        return jsonify({"error": "missing plate"}), 400

    return jsonify({
        "plate": plate,
        "path": generate_track()
    })

if __name__ == "__main__":
    app.run(debug=True)
