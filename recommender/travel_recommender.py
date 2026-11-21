import pandas as pd

class TravelRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, budget=None, vibe=None):
        result = self.data
        if budget:
            result = result[result['budget'].str.strip().str.lower() == budget.lower()]
        if vibe:
            result = result[result['vibe'].str.strip().str.lower() == vibe.lower()]
        return result['destination'].tolist()
