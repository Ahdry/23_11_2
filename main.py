import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1

        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    break  # выходим из цикла, чтобы не итерироваться по изменяющемуся списку

        return finishers


    class TournamentTest(unittest.TestCase):
        all_results = {}

        @classmethod
        def setUpClass(cls):
            cls.all_results = {}

        def setUp(self):
            self.runner1 = Runner("Усэйн", speed=10)
            self.runner2 = Runner("Андрей", speed=9)
            self.runner3 = Runner("Ник", speed=3)

        @classmethod
        def tearDownClass(cls):
            for key in sorted(cls.all_results.keys()):
                print(f"{key}: {cls.all_results[key]}")

        def test_race_usain_nick(self):
            tournament = Tournament(90, self.runner1, self.runner3)
            results = tournament.start()
            cls.all_results[max(results.keys())] = results[max(results.keys())].name
            self.assertTrue(cls.all_results[max(results.keys())] == "Усэйн")

        def test_race_andrey_nick(self):
            tournament = Tournament(90, self.runner2, self.runner3)
            results = tournament.start()
            cls.all_results[max(results.keys())] = results[max(results.keys())].name
            self.assertTrue(cls.all_results[max(results.keys())] == "Андрей")

        def test_race_usain_andrey_nick(self):
            tournament = Tournament(90, self.runner1, self.runner2, self.runner3)


            results = tournament.start()

    cls.all_results[max(results.keys())] = results[max(results.keys())].name
    self.assertTrue(cls.all_results[max(results.keys())] == "Андрей")

if __name__ == "__main__":
    unittest.main()
