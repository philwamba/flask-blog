from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Phil Wamba',
        'title': 'First Blog Posts',
        'content': 'My first blog posts content',
        'date_posted': 'March, 20, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Posts',
        'content': 'My first blog posts content',
        'date_posted': 'March, 21, 2019'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title='Home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')
