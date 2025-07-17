from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = 'super-secret-key'
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'  # JWT encryption key

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# Simple user model (use real DB in production)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def json(self):
        return {"id": self.id, "name": self.name, "price": self.price}


# Auth route
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.username)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

# CRUD operations on items
class ItemResource(Resource):
    @jwt_required()
    def get(self, name):
        item = Item.query.filter_by(name=name).first()
        if item:
            return item.json(), 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if Item.query.filter_by(name=name).first():
            return {"message": f"Item '{name}' already exists."}, 400
        data = request.get_json()
        item = Item(name=name, price=data['price'])
        db.session.add(item)
        db.session.commit()
        return item.json(), 201

    @jwt_required()
    def put(self, name):
        data = request.get_json()
        item = Item.query.filter_by(name=name).first()
        if item:
            item.price = data['price']
        else:
            item = Item(name=name, price=data['price'])
            db.session.add(item)
        db.session.commit()
        return item.json(), 200

    @jwt_required()
    def delete(self, name):
        item = Item.query.filter_by(name=name).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return {"message": f"Item '{name}' deleted."}
        return {"message": "Item not found"}, 404

class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in Item.query.all()]}


# Routes
api.add_resource(UserLogin, '/login')
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# Setup database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create a demo user if it doesn't exist
        if not User.query.filter_by(username='admin').first():
            db.session.add(User(username='admin', password='password'))
            db.session.commit()
    app.run(debug=True)