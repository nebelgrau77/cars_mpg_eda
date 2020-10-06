import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from sqlalchemy import func

from make_chart import make_chart

# define paths to project and database
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, 'cars.db'))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file # tell the app where the database is

bootstrap = Bootstrap(app)

db = SQLAlchemy(app) # initialize a connection to the database

class Car(db.Model):
    __tablename__ = 'cars'
    index = db.Column(db.Integer(), unique = True, nullable=False, primary_key=True)
    brand = db.Column(db.String(40), unique = False, nullable = False)
    model = db.Column(db.String(40), unique = False, nullable = True)
    model_year = db.Column(db.Integer(), unique = False, nullable=False)
    origin = db.Column(db.String(80), unique = False, nullable = True)
    cylinders = db.Column(db.Integer(), unique = False, nullable=False)
    displacement_ccm = db.Column(db.Float(), unique = False, nullable=False)    
    horsepower = db.Column(db.Integer(), unique = False, nullable=False)
    acceleration = db.Column(db.Float(), unique = False, nullable=False)
    weight_kg = db.Column(db.Float(), unique = False, nullable=False)
    liters_per_100km = db.Column(db.Float(), unique = False, nullable=False)

    def __repr__(self):
        return "<Brand: {}, Model: {}, Origin: {}>".format(self.brand, self.model, self.origin)

@app.route('/')
def home():

    return render_template('home.html')

@app.route('/select_brand/')
def select_brand():
    brands = db.session.query(Car.brand.distinct()).all()
    brands = sorted([brand[0] for brand in brands])
    
    return render_template('select_brand.html', brands = brands)

@app.route('/select_brand/display')
def by_brand():
    
    brand = request.args.get('brand')
    
    avg_weight = db.session.query(func.avg(Car.weight_kg)).filter(Car.brand == brand).scalar()
    avg_horsepower = db.session.query(func.avg(Car.horsepower)).filter(Car.brand == brand).scalar()
    avg_consumption = db.session.query(func.avg(Car.liters_per_100km)).filter(Car.brand == brand).scalar()
    count = db.session.query(func.count(Car.index)).filter(Car.brand == brand).scalar()

    return render_template('by_brand.html', brand = brand, avg_weight = avg_weight, avg_horsepower = avg_horsepower, avg_consumption = avg_consumption, count = count)

@app.route('/select_year/')
def select_year():
    years = db.session.query(Car.model_year.distinct()).all()
    years = sorted([year[0] for year in years])
    return render_template('select_year.html', years = years)

@app.route('/select_year/display')
def by_year():
    year = request.args.get('year')

    avg_HP = db.session.query(func.avg(Car.horsepower)).filter(Car.model_year == year).scalar()
    return render_template('by_year.html', year = year, avg_HP = avg_HP)

@app.route('/test_chart')
def test_chart():       
    
    val = request.args.get('val')
   
    queries = {'weight': Car.weight_kg, 'horsepower': Car.horsepower}

    myquery = db.session.query(Car.model_year, func.avg(queries.get(val, Car.weight_kg))).group_by(Car.model_year).all()

    years = [item[0] for item in myquery]
    values = [item[1] for item in myquery]
    chart = make_chart(years, values, val)

    return render_template('test_chart.html', vals = queries.keys(), chart = chart)
