from random import shuffle
from time import time

class Game:
    """Luokka, joka säilyttää ja muokkaa pelin tietoja.

    Attributes:
        pairs (int): Pelin vaikeustaso parien määrällä ilmaistuna.
    """

    def __init__(self, pairs):
        """Luokan konstruktori, joka alustaa pelin tilannetiedot.

        Args:
            pairs (int): Pelin vaikeustaso parien määrällä ilmaistuna.
        """

        self.pairs = pairs
        self.state = {}
        self.state["cardContents"] = list(range(self.pairs)) + list(range(self.pairs))
        self.state["pointedCard"] = 0 # 1 kpl
        self.state["openCards"] = [] # 0-2 kpl
        self.state["foundCards"] = []
        self.state["win"] = False # True, kun kaikki löydetty
        shuffle(self.state["cardContents"]) #testailuun: self.state["cardContents"].sort() ########
        self.state["turns"] = 0
        self.state["start_time"] = time()
        self.state["duration"] = 0

    def point_card(self, card_id):
        """Merkitsee pelaajan osoittaman kortin.

        Lisäksi, jos aiemmin oli auki kaksi korttia, sulkee ne.

        Args:
            card_id (int): Kortin tunnusluku.
        """

        if len(self.state["openCards"]) >= 2:
            self.close_cards()
        if card_id in range(self.pairs*2):
            self.state["pointedCard"] = card_id

    def open_card(self):
        """Merkitsee pelaajan osoittaman kortin avatuksi.

        Lisäksi päivittää pelin keston sekä tarvittaessa löydetyt kortit ja kääntöjen määrän.
        """

        if self.state["pointedCard"] not in self.state["openCards"] + self.state["foundCards"]:
            self.state["openCards"].append(self.state["pointedCard"])
            self.state["duration"] = time() - self.state["start_time"]
            self.update_turns_if_needed()
        self.update_found_cards_if_needed()

    def update_found_cards_if_needed(self):
        # jos on auki kaksi samaa korttia, lisätään ne löydettyihin kortteihin
        if len(self.state["openCards"]) == 2:
            if self.compare_cards():
                self.state["foundCards"] += self.state["openCards"]

    def update_turns_if_needed(self):
        if len(self.state["openCards"]) == 1:
            self.state["turns"] += 1

    def close_cards(self):
        self.state["openCards"] = []

    def compare_cards(self):
        """Tarkistaa, onko löytynyt pari eli onko auki kaksi samaa korttia.

        Returns:
            True, jos pari on löytynyt, muutoin False.
        """

        if len(self.state["openCards"]) == 2:
            card1_id = self.state["openCards"][0]
            card2_id = self.state["openCards"][1]
            if self.state["cardContents"][card1_id] == self.state["cardContents"][card2_id]:
                return True
        return False

    def check_win(self):
        """Tarkistaa, onko peli voitettu eli kaikki parit löydetty.

        Returns:
            True, jos peli on voitettu, muutoin False.
        """

        if len(self.state["foundCards"]) == len(self.state["cardContents"]):
            self.state["win"] = True
            return True
        self.state["win"] = False
        return False
