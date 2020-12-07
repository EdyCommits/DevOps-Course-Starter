from configparser import ConfigParser
from .boards import *
from todo_app.config import *
import os
import requests


class TrelloAPI():
    TRELLO_URL = 'https://api.trello.com/1'
    
    def __init__(self):
        self.object()    
        self.key_and_token = {'key':APIConfig.KEY,'token':APIConfig.TOKEN}
    
    def get_boards(self):
        boards_url = self.TRELLO_URL + '/members/me/boards'
        print(boards_url)
        key_and_token = self.key_and_token
        headers = {"Accept": "application/json"}
        arguments = {'fields': 'name', 'lists': 'open'}
        response = requests.get(boards_url, params=key_and_token, data=arguments)
        print(response)
        json_response = response.json()
        
        for board in json_response:
            print(board['name'])
              
    def object(self):
        Item.item_id = 'id'
        Item.item_id_short = 'idShort'
        Item.item_title = 'name'
        Item.item_due_date = 'due'
        Item.item_description = 'desc'
        Item.item_status = 'idList'
        BoardStatus.boardstatus_id = 'id'
        BoardStatus.boardstatus_name = 'name'
        BoardStatus.boardstatus_pos = 'pos'
        Board.board_id = 'id'
        Board.board_name = 'name'
        Board.board_statuses = 'lists'