
class Board():
    board_id = '' 
    board_name = '' 
    board_statuses = '' 
    def __init__(self, board_object: dict = {}):
        self.id = board_object.get(self.board_id,'') 
        self.name = board_object.get(self.board_name,'') 
        self.statuses = {} 

class BoardStatus():
    boardstatus_id = ''
    boardstatus_name = ''
    boardstatus_pos = ''
    def __init__(self, status: dict = {}):
        self.id = status.get(self.boardstatus_id,'')
        self.name = status.get(self.boardstatus_name,'')
        self.pos = status.get(self.boardstatus_pos,'')

class Item():
    item_id = ''
    item_id_short = ''
    item_title = ''
    item_due_date = ''
    item_description = ''
    item_status = None
    def __init__(self, item_object: dict = {}):
        self.id = item_object.get(self.item_id, '')
        self.id_short = item_object.get(self.item_id_short, '')
        self.title = item_object.get(self.item_title, '')
        self.due_date = item_object.get(self.item_due_date, '')
        self.description = item_object.get(self.item_description, '')
        self.status = item_object.get(self.item_status, '')