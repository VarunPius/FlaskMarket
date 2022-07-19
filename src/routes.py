# Home page
@app.route("/")
@app.route("/home")
def home_page():
    #return "<p>Marketplace Home Page!</p>".format(__name__)
    return render_template('home.html')

# Profile Page
@app.route("/profile/<user>")
def profile_page(user):
    return "<p>Hello {}</p>".format(user)

# Market page
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
