from unittest import TestCase
from main.ww import DeckGenerator


class TestDeckGenerator(TestCase):
    def test_deck_generation(self):
        instance = DeckGenerator()
        deck = instance.deck_generation()

