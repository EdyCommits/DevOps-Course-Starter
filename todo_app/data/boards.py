
class Board():
    board_id = '' 
    board_name = '' 
    board_statuses = '' 
    def __init__(self, board_object = {}):
        self.id = board_object.get(self.board_id,'') 
        self.name = board_object.get(self.board_name,'') 
        self.statuses = {} 

class BoardStatus():
    boardstatus_id = ''
    boardstatus_name = ''
    boardstatus_pos = ''
    def __init__(self, status = {}):
        self.id = status.get(self.boardstatus_id,'')
        self.name = status.get(self.boardstatus_name,'')
        self.pos = status.get(self.boardstatus_pos,'')

class Card():
    identifier = ''
    name = ''
    last_updated = ''

    def __init__(self, item_dict = {}):
        self.identifier = item_dict['id']
        self.name = item_dict['name']
        self.last_updated = item_dict['dateLastActivity']
       