from project1 import organize_data, get_date, get_total

def test_organize_data():
    assert organize_data(['eunice', 'pasig'], [['keyboard', '1', '400']]) == {'name': 'eunice', 'address': 'pasig', 'product': [{'name': 'keyboard', 'quantity': '1', 'price': '400'}]}
    assert organize_data(['eunice', 'pasig'], [['keyboard', '1', '400'], ['mouse', '1', '250']]) == {'name': 'eunice', 'address': 'pasig', 'product': [{'name': 'keyboard', 'quantity': '1', 'price': '400'}, {'name': 'mouse', 'quantity': '1', 'price': '250'}]}


def test_get_date():
    assert get_date('2024-02-02') == ('February 2, 2024', 'May 2, 2024')


def test_get_total():
    assert get_total(
        {'name': 'eunice', 'address': 'pasig ',
         'product': [{'name': 'keyboard', 'quantity': '1', 'price': '400'},
                     {'name': 'mouse', 'quantity': '1', 'price': '250'}]
        }) == 650
    assert get_total(
        {'name': 'eunice', 'address': 'pasig ',
         'product': [{'name': 'keyboard', 'quantity': '2', 'price': '400'},
                     {'name': 'mouse', 'quantity': '2', 'price': '250'}]
        }) == 1300
