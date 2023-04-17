import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(10)

    def test_opens_pointed_card(self):
        self.game.point_card(6)
        self.game.open_card()

        self.assertEqual(str(self.game.state["openCards"][0]), str(6))