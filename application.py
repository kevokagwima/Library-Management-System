from time import strftime
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import *
import random, datetime
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql://@KEVINKAGWIMA/library?driver=SQL SERVER'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'oyamiminimzebeteng'
db.init_app(app)

@app.route("/", methods=["POST", "GET"])
def login():
  username = request.form.get("username")
  password = request.form.get("password")
  librarian = Librarian.query.filter_by(username=username).first()
  if librarian:
    if librarian.password == password:
      flash("Login successfull", category="success")
      session["librarian"] = librarian.username
      return redirect(url_for('home'))
    else:
      flash("Invalid password", category="danger")

  return render_template("login.html")

@app.route("/home")
def home():
  if "librarian" in session:
    sessions = session["librarian"]
    books = Books.query.all()
    bookings = Bookings.query.all()
    students = Student.query.all()
    staffs = Staff.query.all()
    todays_date = datetime.now().strftime("%Y-%m-%d")

    return render_template("index.html", sessions=sessions, books=books, bookings=bookings, students=students, todays_date=todays_date, staffs=staffs)

  return render_template("index.html")

@app.route("/new_student", methods=["POST", "GET"])
def add_student():
  new_student = Student(
    student_id_number = request.form.get("id_number"),
    first_name = request.form.get("first_name"),
    last_name = request.form.get("last_name"),
    student_class = request.form.get("student_class")
  )
  db.session.add(new_student)
  db.session.commit()
  new_booking = Bookings(
      booking_id_number = random.randint(100000,999999),
      issue_date = datetime.now(),
      book = request.form.get("book"),
      return_date = request.form.get("return_date"),
      student = new_student.id
  )
  db.session.add(new_booking)
  book = Books.query.filter_by(id=new_booking.book).first()
  if book.quantity == 0:
    flash("That book is not currently available", category="danger")
    return redirect(url_for('home'))
  book.quantity = book.quantity - 1
  db.session.commit()
  flash(f"Student {new_student.first_name} {new_student.last_name} has borrowed the book {book.title}", category="success")
  return redirect(url_for('home'))

@app.route("/new_staff", methods=["POST", "GET"])
def add_staff():
  new_staff = Staff(
    staff_id_number = request.form.get("id_number"),
    first_name = request.form.get("first_name"),
    last_name = request.form.get("last_name"),
    email_address = request.form.get("email_address"),
    phone_number = request.form.get("phone_number"),
  )
  db.session.add(new_staff)
  db.session.commit()
  new_booking = Bookings(
      booking_id_number = random.randint(100000,999999),
      issue_date = datetime.now(),
      book = request.form.get("book"),
      return_date = request.form.get("return_date"),
      staff = new_staff.id
  )
  db.session.add(new_booking)
  db.session.commit()
  book = Books.query.filter_by(id=new_booking.book).first()
  if book.quantity == 0:
    flash("That book is not currently available", category="danger")
    return redirect(url_for('home'))
  book.quantity = book.quantity - 1
  db.session.commit()
  flash(f"Staff {new_staff.first_name} {new_staff.last_name} has borrowed the book {book.title}", category="success")

  return redirect(url_for('home'))

@app.route("/return-book/<int:booking_id>")
def return_book(booking_id):
  booking = Bookings.query.get(booking_id)
  book = Books.query.filter_by(id=booking.book).first()
  book.quantity = book.quantity + 1
  db.session.delete(booking)
  db.session.commit()
  flash("Book returned successfully", category="success")
  return redirect(url_for('home'))

@app.route("/add-book", methods=["POST", "GET"])
def add_book():
  new_book = Books(
    book_id_number = request.form.get("id-number"),
    title = request.form.get("book-title"),
    author = request.form.get("book-author"),
    category = request.form.get("book-category"),
    price = request.form.get("book-price"),
    quantity = request.form.get("book-quantity")
  )
  db.session.add(new_book)
  db.session.commit()
  flash(f"The book titled {new_book.title} has been added successfully", category="success")
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
