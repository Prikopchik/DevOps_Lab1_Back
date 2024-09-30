from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    if data:
        with open('data.txt', 'a') as f:
            f.write(data + '\n')
        return jsonify({'message': 'Данные успешно сохранены'}), 200
    return jsonify({'message': 'Нет данных для сохранения'}), 400

if __name__ == '__main__':
    app.run(debug=True)