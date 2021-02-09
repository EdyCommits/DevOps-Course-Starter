from functools import reduce

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

    def select(self, name, items):
        return reduce(lambda acc, e : acc + (e['cards'] if e['name'] == name else []), items, [])