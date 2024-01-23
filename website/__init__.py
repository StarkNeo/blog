import os
from flask import Flask
#from dotenv import load_dotenv
#print(load_dotenv('.env'))
#print(os.getenv('KEY'))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']=os.getenv('KEY')

    from .views import views

    app.register_blueprint(views)
    return app