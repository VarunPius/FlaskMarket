####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# Internal Modules:
from market import db


####################################################################################################
# Database object models                                                                          ##
####################################################################################################

## User object model ##
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    pwd_hash = db.Column(db.String(length=60), nullable=False)
    wallet = db.Column(db.Integer(), nullable=False, default = 10)
    owns = db.relationship('Item', backref='owned_user', lazy=True) #backref provides way to back reference relationship. 
                                                    #Here, User owns Item hence the `owns` as relationship.
                                                    #But with backref you can query from Item which User owns the item
                                                    #lazy=True tells SQLAlchemy to grab everything in one shot
                                                    # This won't be a separate column but just a relationship and hence db.relationship and not db.Column

## Item object model ##
class Item(db.Model):
    idx = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}\'s price is {self.price}'
