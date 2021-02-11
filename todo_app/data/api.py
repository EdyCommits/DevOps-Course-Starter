from configparser import ConfigParser
from todo_app.flask_config import Config
from .boards import *
import os
import requests


class TrelloAPI():
    
    def __init__(self):
        self.TRELLO_URL = 'https://api.trello.com/1'
        self.key_and_token = {'key':Config.TRELLO_KEY,'token':Config.TRELLO_TOKEN}
        self.boardId = Config.BOARD_ID
        self.to_do_id = Config.TO_DO_ID
    
    def get_boards(self):
        boards_url = self.TRELLO_URL + '/members/me/boards'
        key_and_token = self.key_and_token
        headers = {"Accept": "application/json"}
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(boards_url, params=key_and_token, data=arguments)
        json_response = response.json()
        return json_response
    
    def get_lists(self): 
        boardId = self.boardId
        lists_url = self.TRELLO_URL + '/boards/' + boardId + '/lists'
        headers = {"Accept": "application/json"}
        key_and_token = self.key_and_token
        arguments = {'fields': 'name', 'lists': 'open',}
        response = requests.get(lists_url, params=key_and_token, data=arguments)
        lists = response.json()
        return lists

    def get_cards_for_lists(self, list_id):
        cards_url = self.TRELLO_URL + '/lists/' + list_id + '/cards/'
        key_and_token = self.key_and_token
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(cards_url, params=key_and_token,data=arguments)
        json_response = response.json()
        return list(map(Card, json_response))

    def add_item(self, title):
        url = self.TRELLO_URL + '/cards'
        # id_list = '5fc54755646b4012c1387e8b'
        id_list = self.to_do_id
        key_and_token = self.key_and_token
        name = title
        description = 'I made this card using the Trello API :fist:'
        arguments = {'name': name,  'desc': description, 'idList' : id_list} 
        response = requests.post(url, params=key_and_token, data=arguments)  
        
    def move_to_in_progress(self, card_id):
        id_list = '5fd147d780c9d384ae4455d1'
        url = self.TRELLO_URL + '/cards/' + card_id + '?idList=' + id_list
        key_and_token = self.key_and_token
        arguments = {'idList' : id_list}
        response = requests.put(url, params=key_and_token, data=arguments) 
    
    def move_to_done(self, card_id):
        id_list = '60217fe6b34350796ad4131e'
        url = self.TRELLO_URL + '/cards/' + card_id + '?idList=' + id_list
        key_and_token = self.key_and_token
        arguments = {'idList' : id_list}
        response = requests.put(url, params=key_and_token, data=arguments)  
    
    def delete(self, card_id):
        card_id = card_id        
        key_and_token = self.key_and_token
        url = self.TRELLO_URL + '/cards/' + card_id 
        response = requests.delete(url, params=key_and_token)
    
        
        
    def to_list(self, json_response: list):
        list_of_items = []
        for element in json_response:
            list_of_items.append(element)
            return list_of_items
              