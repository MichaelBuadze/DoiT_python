from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate (app, db)

@app.route('/')
@app.route('/index')
def main_page():
    return 'Main Page'


@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return "<h1></h1>"

# ============================================

if __name__ == "__main__":
    app.run(debug=True)

print ("Hello World")