from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TechData(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    manufacturer = db.Column(db.String(100), nullable = False)
    model = db.Column(db.String(100), nullable = False)
    instock = db.Column(db.String(5), nullable = False)
    price = db.Column(db.Integer, nullable = False)

    def __init__(self, manufacturer, model, instock, price):
        self.manufacturer = manufacturer
        self.model = model
        self.instock = instock
        self.price = price

print ("Ready to Go!") 