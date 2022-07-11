from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Librarian(db.Model):
  __tablename__ = 'librarian'
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(30), nullable=False)
  password = db.Column(db.String(20), nullable=False)

class Student(db.Model):
  __tablename__ = 'student'
  id = db.Column(db.Integer(), primary_key=True)
  student_id_number = db.Column(db.String(10), nullable=False)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(20), nullable=False)
  student_class = db.Column(db.String(10), nullable=False)
  bookings = db.relationship("Bookings", backref="book-borrowing", lazy=True)

class Books(db.Model):
  __tablename__= 'books'
  id = db.Column(db.Integer(), primary_key=True)
  book_id_number = db.Column(db.String(10), nullable=False)
  title = db.Column(db.String(50), nullable=False)
  author = db.Column(db.String(30), nullable=False)
  category = db.Column(db.String(30), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  quantity = db.Column(db.Integer(), nullable=False)
  bookings = db.relationship("Bookings", backref="book-borrowed", lazy=True)

class Staff(db.Model):
  __tablename__ = 'staff'
  id = db.Column(db.Integer(), primary_key=True)
  staff_id_number = db.Column(db.String(10), nullable=False)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(20), nullable=False)
  email_address = db.Column(db.String(50), nullable=False)
  phone_number = db.Column(db.Integer(), nullable=False)
  bookings = db.relationship("Bookings", backref="staff-borrowing", lazy=True)

class Bookings(db.Model):
  __tablename__ = 'bookings'
  id = db.Column(db.Integer(), primary_key=True)
  booking_id_number = db.Column(db.String(10), nullable=False)
  issue_date = db.Column(db.Date(), nullable=False)
  return_date = db.Column(db.Date(), nullable=False)
  student = db.Column(db.Integer(), db.ForeignKey('student.id'))
  book = db.Column(db.Integer(), db.ForeignKey('books.id'))
  staff = db.Column(db.Integer(), db.ForeignKey('staff.id'))
