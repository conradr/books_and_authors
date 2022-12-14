from flask import Flask, render_template
from controllers.book_controller import book_blueprint
from controllers.author_controller import author_blueprint

app = Flask(__name__)

app.register_blueprint(author_blueprint)
app.register_blueprint(book_blueprint)


@app.route('/')
def home():
    return render_template('index.html')
