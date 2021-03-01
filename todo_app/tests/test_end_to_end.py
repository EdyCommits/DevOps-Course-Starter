import os
import pytest
from dotenv import find_dotenv , load_dotenv
from selenium import webdriver
from selenium import webdriver
from seleniumrequests import Chrome
from selenium.webdriver.support.ui import Select
from todo_app.data.api import TrelloAPI
from threading import Thread
from todo_app import app


def create_test_board():
    api = TrelloAPI()
    name = "Test Board"
    test_board = api.create_board(name)
    print(test_board.get('id'))
    return test_board.get('id')

def delete_temp_board(board_id):
    api = TrelloAPI()
    api.delete_board(board_id)
    
@pytest.fixture(scope='module')
def test_app():
    # Load the env file
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    
    # Create the new board & update the board id environment variable
    board_id = create_test_board()
    print(board_id)
    os.environ['BOARD_ID'] = board_id    
    
    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield app
    
    # Tear Down
    thread.join(1)
    delete_temp_board(board_id)
    
@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome("/usr/local/bin/chromedriver") as driver:
        yield driver
        
def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

    
    