from app import app
from flask import request
from app import db
from bird import Bird


@app.route('/')
def index():
    firstmember = Bird.query.first()
    return '<h1> Here you can find bird list! </h1>'


@app.route('/bird')
def view():
    bird = Bird.query.first()
    if bird is not None:
        return str('First member weight \n' + bird.__str__())
    else:
        return "Bird with this id does not exist"


@app.route('/bird/<id>')
def get_bird(id):
    bird = Bird.query.get(id)
    if bird is not None:
        return bird.__str__()
    else:
        return "Bird with this id does not exist"


@app.route('/bird', methods=['POST'])
def add_bird():
    bird_id = request.json['id']
    name = request.json['name']
    bird_type = request.json['type']
    weight = request.json['weight']

    new_bird = Bird()
    new_bird.bird_id = bird_id
    new_bird.name = name
    new_bird.type = bird_type
    new_bird.weight = weight

    db.session.add(new_bird)
    db.session.commit()

    return str(new_bird.__str__())


@app.route('/bird/<id>', methods=['PUT'])
def bird_update(id):
    name = request.json['name']
    bird_type = request.json['type']
    weight = request.json['weight']

    new_bird = Bird()
    new_bird.name = name
    new_bird.type = bird_type
    new_bird.weight = weight

    db.session.commit()

    return new_bird.__str__()


@app.route('/bird/<id>', methods=['DELETE'])
def bird_delete(id):
    bird = Bird.query.get(id)
    db.session.delete(bird)
    db.session.commit()

    return str("Deleting successful")
