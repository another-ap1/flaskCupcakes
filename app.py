"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake, DEFAULT_CUPCAKE_IMAGE
from cupcake_secrets import SECRET_KEY

from forms import AddCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)

@app.route('/')
def show_home():
    """page to show all the cupcakes"""

    cupcakes = Cupcake.query.all()
    form = AddCupcakeForm()

    return render_template('index.html', cupcakes=cupcakes, form=form)

@app.route('/api/cupcakes')
def show_cupcakes():
    """get data for all cupcakes from db"""

    all_cupcakes=[cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    """get data for a specific cupcake"""

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """Add a new cupcake to the db"""
    if request.json['image']=="":
        new_cupcake = Cupcake(flavor=request.json["flavor"],
                          size=request.json["size"],
                          rating=request.json["rating"],
                          image=DEFAULT_CUPCAKE_IMAGE)
    else:
        new_cupcake = Cupcake(flavor=request.json["flavor"],
                          size=request.json["size"],
                          rating=request.json["rating"],
                          image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())

    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """update a cupcake in the db"""

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete a cupcake from db"""

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")