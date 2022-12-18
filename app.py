from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


# Creando una instancia
app = Flask(__name__)
# Configurando la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Relacionando la base de datos con la app flask
db = SQLAlchemy(app)

# Creando 3 tablas (Models) con primary_key ID
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    # Relacionando la tabla Orders con Customer
    orders = db.relationship("Order", backref="customer")


# Creando la tabla que surge de la relacion N:M entre Order y Product
order_product = db.Table(
    "order_product",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped_date = db.Column(db.DateTime)
    delivered_date = db.Column(db.DateTime)
    coupon_code = db.Column(db.String(50))
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

    # Relacionando las tablas Order y Product mediante la tabla order product
    products = db.relationship("Product", secondary=order_product)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
