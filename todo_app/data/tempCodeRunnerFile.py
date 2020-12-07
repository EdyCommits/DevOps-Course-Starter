  
    # def get_boards(self):
    #     boards_url = self.TRELLO_URL + '/members/me/boards'
    #     key_and_token = self.key_and_token
    #     headers = {"Accept": "application/json"}
    #     arguments = {'fields': 'name', 'lists': 'open'}
    #     response = requests.get(boards_url, params=key_and_token, data=arguments)
    #     print(response)
    #     json_response = response.json()
        
    #     for board in json_response:
    #         print(board['id'])