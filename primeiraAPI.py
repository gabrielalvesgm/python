from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def get_message():
    return jsonify({"message": "Olá, está é minha primeira API REST!"})
if __name__ == '__main__':
    app.run(debug=True)
