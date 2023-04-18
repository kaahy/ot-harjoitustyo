import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(10)

    def test_opens_pointed_card(self):
        self.game.point_card(6)
        self.game.open_card()

        self.assertEqual(str(self.game.state["openCards"][0]), str(6))

    def test_does_not_open_more_than_two_cards(self):
        self.game.point_card(1)
        self.game.open_card()
        self.game.point_card(2)
        self.game.open_card()
        self.game.point_card(3)
        self.game.open_card()

        self.assertEqual(len(self.game.state["openCards"]), 1)
