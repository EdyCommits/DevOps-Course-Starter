from configparser import ConfigParser
from .boards import *
from todo_app.config import *
import os
import requests


class TrelloAPI():
    TRELLO_URL = 'https://api.trello.com/1'
    
    def __init__(self):
        self.key_and_token = {'key':APIConfig.KEY,'token':APIConfig.TOKEN}
    
    def get_boards(self):
        boards_url = self.TRELLO_URL + '/members/me/boards'
        key_and_token = self.key_and_token
        headers = {"Accept": "application/json"}
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(boards_url, params=key_and_token, data=arguments)
        print(response)
        json_response = response.json()
        
        for board in json_response:
            print(board['name'])
        return json_response
    
    
    def get_list_of_items(self):
        boardId = "oIJEvych"
        cards_url = self.TRELLO_URL + '/boards/' + boardId + '/cards/'
        key_and_token = self.key_and_token
        headers = {"Accept": "application/json"}
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(cards_url, params=key_and_token, data=arguments)
        print(response)
        json_response = response.json()
    
        return json_response
    
    def get_lists(self, id): 
        lists_on_boards = self.get_list_of_items()
        boardId = "oIJEvych"
        lists_url = self.TRELLO_URL + '/boards/' + boardId + '/lists'
        headers = {"Accept": "application/json"}
        key_and_token = self.key_and_token
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(lists_url, params=key_and_token, data=arguments)
        print(response)
        json_response = response.json()
        
        for board in json_response:
            print(board['name'])
            print(lists_on_boards)
        return json_response
 

    def add_item(self, title):
        url = "https://api.trello.com/1/cards"
        id_list = '5fc54755646b4012c1387e8b'
        query = {
        'key': APIConfig.KEY,
        'token': APIConfig.TOKEN,
        'idList': id_list
        }
        name = title
        description = 'I made this card using the Trello API :fist:'

        arguments = {'name': name,  'desc': description, 'idList' : id_list}
        
        response = requests.request(
         "POST",
         url,
         params=query,
         data=arguments 
        )  
        print(response.text)

    
    def to_list(self, json_response: list) -> list :
        list_of_items =[]
        for element in json_response:
            list_of_items.append(element)
        print(list_of_items)
        
        return list_of_items
              