from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/Flask_Intro'
db = SQLAlchemy(app)


class Skotare(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(30), unique=False, nullable=False)
    Animals = db.relationship("Animal", backref="skotare", lazy=True)


class Animal(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Typ = db.Column(db.String(20), unique=False, nullable=False)
    Namn = db.Column(db.String(30), unique=False, nullable=False)
    Vikt = db.Column(db.Integer, unique=False, nullable=True)
    Skotare_Id = db.Column(db.Integer, db.ForeignKey(
        "skotare.Id"), nullable=False)


db.create_all()

while True:
    print("""
       1. Skapa djur
       2. Lista alla 
       3. Ändra djur
       4. Söka djur

       11. Ny skötare
        """)
    sel = input("Val: ")
    if sel == "1":
        a = Animal()
        a.Namn = input("Ange namn: ")
        a.Typ = input("Ange typ: ")
        a.Vikt = int(input("Ange vikt: "))
        a.Skotare_Id = int(input("Ange SkotareID"))
        db.session.add(a)
        db.session.commit()
    if sel == "2":
        for animal in Animal.query.all():
            print(f"{animal.Namn} {animal.Typ} {animal.Vikt}")
    if sel == "3":
        selectedID = int(input("Ange Id: "))
        djurAttUppdatera = Animal.query.filter_by(Id=selectedID).first()
        djurAttUppdatera.Namn = input("Ange nytt namn: ")
        djurAttUppdatera.Vikt = input("Ange nytt vikt: ")
        db.session.commit()

    if sel == "4":
        search = input("Sök efter: ")
        print("Sökresultat")
        for animal in Animal.query.filter(Animal.Namn.contains(search)).all():
            print(f"{animal.Id} {animal.Namn}")
        print("Slut sök")

    if sel == "11":
        s = Skotare()
        s.Namn = input("Ange namn: ")
        db.session.add(s)
        db.session.commit()
    if sel == "12":
        skotarID = int(input("Ange id: "))
        skotare = Skotare.query.get(skotarID)
        for animal in skotare.Animals:
            print(animal.Namn)
        print(f"{skotare.Namn} {skotare.Animals[0].Namn}")
