from flask import Flask, request, jsonify
from models import db, Circle_curated_api
import json

app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    POSTGRES = {
    'user': 'ugkqsbelwstbad',
    'pw': '22f3336ee10a38155a9140a7e56a4ce378ab17110d6179753d98b27f36b09796',
    'db': 'dctkv6bissui9r',
    'host': 'ec2-52-72-65-76.compute-1.amazonaws.com',
    'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ugkqsbelwstbad:22f3336ee10a38155a9140a7e56a4ce378ab17110d6179753d98b27f36b09796@ec2-52-72-65-76.compute-1.amazonaws.com:5432/dctkv6bissui9r' % POSTGRES

    db.init_app(app)
        
    @app.route('/circles', methods=['GET'])
    def welcome():
        circles = Circle_curated_api.query.all()
        lcircles = []
        for item in circles:
            lcircles.append(item.tojson())
        return jsonify(lcircles)

    @app.route('/', methods=['GET'])
    def root():
        return "API PARA EL PROYECTO DE SIG"
    app.config['CONFIG'] = True
    return app