from flask import Flask, request, jsonify

app = Flask(__name__)


welcome_messages = [
    {
        "id":0,
        "message" : "Welcome to the Summoner\'s Rift"
    }
]


def create_app():
    app = Fask(__name__)
        
    @app.route('/testget', methods=['GET'])
    def welcome():
        return jsonify(welcome_messages)

    @app.route('/', methods=['GET'])
    def root():
        return "SIG SUPER PODEROSO"
    return app
    