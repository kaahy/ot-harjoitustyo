import unittest
from game.game import Game

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

    def test_counts_turns_correctly(self):
        turn_counts = []

        turn_counts.append(self.game.state["turns"])

        self.game.point_card(1)
        self.game.open_card()
        turn_counts.append(self.game.state["turns"])

        self.game.point_card(2)
        self.game.open_card()
        turn_counts.append(self.game.state["turns"])

        self.game.point_card(3)
        self.game.open_card()
        turn_counts.append(self.game.state["turns"])

        self.game.point_card(4)
        self.game.open_card()
        turn_counts.append(self.game.state["turns"])

        self.assertEqual(turn_counts, [0, 1, 1, 2, 2])

    def test_compares_correctly_when_pair_found(self):
        card_id1 = 0

        for i in range(1, len(self.game.state["cardContents"])):
            if self.game.state["cardContents"][0] == self.game.state["cardContents"][i]:
                card_id2 = i
                x = (self.game.state["cardContents"][0], self.game.state["cardContents"][i])
                break

        self.game.point_card(card_id1)
        self.game.open_card()

        self.game.point_card(card_id2)
        self.game.open_card()

        self.assertEqual(self.game.compare_cards(), True)

    def test_compares_correctly_when_pair_not_found(self):
        returns = []

        # avataan vain yksi kortti
        card_id1 = 0
        self.game.point_card(card_id1)
        self.game.open_card()
        returns.append(self.game.compare_cards())

        # avataan toinen, erilainen kortti
        for i in range(1, len(self.game.state["cardContents"])):
            if self.game.state["cardContents"][0] != self.game.state["cardContents"][i]:
                card_id2 = i
                x = (self.game.state["cardContents"][0], self.game.state["cardContents"][i])
                break
        self.game.point_card(card_id2)
        self.game.open_card()
        returns.append(self.game.compare_cards())

        self.assertEqual(returns, [False, False])

    def test_points_at_existing_cards_only(self):
        pointed_cards = []
        
        self.game.point_card(19)
        pointed_cards.append(self.game.state["pointedCard"])
        self.game.point_card(-1)
        self.game.point_card(20)
        pointed_cards.append(self.game.state["pointedCard"])
        self.game.point_card(0)
        pointed_cards.append(self.game.state["pointedCard"])

        self.assertEqual(pointed_cards, [19, 19, 0])

    def test_check_win(self):
        positions = [[] for _ in range(10)]

        for i in range(0, len(self.game.state["cardContents"])):
            content = self.game.state["cardContents"][i]
            positions[content].append(i)

        win_checks = []

        win_checks.append(self.game.check_win())

        for card_ids in positions:
            self.game.point_card(card_ids[0])
            self.game.open_card()

            self.game.point_card(card_ids[1])
            self.game.open_card()

        win_checks.append(self.game.check_win())
                      
        self.assertEqual(win_checks, [False, True])
