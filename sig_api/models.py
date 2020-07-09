from flask_sqlalchemy import SQLAlchemy

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
            "lat" : float(self.lat),
            "long" : float(self.long_),
            "radius" : float(self.radius),
            "density" : self.density,
            "risk_level" : self.risk_level
        }
    