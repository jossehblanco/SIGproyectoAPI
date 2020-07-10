from flask import Flask, make_response, request, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
import datetime
from functools import wraps
import uuid
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)

db = SQLAlchemy()


class Circle_curated_api(db.Model):
#Clase para 
    __tablename__ = 'circle_curated_api'
    circle_id = db.Column(db.Integer, primary_key = True)
    lat = db.Column(db.String)
    long_ = db.Column('long', db.String)
    radius = db.Column(db.Float)
    density = db.Column(db.Integer)
    risk_level = db.Column(db.String)
    
    def tojson(self):
        return { 
            "id": self.circle_id,
            "latitude" : float(self.lat),
            "longitude" : float(self.long_),
            "radius" : float(self.radius)*111111,
            "density" : self.density,
            "risk_level" : self.risk_level
        }


class Usuario(db.Model):
#Clase para 
    __tablename__ = 'usuario'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    pass_ = db.Column('pass', db.String)
    iscovid = db.Column(db.Integer)
    
    def tojson(self):
        return { 
            "id": self.user_id,
            "user" : self.username,
            "pass" : self.pass_,
            "iscovid" : float(self.iscovid),
        }


    
    
app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY']='sig012020'

    app.config['DEBUG'] = False
    POSTGRES = {
    'user': 'ugkqsbelwstbad',
    'pw': '22f3336ee10a38155a9140a7e56a4ce378ab17110d6179753d98b27f36b09796',
    'db': 'dctkv6bissui9r',
    'host': 'ec2-52-72-65-76.compute-1.amazonaws.com',
    'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ugkqsbelwstbad:22f3336ee10a38155a9140a7e56a4ce378ab17110d6179753d98b27f36b09796@ec2-52-72-65-76.compute-1.amazonaws.com:5432/dctkv6bissui9r' % POSTGRES
    jwt = JWTManager(app)
    db.init_app(app)
        
    @app.route('/circles', methods=['GET'])
    @jwt_required
    def getcircles():
        circles = Circle_curated_api.query.all()
        lcircles = []
        for item in circles:
            lcircles.append(item.tojson())
        return jsonify(lcircles)

    @app.route('/circlesdev', methods=['GET'])
    def getcirclesdev():
        circles = Circle_curated_api.query.all()
        lcircles = []
        for item in circles:
            lcircles.append(item.tojson())
        return jsonify(lcircles)


    @app.route('/login', methods=['POST'])
    def login_user():
        print(request.authorization)
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return make_response('missing arguments', 401, {'WWW.Authentication': 'Basic realm: "login required"'})
        user = Usuario.query.filter_by(username=auth.username).first()
        if (user.pass_ == auth.password):
            data = {'user_id': user.user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
            access_token = create_access_token(identity= {"user_id" : user.user_id})
            return {"access_token" : access_token, "user_id" : user.user_id}, 200
        return make_response('authentication failed',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

    @app.route('/register', methods=['POST'])
    def register_user():
        username = request.json.get('username')
        pwd = request.json.get('password')
        if username is None or pwd is None:
            return jsonify({'message' : 'missing arguments: username or password'}), 400
        if Usuario.query.filter_by(username= username).first() is not None:
            return jsonify({'message' : 'missing arguments: username or password'}), 400
        user = Usuario(username = username, pass_ = pwd, iscovid = 0)
        access_token = create_access_token(identity= {"user_id" : user.user_id})
        db.session.add(user)
        db.session.commit()
        return jsonify({'message' : 'success', "token" : access_token, "user_id" : user.user_id}), 200

    
    @app.route('/', methods=['GET'])
    def root():
        return "API PARA EL PROYECTO DE SIG"
    app.config['CONFIG'] = True
    return app