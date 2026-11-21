from recommender.travel_recommender import TravelRecommender

def main():
    recommender = TravelRecommender("data/destinations.csv")
    print("Recommendations for budget='Low', vibe='Nature':")
    print(recommender.recommend(budget='Low', vibe='Nature'))

if __name__ == "__main__":
    main()
