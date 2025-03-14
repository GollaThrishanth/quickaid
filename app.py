from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "QuickAid Backend is Running!"

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "message": "Backend is live"})

@app.route('/api/help', methods=['GET'])
def help_info():
    return jsonify({
        "endpoints": [
            {"route": "/api/status", "description": "Check server status"},
            {"route": "/api/help", "description": "Get API endpoints"}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
