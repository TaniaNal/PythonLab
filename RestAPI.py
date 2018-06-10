from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)

birds = {}

birds_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'weight': fields.Float,
    'amount': fields.Integer,
    'birds_colour': fields.String,
    'birds_type': fields.String
}


class Birds(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('weight', type=float, location='json')
        self.reqparse.add_argument('amount', type=int, location='json')
        self.reqparse.add_argument('birds_colour', type=str, location='json')
        self.reqparse.add_argument('birds_type', type=str, location='json')
        super(Birds, self).__init__()  # super().__init__() / bird.__init__(self)

    @app.route('/birds')
    def put(self):
        args = self.reqparse.parse_args()
        bird = {
            'id': args['id'],
            'name': args['name'],
            'weight': args['weight'],
            'amount': args['amount'],
            'birds_colour': args['birds_colour'],
            'birds_type': args['birds_type']
        }
        birds.update(bird)
        return marshal(bird, birds_fields), 201

    @app.route('/birds')
    def post(self):
        args = self.reqparse.parse_args()
        bird = [bird for bird in birds if birds.get('id') == args['id']]
        if len(bird) == 0:
            abort(404)
        birds.pop(bird[0])
        new_bird = {
            'id': args['id'],
            'name': args['name'],
            'weight': args['weight'],
            'amount': args['amount'],
            'birds_colour': args['birds_colour'],
            'birds_type': args['birds_type']
        }
        birds.update(new_bird)
        return marshal(new_bird, birds_fields)

    @app.route('/birds/<int:id>')
    def get(self, id):
        bird = [bird for bird in birds if birds.get('id') == id]
        if len(bird) == 0:
            abort(404)
        return marshal(bird[0], birds_fields)

    @app.route('/birds/<int:id>')
    def delete(self, id):
        bird = [bird for bird in birds if birds.get('id') == id]
        if len(bird) == 0:
            abort(404)
        birds.pop(bird[0])
        return {'result': True}


api.add_resource(Birds, '/birds', endpoint='birds')
api.add_resource(Birds, '/birds/<int:id>', endpoint='bird')

if __name__ == '__main__':
    app.run(debug=True)