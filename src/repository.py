class Repository:
    def __init__(self):
        self.file = "results.txt"

    def save_results(self, time, pairs, turns, duration):
        with open(self.file, "a") as file:
            file.write(f"\n{time} {pairs} {turns} {duration} {time}")

    def get_top_results(self, pairs, amount=-1):
        results = []

        with open(self.file) as file:
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
