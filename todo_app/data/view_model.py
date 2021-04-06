from functools import reduce
from datetime import datetime
from dateutil import parser

class ViewModel:
    def __init__(self, items):
        self._to_do_items = self.select('To Do', items)
        self._doing_items = self.select('In Progress', items)
        self._done_items = self.select('Done', items)
        
    @property
    def to_do_items(self):
        return self._to_do_items
    
    @property
    def doing_items(self):
        return self._doing_items
    
    @property
    def done_items(self):
        return self._done_items
    
    @property
    def show_all_done_items(self):
        if len(self.done_items) < 5:
            return True
        else:
            return False
    
    def count_done_items(self):
        number_of_done_items = len(self.done_items)
        
        return number_of_done_items 

    def recent_done_items(self, today=datetime.utcnow().date()):
        recent_done_items = []        
        for item in self.done_items:
            item_last_updated =  parser.isoparse(item.last_updated).date()
            if (item_last_updated == today):
                recent_done_items.append(item)
                
        return recent_done_items
    
    def older_done_items(self, today=datetime.utcnow().date()):
        older_done_items = []        
        for item in self.done_items:
            item_last_updated =  parser.isoparse(item.last_updated).date()
            if (item_last_updated < today):
                older_done_items.append(item)

        return older_done_items

    def select(self, name, items):
        return reduce(lambda acc, e : acc + (e['cards'] if e['name'] == name else []), items, [])
   