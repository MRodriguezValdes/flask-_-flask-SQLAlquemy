from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from faker import Faker

import random

# Facker genera datos falsos
fake = Faker()


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


# Añade 100 clientes falsos
def add_customers():
    for _ in range(100):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.street_address(),
            city=fake.city(),
            postcode=fake.postcode(),
            email=fake.email(),
        )
        db.session.add(customer)
    db.session.commit()


def add_orders():
    # Hago una query que devuelve todos los clientes
    customers = Customer.query.all()

    for _ in range(1000):
        # Selecciono un cliente aleatorio
        customer = random.choice(customers)

        ordered_date = fake.date_time_this_year()
        shipped_date = random.choices(
            [None, fake.date_time_between(start_date=ordered_date)], [10, 90]
        )[0]

        # Aqui lo que hacemos es asignar None o un valor random a delivered_date
        delivered_date = None
        if shipped_date:
            delivered_date = random.choices(
                [None, fake.date_time_between(start_date=shipped_date)], [50, 50]
            )[0]

        # Aqui lo que hacemos es asignar None o un valor random a coupon_code
        coupon_code = random.choices(
            [None, "50OFF", "FREESHIPPING", "BUYONEGETONE"], [80, 5, 5, 5]
        )[0]

        #Generamos la orden
        order = Order(
            customer_id=customer.id,
            order_date=ordered_date,
            shipped_date=shipped_date,
            delivered_date=delivered_date,
            coupon_code=coupon_code,
        )

        db.session.add(order)
    db.session.commit()

#Agregamos 10 productos
def add_products():
    for _ in range(10):
        #Los prodcutos son colores random con un precio entre 10 y 100
        product = Product(name=fake.color_name(), price=random.randint(10, 100))
        db.session.add(product)
    db.session.commit()

#Se establece una relacion enre el producto y su compra
def add_order_products():
    #Hacemos dos queries para obtener todas las ordenes y productos
    orders = Order.query.all()
    products = Product.query.all()

    for order in orders:
        # Seleccionamos un numero aleatorio k
        k = random.randint(1, 3)
        # Seleccionamos un producto aleatorio
        purchased_products = random.sample(products, k)
        order.products.extend(purchased_products)

    db.session.commit()


# Llamamos a las funciones y genereamos informacion falsa
def create_random_data():
    db.create_all()
    add_customers()
    add_orders()
    add_products()
    add_order_products()
