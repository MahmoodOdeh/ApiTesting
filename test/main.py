import unittest

from infra.api_wrapper import APIWrapper
from logic.deck_count import DeckEndPoints


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.my_api = APIWrapper()

    def test_check_status_code_in_deck(self):
        api_logic = DeckEndPoints(self.my_api)
        result = api_logic.deck_api()
        self.assertTrue(result.ok)

    def test_check_draw_card(self):
        api_logic = DeckEndPoints(self.my_api)
        new_deck = api_logic.deck_api_json()
        deck_id = new_deck["deck_id"]
        json_data = api_logic.draw_cards(deck_id=deck_id, count=2)
        self.assertEqual(json_data['remaining'], 50)

    def test_draw_cards(self):
        api_logic = DeckEndPoints(self.my_api)
        new_deck = api_logic.deck_api_json()
        deck_id = new_deck["deck_id"]
        json_data = api_logic.draw_cards(deck_id=deck_id, count=2)
        self.assertTrue(json_data["success"])

        expected_remaining = 52 - len(json_data["cards"])
        self.assertEqual(json_data["remaining"], expected_remaining)

        for card in json_data["cards"]:
            self.assertIn("value", card)
            self.assertIn("suit", card)
            self.assertIn("code", card)
            self.assertIn("image", card)
            self.assertIn("images", card)

    def test_check_shuffle_deck(self):
        api_logic = DeckEndPoints(self.my_api)
        new_deck = api_logic.deck_api_json()
        deck_id = new_deck["deck_id"]
        json_data = api_logic.shuffle_cards(deck_id=deck_id)
        self.assertEqual(json_data['remaining'], 52)
        self.assertTrue(json_data['shuffled'], "The deck not shuffled")

    def test_check_brand_new_deck(self):
        api_logic = DeckEndPoints(self.my_api)
        new_deck = api_logic.deck_api_json()
        deck_id = new_deck["deck_id"]
        json_data = api_logic.brand_new_deck(deck_id=deck_id)
        self.assertEqual(json_data['remaining'], 52)
        self.assertTrue(json_data['shuffled'], "The deck not shuffled")

    def test_check_partial_deck(self):
        api_logic = DeckEndPoints(self.my_api)
        new_deck = api_logic.deck_api_json()
        deck_id = new_deck["deck_id"]
        json_data = api_logic.partial_deck(deck_id=deck_id)
        self.assertEqual(json_data['remaining'], 12)
        self.assertTrue(json_data['shuffled'], "The deck not shuffled")
