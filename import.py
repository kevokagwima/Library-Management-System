import csv
from flask import Flask
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql://@KEVINKAGWIMA/library?driver=SQL SERVER'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
  f = open("Book1.csv")
  reader = csv.reader(f)
  for id_number, title, author, category, price, quantity in reader:
    new_book = Books(
      book_id_number = id_number,
      title = title,
      author=author,
      category = category,
      price = price,
      quantity=quantity
    )
    db.session.add(new_book)
    db.session.commit()

if __name__ == '__main__':
  with app.app_context():
    main()
