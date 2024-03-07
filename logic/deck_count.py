from infra.api_wrapper import APIWrapper


class DeckEndPoints:

    def __init__(self, api_object):
        self.my_api = api_object

    def deck_api(self):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        return result

    def deck_api_json(self):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
        return result.json()

    def draw_cards(self, deck_id, count):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}')
        return result.json()

    def shuffle_cards(self, deck_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/?remaining=true')
        return result.json()

    def brand_new_deck(self, deck_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/{deck_id}/')
        return result.json()

    def partial_deck(self, deck_id):
        my_api = APIWrapper()
        result = my_api.api_get_request(
            f'https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/?cards=AS,2S,KS,AD,2D,KD,AC,2C,KC,AH,2H,KH')
        return result.json()

    def add_cards_to_pile(self, deck_id, pile_name, cards):
        my_api = APIWrapper()
        result = my_api.api_get_request(
            f'https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/add/?cards={cards}')
        return result.json()
