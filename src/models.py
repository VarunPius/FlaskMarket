from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Database object model ##
class Item(db.Model):
    idx = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=True)

    def __repr__(self):
        return f'Item {self.name}\'s price is {self.price}'
