from flask import Flask, redirect, render_template, request
from todo_app.flask_config import Config
from todo_app.data import session_items
from todo_app.data.api import TrelloAPI


app = Flask(__name__)
api = TrelloAPI()

@app.route('/')
def index():
    lists_on_board = api.get_lists()
    for aList in lists_on_board:
        list_id = aList['id']
        aList['cards'] = api.get_cards_for_lists(list_id)
    return render_template('index.html', items=lists_on_board)

@app.route('/add', methods=['GET'])
def add():
    return render_template('form.html')

@app.route('/add', methods=['POST'])
def post_item():
    title = request.form.get('title')
    # print(title)
    api.add_item(title=title)
    return redirect('/')

@app.route('/complete_item', methods=["GET"])
def update_progress():
    id = request.args['id']
    task = request.args['name']
    
    return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run()
