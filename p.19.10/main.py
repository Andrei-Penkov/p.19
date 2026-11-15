from flask import Flask, request, jsonify

app = Flask(__name__)

received_data = []
stored_data = []


@app.route('/set', methods=['POST'])
def set_data():
    global received_data

    data = request.get_json(silent=True)
    if not isinstance(data, list):
        return jsonify({"error": "Ожидается JSON-массив"}), 400

    received_data = data
    return jsonify({"status": "ok", "saved": received_data}), 200


@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(stored_data), 200


if __name__ == '__main__':
    app.run(debug=True)