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
    api.add_item(title=title)
    return redirect('/')

@app.route('/complete_items', methods=["GET", "PUT"])
def update_progress():
    card_id = request.args['card_id']
    name = request.args['name']
    api.move_to_in_progress(card_id)    

    return render_template('update.html', task=name)


@app.route('/', methods=["PUT"])
def move_to_in_progress():
    card_id = request.args['card_id']
    api.move_to_in_progress(card_id)    
    return ("index.html")

@app.route('/delete', methods=["GET", "DELETE"])
def delete():
    card_id = request.args['card_id']
    print(card_id)
    api.delete(card_id)   
    return redirect('/')


if __name__ == '__main__':
    app.run()
