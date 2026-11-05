# part_b.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient

# Fetch data from CSV files
def fetch_data_from_csv():
    happiness_data = pd.read_csv("data/happiness.csv")
    covid_data = pd.read_csv("data/covid_data.csv")
    return happiness_data, covid_data


# Store data in MongoDB
def store_data_in_mongodb(happiness_data, covid_data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["lab1_database"]

    # Insert data into collections
    db["happiness"].insert_many(happiness_data.to_dict("records"))
    db["covid"].insert_many(covid_data.to_dict("records"))

    print("Data stored in MongoDB successfully!")


# Visualize data
def visualize_data(happiness_data, covid_data):
    # Line Chart: Happiness Rank vs Happiness Score
    plt.figure(figsize=(10, 5))
    plt.plot(happiness_data["Happiness Rank"], happiness_data["Happiness Score"], marker="o")
    plt.title("Happiness Rank vs Happiness Score")
    plt.xlabel("Happiness Rank")
    plt.ylabel("Happiness Score")
    plt.grid()
    plt.show()

    # Bar Chart: Total COVID Cases by Country
    plt.figure(figsize=(12, 6))
    plt.bar(covid_data["Country"], covid_data["Total Cases"])
    plt.title("Total COVID Cases by Country")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=90)
    plt.show()

    # Heatmap: Correlation for Happiness Dataset
    plt.figure(figsize=(8, 6))
    sns.heatmap(happiness_data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap for Happiness Dataset")
    plt.show()

    # Scatterplot: GDP per Capita vs Happiness Score
    plt.figure(figsize=(8, 6))
    plt.scatter(happiness_data["GDP per Capita"], happiness_data["Happiness Score"])
    plt.title("GDP per Capita vs Happiness Score")
    plt.xlabel("GDP per Capita")
    plt.ylabel("Happiness Score")
    plt.show()


# Main function to test Part B
if __name__ == "__main__":
    # Fetch data from CSV files
    happiness_data, covid_data = fetch_data_from_csv()

    # Store data in MongoDB
    store_data_in_mongodb(happiness_data, covid_data)

    # Visualize data
    visualize_data(happiness_data, covid_data)