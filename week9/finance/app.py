import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userData = db.execute(
        "SELECT symbol, SUM(amount) as amount FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(amount) > 0", session["user_id"])
    sumPrices = 0
    balance = db.execute(
        "SELECT cash FROM users WHERE id = ?", session["user_id"])
    for row in userData:
        sharePrice = lookup(row["symbol"])
        row["priceForOne"] = usd(sharePrice["price"])
        row["name"] = sharePrice["name"]
        row["price"] = usd(sharePrice["price"] * row["amount"])
        sumPrices += sharePrice["price"] * row["amount"]
    total = usd(sumPrices + balance[0]["cash"])
    return render_template("index.html", userData=userData, total=total, balance=usd(balance[0]["cash"]))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        if not symbol or not shares:
            return apology("must enter stock's symbol/amount of shares", 400)
        if lookup(symbol) == None:
            return apology("No stocks were found", 400)
        if not request.form.get("shares").isnumeric():
            return apology("must enter a number", 400)
        if int(shares) < 0 or int(shares) % 1 != 0:
            return apology("must enter a positive number", 400)
        # If everything is correct:
        else:
            balance = db.execute(
                "SELECT cash FROM users WHERE id = ?", session["user_id"])
            stock = lookup(symbol)
            boughtFor = int(stock["price"]) * int(shares)
            # If user can not afford stocks:
            if boughtFor > balance[0]["cash"]:
                return apology("cash not enough for completing transaction", 400)
            else:
                db.execute("UPDATE users SET cash = cash - ? WHERE id = ?",
                           boughtFor, session["user_id"])
                db.execute("INSERT into transactions (user_id, symbol, price, action, amount) VALUES (?, ? ,?, ?, ?)",
                           session["user_id"], symbol, boughtFor, "buy", int(shares))
                return redirect("/")
    return apology("error", 404)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT symbol, amount, time FROM transactions WHERE user_id = ?", session["user_id"])
    for row in transactions:
        row["priceForOne"] = usd(lookup(row["symbol"])["price"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # If user routed via GET:
    if request.method == "GET":
        return render_template("quote.html")
    # If user submitted form on the page (i.e. reached /quote via POST)
    elif request.method == "POST":
        symbol = request.form.get("symbol").upper()
        if not symbol:
            return apology("must type a symbol", 400)
        else:
            # If symbol doesn't exist:
            if lookup(symbol) == None:
                return apology("No stocks were found", 400)
            else:
                data = lookup(symbol)
                price = usd(data["price"])
                # If everything is correct, output 'quoted.html' and inject there variables
                # for the 1)stock's symbol and 2)dictionary with stock's data
                return render_template("quoted.html", symbol=symbol, data=lookup(symbol), price=price)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")
        # If user doesnt type an username:
        if not name:
            return apology("must provide an username", 400)
        # If user doesnt type a password:
        elif not password:
            return apology("must provide an password", 400)
        # If user doesnt confirm the password:
        elif not confirm:
            return apology("must confirm a password", 400)
        # If username already exists:
        elif len(db.execute("SELECT username from users WHERE username = ?;", name)) != 0:
            return apology("user already exsists", 400)
        # If passwords do not match:
        elif not password == confirm:
            return apology("passwords do not match", 400)
        # If there are no errors(else):
        else:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                       name, generate_password_hash(password))
            return redirect("/login")
    if request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        listOfSym = db.execute(
            "SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(amount) > 0", session["user_id"])
        return render_template("sell.html", listOfSym=listOfSym)
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))
        ownsShares = db.execute(
            "SELECT symbol, SUM(amount) as amount FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(amount) > 0", session["user_id"])[0]["amount"]
        if not symbol or not shares:
            return apology("must enter stock's symbol/amount of shares", 400)
        if not request.form.get("shares").isnumeric():
            return apology("must enter a number", 400)
        if shares < 0 or shares % 1 != 0:
            return apology("must enter a positive number", 400)
        # If user sells more shares as has:
        if ownsShares < shares:
            return apology("you don't have that much shares", 400)
        # If everything is correct:
        else:
            stock = lookup(symbol)
            soldFor = int(stock["price"]) * shares
            db.execute("UPDATE users SET cash = cash + ? WHERE id = ?",
                       soldFor, session["user_id"])
            db.execute("INSERT into transactions (user_id, symbol, price, action, amount) VALUES (?, ? ,?, ?, ?)",
                       session["user_id"], symbol, soldFor, "sell", -shares)
            return redirect("/")
