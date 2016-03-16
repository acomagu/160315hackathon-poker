import connection
import countval
import time
import itertools

def trigger():
    while(True):
        time.sleep(1)
        field = connection.get_field()
        if field['your_turn']:
            connection.act(get_action(field))

def get_action(field):
    action = {'action_name': None, 'amount': None}
    if field['community_cards']:
        clear_cards = field['hand'] + field['community_cards']
        if sum(countval.calculate(cards) for cards in itertools.combinations(clear_cards, 5)) > 10:
            action['action_name'] = 'bet'
            action['amount'] = 10
        else:
            action['action_name'] = 'fold'
    else:
        action['action_name'] = 'bet'
        action['amount'] = 10
    return action
