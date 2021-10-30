from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = 'roy'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# Do not run if the app.py is imported from other file.
if __name__ == '__main__':
    app.run(port=5000, debug=True)
