from flask import render_template, request, redirect, url_for, session
from app import app, products, users


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            session['cart'] = {}
            return redirect(url_for('index'))
        else:
            return 'Login Failed'
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        return redirect(url_for('login'))

    cart = session['cart']
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))


@app.route('/cart')
def show_cart():
    if 'cart' not in session:
        return redirect(url_for('login'))

    cart_items = {}
    total_price = 0
    for product_id, quantity in session['cart'].items():
        product = products[product_id]
        cart_items[product_id] = {'name': product['name'], 'quantity': quantity, 'price': product['price']}
        total_price += product['price'] * quantity

    return render_template('cart.html', cart=cart_items, total_price=total_price)


