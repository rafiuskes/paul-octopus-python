from predictor.AbstractPredictor import AbstractPredictor
import random

class Dinah(AbstractPredictor):
    def predict_match(self, home, away):
        return {'home': home, 'home_score': random.randint(0,4), 'away_score': random.randint(0,4), 'away': away}