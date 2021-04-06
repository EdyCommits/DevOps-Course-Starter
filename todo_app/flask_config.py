import os


class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.TRELLO_KEY = os.environ.get('TRELLO_KEY')
        self.TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
        self.BOARD_ID = os.environ.get('BOARD_ID')
        self.TO_DO_ID = os.environ.get('TO_DO_ID')
        self.DOING_ID = os.environ.get('DOING_ID')
        self.DONE_ID = os.environ.get('DONE_ID')
        
        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
