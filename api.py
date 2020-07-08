from flask import Flask, request, jsonify

app = Flask(__name__)


welcome_messages = [
    {
        "id":0,
        "message" : "Welcome to the Summoner\'s Rift"
    }
]

@app.route('/testget', methods=['GET'])
def welcome():
    return jsonify(welcome_messages)

@app.route('/', methods=['GET'])
def root():
    return "SIG SUPER PODEROSO"

if __name__ == '__main__':

    app.run()