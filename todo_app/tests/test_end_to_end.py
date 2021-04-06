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
    return test_board.get('id')

def create_test_list(board_id):
    api = TrelloAPI()
    name = "To Do"
    test_list = api.create_list(name, board_id)
    return test_list.get('id')

def delete_temp_board(board_id):
    api = TrelloAPI()
    board_id = board_id 
    api.delete_board(board_id)
    
@pytest.fixture(scope='module')
def test_app():
    # Load the env file
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)
    
    # Create the new board & update the board id environment variable
    board_id = create_test_board()
    list_id = create_test_list(board_id)
    
    os.environ['BOARD_ID'] = board_id    
    os.environ['TO_DO_ID'] = list_id    
     
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
    with webdriver.Chrome() as driver:
        yield driver
        
def test_task_journey(driver, test_app):
    home_url = 'http://localhost:5000/'
    driver.get(home_url)
    assert driver.title == 'To-Do App'
  
    button = driver.find_element_by_name("button")
    button.click()
    assert ('/add' in driver.page_source)
    
    assert driver.title == 'Add Task'
    
    form = driver.find_element_by_id('form')
    input_filed = form.find_element_by_name("title")
    input_filed.send_keys('test task')
    button = driver.find_element_by_name("button")
    button.click()
    assert ('test task' in driver.page_source)

    button = driver.find_element_by_name("move_to_doing")
    #click redirects to /complete_items? endpoint
    button.click()
    
    #clicks in /complete_items? endpoint
    button = driver.find_element_by_name("move_to_doing")
    button.click()
    
    driver.get(home_url)
    
    button = driver.find_element_by_id("move_to_done")
    #click redirects to /complete? endpoint
    button.click()
    
    #click in /complete? endpoint
    button = driver.find_element_by_id("move_to_done")
    button.click()

 #check item deleted
    button = driver.find_element_by_id("delete")
    button.click()
    assert ('test task' not in driver.page_source)


    
    
