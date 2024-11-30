from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")

@app.route("/menu")
def menu():
    pizzas = [
        {"name": "Маргарита", "ingredients": "Сир, томати, базилік", "price": "120грн"},
        {"name": "Піпероні", "ingredients": "Сир, пепероны, томатний соус", "price": "150грн"},
        {"name": "Гавайська", "ingredients": "Сир, шинка, ананаси", "price": "160грн"},
    ]
    return render_template("menu.html", pizzas=pizzas)

if __name__ == "__main__":
    app.run(port=5006, debug=True)