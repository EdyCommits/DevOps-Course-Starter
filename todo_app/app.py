from flask import Flask
from todo_app.flask_config import Config
from flask import render_template
from todo_app.data import session_items

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()
    
    print(items)
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run()
