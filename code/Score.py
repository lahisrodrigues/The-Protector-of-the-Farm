from code.Const import SCORE_LOSE_ANIMAL

class Score:
    def __init__(self):
        self.points = 0

    def add_strike(self, enemy_name):
        if enemy_name == "DogPredator":
            self.points += 150 # Cachorro vale mais!
        elif enemy_name == "FoxPredator":
            self.points += 100

    def lose_animal(self):
        self.points -= SCORE_LOSE_ANIMAL

    def get_score(self):
        return f"Score: {self.points}"