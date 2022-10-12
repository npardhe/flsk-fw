
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy is an ORM written in Python to SQL

app = Flask(__name__)  # creating flask obj

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin@localhost/mydb" # configer  db


db = SQLAlchemy(app)  # db contain helper func. of ORM

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))

    def __init__(self, name,city,id):
        self.name = name
        self.city = city
        self.id = id


@app.route('/')
def show_all():
    info=Students(name='A',city='betul',id=5)
    #print(info)
    db.session.add(info)
    db.session.commit()
    data = Students.query.all()
    results = [
        {
            "name": car.name,
            "id": car.id,
            "city": car.city
        } for car in data]

    return {"count": len(results), "cars": results}
    #return "DB Created"



if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)

