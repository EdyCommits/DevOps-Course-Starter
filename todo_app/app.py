from flask import Flask, redirect, render_template, request
from todo_app.flask_config import Config
from todo_app.data import session_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()

    print(items)
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET'])
def add():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def post_item():
    title = request.form.get('add')
    new_item = session_items.add_item(title=title)
    return redirect('/')



if __name__ == '__main__':
    app.run()
