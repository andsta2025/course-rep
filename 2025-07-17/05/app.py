from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# App setup
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class ItemModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def json(self):
        return {"id": self.id, "name": self.name, "price": self.price}

# API Resource
class Item(Resource):
    def get(self, name):
        item = ItemModel.query.filter_by(name=name).first()
        if item:
            return item.json(), 200
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.query.filter_by(name=name).first():
            return {"message": f"Item '{name}' already exists."}, 400

        data = request.get_json()
        item = ItemModel(name=name, price=data['price'])
        db.session.add(item)
        db.session.commit()
        return item.json(), 201

    def put(self, name):
        data = request.get_json()
        item = ItemModel.query.filter_by(name=name).first()
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name=name, price=data['price'])
            db.session.add(item)
        db.session.commit()
        return item.json()

    def delete(self, name):
        item = ItemModel.query.filter_by(name=name).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            return {"message": f"Item '{name}' deleted."}
        return {"message": "Item not found."}, 404

class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}

# Routes
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# Initialize DB and run app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)