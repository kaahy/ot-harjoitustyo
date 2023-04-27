class Repository:
    def __init__(self):
        self.file = "results.txt"

    def save_results(self, time, pairs, turns, duration):
        f = open(self.file, "a")
        f.write(f"\n{time} {pairs} {turns} {duration} {time}")
        f.close()

    def get_top_results(self, pairs, amount=-1):
        results = []

        with open(self.file) as f:
            lines = f.read().splitlines()

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