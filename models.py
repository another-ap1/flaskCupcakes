"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_CUPCAKE_IMAGE='https://tinyurl.com/demo-cupcake'

class Cupcake(db.Model):
    __tablename__='cupcakes'

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, default=DEFAULT_CUPCAKE_IMAGE)

    def serialize(self):
        return{
            'id':self.id,
            'flavor':self.flavor,
            'size':self.size,
            'rating':self.rating,
            'image':self.image
        }
