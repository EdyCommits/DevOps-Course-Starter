from dotenv import find_dotenv , load_dotenv
from todo_app import app
from mock import patch, Mock
import os
import pytest

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    print(file_path)
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
     # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client
        
@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')

    assert response.status_code == 200
   
        
@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/')

    assert response.status_code == 200

@patch('requests.get')
def test_add_page(mock_get_requests, client):
    mock_get_requests.side_effect = mock_get_lists
    response = client.get('/add')

    html_string = str(response.data)
    assert 'New Task' in html_string
    assert response.status_code == 200
    
def mock_get_lists(url, params, data=None):
    list_id = os.environ.get('TO_DO_ID')
    sample_trello_lists_response = [{'id' : list_id, 'name' : "to_do"}]
    sample_trello_cards_response = [{'id' : "card_id", 'name' : "to_do", 'dateLastActivity' : 'date'}]
     
    BOARD_ID = os.environ.get('BOARD_ID')
    if url == f'https://api.trello.com/1/boards/{BOARD_ID}/lists':
        response = Mock()
        response.json.return_value = sample_trello_lists_response
        return response
    if url == f'https://api.trello.com/1/lists/5fc54755646b4012c1387e8b/cards/':
        response = Mock()
        response.json.return_value = sample_trello_cards_response
        return response
    
  
    return None