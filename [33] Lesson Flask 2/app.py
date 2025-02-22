from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(50), nullable=False, unique=True)
  email = db.Column(db.String(100))
  age = db.Column(db.Integer)


# flask db init
# flask db migrate -m "Init migrate"
# flask db upgrade


# flask db migrate -m "Add column age"
# flask db upgrade


@app.route('/')
@app.route('/index')
def main_page():
  # return "Main Page"
  # return "<h1>Main Page</h1>"
  return "<h1>მთავარი გვერდი</h1>"


@app.route('/home', methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    return "<h1>Page with POST method...</h1>"
  elif request.method == 'GET':
    return "<h1>Page with GET method...</h1>"


@app.route("/create_user", methods=['POST', 'GET'])
def create_user():
  if request.method == "POST":
    username = request.form['username']
    email = request.form['email']
    age = request.form['age']
 
    user = User(username=username, email=email, age=age)
    db.session.add(user)
    db.session.commit()

    # print(username)
    # print(email)
    # print(age)
 
    return "User created success!.."
 
  return render_template('create_user.html')


@app.route('/user/<int:user_id>')
def get_user(user_id):
  # user = User.query.get(user_id)
  user = User.query.get_or_404(user_id)

  # return str(user.id)
  # return f"{user.id}"

  return f"<p>Username: {user.username}, E-mail: {user.email}, Age: {user.age}</p>"

@app.route('/users')
def users():
  # users = User.query.all()
  # users = User.query.filter(User.age < 40)
  # users = User.query.filter(User.email.endswith('mail.com'))
  users = User.query.order_by(User.age.desc())

  result = ''
  for user in users:
    result += f"<p>Username: {user.username}, E-mail: {user.email}, Age: {user.age}</p>"

  return result

# ==============
if __name__ == '__main__':
  app.run(debug=True)