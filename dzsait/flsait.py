from flask import Flask, render_template, url_for, request


app = Flask(__name__)
menu = [
    {"name": "Ресторан one_loung", "url": "index"},
    {"name": "О нас", "url": "about"},
    {"name": "Забронировать столик", "url": "contact"},
    {"name": "Меню", "url": "menurest"}
]


@app.route("/")
@app.route("/index")
def index():
    print(url_for("index"))
    return render_template("index.html", title = "Ресторан one_loung", menu=menu)

@app.route("/about")
def about():
    return render_template("about.html", title = "О нас", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template('contact.html', title = "Забронировать столик", menu=menu)

@app.route("/menurest")
def menurest():
    return render_template('menu.html', title = "Меню", menu=menu)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
