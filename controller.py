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
    if len(field['community_cards']) >= 4:
        clear_cards = field['hand'] + field['community_cards']
        if sum(countval.calculate(cards) for cards in itertools.combinations(clear_cards, 5)) > 100:
            action['action_name'] = 'bet'
            action['amount'] = min(100, int(field['stack'] / 2))
        else:
            action['action_name'] = 'fold'
    else:
        action['action_name'] = 'bet'
        action['amount'] = 0
    return action
