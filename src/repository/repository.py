import os.path

class Repository:
    """Luokka, joka vastaa pysyvän tiedon tallentamisesta ja palauttamisesta.
    """

    def __init__(self):
        self.file = "results.txt"

    def save_results(self, time, pairs, turns, duration):
        """Tallentaa tulokset tiedostoon.

        Args:
            time (float): Aika nyt sekunteina.
            pairs (int): Vaikeustaso parien määränä.
            turns (int): Korttien avausten määrä.
            duration (float): Pelin kesto sekunteina.
        """

        with open(self.file, "a", encoding="utf-8") as file:
            file.write(f"\n{time} {pairs} {turns} {duration} {time}")

    def get_top_results(self, pairs, amount=-1):
        """Palauttaa tietyn vaikeustason parhaat tulokset parhausjärjestyksessä.

        Args:
            pairs (int): Pelin vaikeustaso parien määrällä ilmaistuna.
            amount (int, optional): Tulosten määrä.

        Returns:
            list: Arvot ovat listoja, joissa on korttien avausmäärä ja pelin kesto sekunteina.
        """

        results = []

        if os.path.isfile(self.file):

            with open(self.file, encoding="utf-8") as file:
                lines = file.read().splitlines()

            for line_ in lines:
                line = line_.split()
                if len(line) < 2:
                    continue

                if int(line[1]) == pairs:
                    turns = int(line[2])
                    duration = float(line[3])
                    results.append((turns, duration))

            results.sort()

        return results[:amount]
