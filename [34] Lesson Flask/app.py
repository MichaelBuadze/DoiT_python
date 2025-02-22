from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate
from config import Config
from models import db, TechData

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
 all_data = TechData.query.all()
 



 return render_template('index.html', technique = all_data)


@app.route("/insert", methods = ["POST", "GET"])
def insert():
  if request.method == "POST":
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    instock = request.form['instock']
    price = request.form['price']

    data = TechData(manufacturer=manufacturer, model=model, instock=instock, price=price)


    db.session.add(data)
    db.session.commit()

    flash("Order Insetred Successfully...")

    return redirect (url_for('index'))


@app.route("/update",  methods = ["POST", "GET"])
def update():
  if request.method == 'POST':
    # data = TechData.query.get(request.form['id'])
    data = TechData.query.get(request.form.get('id'))

    data.manufacturer = request.form.get('manufacturer')
    data.model = request.form.get('model')
    data.instock = request.form.get('instock')
    data.price = request.form.get('price')

    db.session.commit()

    flash("Technuque Updated Successfully...")
    
    return redirect (url_for('index'))
  
@app.route('/delete/<id>')
def delete(id):
  data = TechData.query.get(id)

  db.session.delete(data)
  db.session.commit()

  flash("Technique Deleted Successfully ... ")

  return redirect (url_for('index'))




#===========
if __name__ == '__main__':
  app.run(debug=True, port = 5034)