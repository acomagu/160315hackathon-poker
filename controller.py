import connection
import time
import itertools

def trigger():
    while(True):
        time.sleep(1)
        field = connection.get_field()
        connection.act(get_action(field)) if field['your_turn']

def get_action(field):
    action = {'action_name': null, 'amount': null}
    if field['community_cards']:
        clear_cards = field['hand'] + field['community_cards']
        if sum(get_score(cards) for cards in itertools.combinations(clear_cards, 5)) > 10:
            action['action_name'] = 'bet'
            action['amount'] = 10
        else:
            action['action_name'] = 'fold'
    else:
        action['action_name'] = 'bet'
        action['amount'] = 10
    return action
