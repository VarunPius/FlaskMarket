####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# External Modules:
from flask_login import UserMixin

# Internal Modules:
from market import db, login_manager
from market import bcrypt


####################################################################################################
# Database object models                                                                          ##
####################################################################################################

'''
The following method is added because if you try to reach login page, it will give following error:
http://localhost:8000/login =>
Exception: Missing user_loader or request_loader. Refer to http://flask-login.readthedocs.io/#how-it-works for more info.

This is because you will need to provide a user_loader callback. 
This callback is used to reload the user object from the user ID stored in the session.
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


## User object model ##
# class User(db.Model):
class User(db.Model, UserMixin):
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

    @property
    def password(self):
        return self.password
    
    @password.setter        # property's name here to indicate which property is getting set (or get)
    def password(self, plain_txt_pwd):
        self.pwd_hash = bcrypt.generate_password_hash(plain_txt_pwd).decode('utf-8')

    def check_pwd(self, attempted_password):
        return bcrypt.check_password_hash(self.pwd_hash, attempted_password)
    
    @property
    def pretty_wallet(self):
        if len(str(self.wallet)) >= 4:
            process_wallet = str(self.wallet)
            process_wallet = process_wallet[::-1]
            str_wallet = ""
            for i, ch in enumerate(process_wallet):
                if i%3 != 0 or i == 0:
                    str_wallet += ch
                else:
                    str_wallet += "," + ch
            return str_wallet[::-1]
        else:
            return f"{self.wallet}"


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
