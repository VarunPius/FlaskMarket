####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# External modules:
from flask import render_template, redirect, url_for, flash, get_flashed_messages

# Internal Modules:
from market import app
from market.models import Item, User
from market.forms import RegisterForm
from market import db


####################################################################################################
# Code start                                                                                      ##
####################################################################################################

## Home page ##
@app.route("/")
@app.route("/home")
def home_page():
    #return "<p>Marketplace Home Page!</p>".format(__name__)
    return render_template('home.html')

## Profile Page ##
@app.route("/profile/<user>")
def profile_page(user):
    return "<p>Hello {}</p>".format(user)

## Market page ##
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)
    #items = [
    #    {'id': 1, 'name': 'iPhone', 'code': 'A123QR', 'price': 1000},
    #    {'id': 2, 'name': 'Laptop', 'code': 'A124QD', 'price': 1500},
    #    {'id': 3, 'name': 'Camera', 'code': 'b325rQ', 'price': 600},
    #    {'id': 4, 'name': 'Watch', 'code': 'c486xZ', 'price': 400}
    #]
    # data sent here to template via Jinja Templates
    #return render_template('market.html', item_name="iPhone")

## Registration page ##
# we added methods here in the annotation and not in Homepage because in the HTML page
# we are pushing data via POST method.
# If we don;t add this, we will get a "Method not Allowed" error in the HTML page.
# It will render the register page, but the error will pop-up when we try to submit as it tries to send POST data
@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.user_name.data,
                              email = form.email_address.data,
                              pwd_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error in creating user: {err_msg}", category='danger')



    return render_template('register.html', form = form)
