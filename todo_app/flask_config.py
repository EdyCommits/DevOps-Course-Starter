import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TRELLO_KEY = os.environ.get('TRELLO_KEY')
    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    BOARD_ID = os.environ.get('BOARD_ID')
    TO_DO_ID = os.environ.get('TO_DO_ID')
    DOING_ID = os.environ.get('DOING_ID')
    DONE_ID = os.environ.get('DONE_ID')

    # if not SECRET_KEY:
    #     raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")
