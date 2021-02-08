import pytest
from todo_app.data.view_model import ViewModel
from todo_app.data.boards import Card

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

def make_card(identifier, name):
    return Card({'id': identifier, 'name': name})
