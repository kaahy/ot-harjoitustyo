from random import shuffle
from time import time

class Game:
    # pelin toiminnallisuuksia

    def __init__(self, pairs):
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

    # osoittaa haluttua korttia, kunhan se on olemassa (+ sulkee ensin mahdollisen aiemman parin)
    def point_card(self, card_id):
        if len(self.state["openCards"]) >= 2:
            self.close_cards()
        if card_id in range(self.pairs*2):
            self.state["pointedCard"] = card_id

    # avaa osoitettavana olevan kortin, kunhan se on vapaana (eli ei joko avattu tai löydetty)
    # päivittää tarvittaessa listaa löydetyistä korteista
    # kasvattaa kääntöjen määrää tarvittaessa
    # päivittää keston
    def open_card(self):
        if self.state["pointedCard"] not in self.state["openCards"] + self.state["foundCards"]:
            self.state["openCards"].append(self.state["pointedCard"])
            self.state["duration"] = time() - self.state["start_time"]
            self.update_turns_if_needed()
        self.update_found_cards_if_needed()

    # päivittää löytyneiden korttien listaa tarvittaessa
    def update_found_cards_if_needed(self):
        # tarkistaa onko avattuja kortteja kaksi. jos on, onko ne samat. jos on, tallennus
        if len(self.state["openCards"]) == 2:
            if self.compare_cards():
                self.state["foundCards"] += self.state["openCards"]

    def update_turns_if_needed(self):
        if len(self.state["openCards"]) == 1:
            self.state["turns"] += 1

    # tyhjentää avatut kortit (ei tarkoita löydettyjä)
    def close_cards(self):
        self.state["openCards"] = []

    # tarkistaa onko löytynyt pari (ts. avattu 2 samaa korttia)
    def compare_cards(self):
        if len(self.state["openCards"]) == 2:
            card1_id = self.state["openCards"][0]
            card2_id = self.state["openCards"][1]
            if self.state["cardContents"][card1_id] == self.state["cardContents"][card2_id]:
                return True
        return False

    # tarkistaa onko kaikki parit löydetty + päivittää samalla win-tiedon
    def check_win(self):
        if len(self.state["foundCards"]) == len(self.state["cardContents"]):
            self.state["win"] = True
            return True
        self.state["win"] = False
        return False
