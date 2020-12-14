from flask import Flask, redirect, render_template, request
from todo_app.flask_config import Config
from todo_app.data import session_items
from todo_app.data.api import TrelloAPI


app = Flask(__name__)
api = TrelloAPI()

@app.route('/')
def index():
    list_of_items = api.get_list_of_items()
    items = api.to_list(list_of_items)
    print(items)
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET'])
def add():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def post_item():
    title = request.form.get('title')
    print(title)
    api.add_item(title=title)
    return redirect('/')

@app.route('/complete_item', methods=['GET'])
def update_progress():
    lists_on_board = api.get_lists(id)
    lists = api.to_list(lists_on_board)
    print(lists)
    return render_template('update.html', lists=lists)


if __name__ == '__main__':
    app.run()
