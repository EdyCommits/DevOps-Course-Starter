import pytest
from todo_app.data.view_model import ViewModel
from todo_app.data.boards import Card
from datetime import datetime

def test_empty_items():
    vm = ViewModel([])
    
    assert vm.to_do_items == []
    assert vm.doing_items == []
    assert vm.done_items == []

def test_to_do_items():
    card1 = make_card('id 1', 'name 1')
    card2 = make_card('id 2', 'name 2')
    card3 = make_card('id 3', 'name 3')
    card4 = make_card('id 4', 'name 4')
    
    to_do_list = {'name': 'To Do', 'cards': [card1]}
    doing_list = {'name': 'In Progress', 'cards': [card2]}
    done_list = {'name': 'Done', 'cards': [card3]}
    any_list = {'name': 'ANY', 'cards': [card4]}
    
    vm = ViewModel([to_do_list, doing_list, done_list, any_list])
    
    assert vm.to_do_items == [card1]
    assert vm.doing_items == [card2]
    assert vm.done_items == [card3]
    
def test_number_of_done_items():
    card1 = make_card('id 1', 'name 1', '2021-02-14')
    card2 = make_card('id 2', 'name 2', '2021-02-15')
    
    done_list = {'name': 'Done', 'cards': [card1, card2]}
    
    vm = ViewModel([done_list])
    
    assert vm.count_done_items() == 2
    
def test_recent_done_items():
    card1 = make_card('id 1', 'name 1', '2021-02-14T10:03:29.527Z')
    card2 = make_card('id 2', 'name 2', '2021-02-15T11:03:29.527Z')
    card3 = make_card('id 3', 'name 3', '2021-02-15T15:03:29.527Z')
    card4 = make_card('id 4', 'name 4', '2021-02-16T12:03:29.527Z')
    card5 = make_card('id 5', 'name 5', '2021-02-15T04:03:29.527Z')
    card6 = make_card('id 6', 'name 6', '2021-02-15T02:03:29.527Z')
    today = datetime.fromisoformat('2021-02-15').date()
    
    done_list = {'name': 'Done', 'cards': [card1, card2, card3, card4, card5, card6]}
    
    vm = ViewModel([done_list])
    
    assert vm.recent_done_items(today) == [card2, card3, card5, card6]
    
def test_older_done_items():
    card1 = make_card('id 1', 'name 1', '2021-02-14T10:03:29.527Z')
    card2 = make_card('id 2', 'name 2', '2021-02-15T11:03:29.527Z')
    card3 = make_card('id 3', 'name 3', '2021-02-15T15:03:29.527Z')
    card4 = make_card('id 4', 'name 4', '2021-02-16T12:03:29.527Z')
    card5 = make_card('id 5', 'name 5', '2021-02-17T04:03:29.527Z')
    card6 = make_card('id 6', 'name 6', '2021-02-12T02:03:29.527Z')
    today = datetime.fromisoformat('2021-02-16').date()
    
    done_list = {'name': 'Done', 'cards': [card1, card2, card3, card4, card5, card6]}
    
    vm = ViewModel([done_list])
    
    assert vm.older_done_items(today) == [card1, card2, card3, card6]
    
def test_show_all_done_items():
    card1 = make_card('id 1', 'name 1')
    card2 = make_card('id 2', 'name 2')
    card3 = make_card('id 3', 'name 3')
    card4 = make_card('id 4', 'name 4')
    
    done_list = {'name': 'Done', 'cards': [card1, card2, card3, card4]}
    
    vm = ViewModel([done_list])
    
    assert vm.show_all_done_items == True
    
    card1 = make_card('id 1', 'name 1')
    card2 = make_card('id 2', 'name 2')
    card3 = make_card('id 3', 'name 3')
    card4 = make_card('id 4', 'name 4')
    card5 = make_card('id 5', 'name 5')
    
    done_list = {'name': 'Done', 'cards': [card1, card2, card3, card4, card5]}
    
    vm = ViewModel([done_list])
    
    assert vm.show_all_done_items == False
    
     

def make_card(identifier, name, last_edited='2021-02-15'):
    return Card({'id': identifier, 'name': name, 'dateLastActivity': last_edited })
