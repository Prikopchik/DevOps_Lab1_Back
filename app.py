from flask import Flask, request, jsonify
import os

app = Flask(__name__)

DATA_FILE = 'data.txt'

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    if data:
        with open(DATA_FILE, 'a') as f:
            f.write(data + '\n')
        return jsonify({'message': 'Данные успешно сохранены'}), 200
    return jsonify({'message': 'Нет данных для сохранения'}), 400

@app.route('/api/data', methods=['GET'])
def get_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = f.read()
        return jsonify({'data': data}), 200
    return jsonify({'data': 'Файл данных не найден'}), 404

if __name__ == '__main__':
    app.run(debug=True)
