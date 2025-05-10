from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/stats/')
def get_stats():
    return jsonify({
        "onlineDrivers": 22,
        "onTimeRate": 92,
        "distanceToday": 128,
        "ordersOverdue": 14
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
