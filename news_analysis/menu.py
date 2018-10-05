from store import store_news_data
from popular import determine_popular_article, populate_counts
from sentiment import display_results, populate_sentiment
import nltk
nltk.download('punkt')




def main():
    while True:

        print("Choose one of the following options:\n")
        print("1. Fetch News Data from Web")
        print("2. Determine most popular article")
        print("3. Determine most popular article (recompute score)")
        print("4. Perform Positive/Negative Valence Analysis")
        print("5. Perform Positive/Negative Valence Analysis (recompute sentiment)")
        print("6. Exit")

        choice = input("Select a number to indicate your choice (Example: 1):")
        try:
            choice = int(choice)
        except:
            choice = -1
        if choice == 1:
            print("This will take several minutes")
            store_news_data()
        elif choice == 2:
            determine_popular_article()
        elif choice == 3:
            print("This may take several minutes")
            populate_counts()
            determine_populat_article()
        elif choice == 4:
            display_results()
        elif choice == 5:
            populate_sentiment()
            display_results()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again by selecting a number.")

if __name__ == '__main__':
    main()
