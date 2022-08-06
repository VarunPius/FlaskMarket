####################################################################################################
# Imports                                                                                         ##
####################################################################################################

# External modules:
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

# Internal Modules:
from market import app
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, BuyItemForm, SellItemForm
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
@app.route("/market", methods=['GET', 'POST'])
@login_required
def market_page():
    buy_form = BuyItemForm()
    
    """
    if buy_form.validate_on_submit():
        #print(buy_form)             #will display form object in server-side cli/terminal
        #print(buy_form.__dict__)    #will display all key value pairs available in object
        #print(buy_form['submit'])
        print(request.form.get('purchased_item'))    # will return parameter of item passed in the item_modal.html file at:
                                                     # <input id="purchased_item" name="purchased_item" type="hidden" value="{{ item.idx }}">
                                                     # Here, it will be item.idx
    """
    
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_obj = Item.query.filter_by(idx=purchased_item).first()
        if p_item_obj:
            if current_user.can_purchase(p_item_obj):
                #p_item_obj.owner = current_user.id     #will move this n next 2 lines to item model
                #current_user.wallet -= p_item_obj.price
                #db.session.commit()
                p_item_obj.buy(current_user)
                flash(f"You now own {p_item_obj.name} for {p_item_obj.price}. Congratulations!", category = "success")
            else:
                flash(f"Not enough funds. Add more money to wallet", category = "danger")
            
            return redirect(url_for('market_page'))

    if request.method == "GET":
        #items = Item.query.all()   # will display all items
        items = Item.query.filter_by(owner=None)
        return render_template('market.html', items=items, buy_form = buy_form)
    
    """
    We segregated the method with request.method because of form resubmission.
    Without that, the form keeps resubmitting everytime you refresh and it keeps deducting money.
    This makes it impossible to refresh the market page once you have hit buy item.
    Now, you can refresh page because buy item is a POST requst while refresh will be a GET request
    """
    
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
    form = RegisterForm()       # Defined inside forms.py
    if form.validate_on_submit():
        user_to_create = User(username = form.user_name.data,
                              email = form.email_address.data,
                              #pwd_hash = form.password1.data
                              password = form.password1.data)   #password here is the @property
        db.session.add(user_to_create)
        db.session.commit()

        # next 2 lines added because market page is a restricted page and we need to ensure user is logged in
        # else we will be redirected to login page to login with this newly created user.
        # it's just a matter of inconvenience
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Error in creating user: {err_msg}", category='danger')



    return render_template('register.html', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.user_name.data).first()
        if attempted_user and attempted_user.check_pwd(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Login successful for {attempted_user.username}', category='success')

            return redirect(url_for('market_page'))
        else:
            flash('Username and/or password did not match. Please try again', category='danger')

    return render_template('login.html', form = form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out", category='info')
    return redirect(url_for('home_page'))


## Custom static data ##
'''
This method is used for showing images.
In production, you don't want Flask server serving images. 
Instead you set up NGINX or appropriate web server to do it

In Dev, we do this with `url_for` pointing to this method to serve image
'''
@app.route('/static/<path:filename>')
def custom_static(filename):
    #return send_from_directory(app.config['CUSTOM_STATIC_PATH'], filename) # this works too
    return send_from_directory(app.static_folder, filename)                 # this works too
