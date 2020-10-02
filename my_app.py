import os

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

# define paths to project and database
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, 'cars.db'))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file # tell the app where the database is

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

    brands = db.session.query(Car.brand.distinct()).all()
    brands = [brand[0] for brand in brands]
    return render_template('home.html', brands = brands)

@app.route('/by_brand/')
def by_brand():
    brand = request.args.get('brand')
    
    
    avg = db.session.query(func.avg(Car.weight_kg)).filter(Car.brand == brand).scalar()

    cars = db.session.query(Car).filter(Car.brand == brand).all()
    heaviest = Car.query.filter_by(brand = brand).order_by(Car.weight_kg.desc()).first()
    return render_template('by_brand.html', brand = brand, cars = cars, heavy = heaviest, avg = avg)


'''
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        kit = Kit(name = request.form.get("name"), manufacturer = request.form.get("manufacturer"), scale = int(request.form.get("scale")))
        db.session.add(kit)
        db.session.commit()
    kits = Kit.query.all()
    return render_template('home.html', kits = kits)

@app.route('/update', methods=["POST"])
def update():
    newname = request.form.get("newname")
    oldname = request.form.get("oldname")
    newmanufacturer = request.form.get("newmanufacturer")
    newscale = request.form.get("newscale")
    kit = Kit.query.filter_by(name = oldname).first()
    kit.name = newname
    kit.manufacturer = newmanufacturer
    kit.scale = int(newscale)
    db.session.commit()
    return redirect('/')

@app.route('/delete', methods = ["POST"])
def delete():
    name = request.form.get("name")
    kit = Kit.query.filter_by(name=name).first()
    db.session.delete(kit)
    db.session.commit()
    return redirect('/')
'''