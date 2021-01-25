
class ViewModel:
    def __init__(self, items):
        self._items = items
    
    @property
    def lists_on_board(self):
        return self._items