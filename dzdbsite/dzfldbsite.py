import sqlite3
import os
from flask import Flask, render_template,  request, flash, g

from FDataBase import FDataBase


DATABASE = 'dzflsk.db'
DEBUG = True
SECRET_KEY = "82e21ff3005d8759fff364525eaf33d6570ec73f"



app = Flask(__name__)
app.config.from_object(__name__)


app.config.update(dict(DATABASE=os.path.join(app.root_path, 'dzflsk.db')))



def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.route("/")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu=dbase.get_menu())
@app.route("/katalog")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = dbase.get_menu(), title = "Pricing" ,posts=dbase.get_posts_annonce() )

@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['price'],  request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добавления курса", category="error")
            else:
                flash("Курс добавлен успешно", category="success")
        else:
            flash("Ошибка длины", category="error")
    return render_template("add_post.html", menu=dbase.get_menu(), title="Добавление курсов")

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())

@app.route("/post/<alias>")
def show_post(alias):
    db = get_db()
    dbase = FDataBase(db)
    title, price, post = dbase.get_post(alias)

    return render_template('post.html', menu=dbase.get_menu(),title=title, price=price, post=post)


if __name__ == '__main__':
    app.run()











