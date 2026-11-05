# Data Analysis with Python and MongoDB

Analysing the **World Happiness Report 2019** and **WHO COVID-19** datasets: descriptive statistics written from scratch with object-oriented Python, data storage in **MongoDB**, and visualisation.

## 🎯 What this project does

### Part A: Statistics from scratch (`part_a.py`)
- A `Fileloader` class that reads CSV files with plain Python file I/O (no pandas)
- A `ComputeStatistics` class that **inherits** from `Fileloader` and calculates mean, median, variance, standard deviation, min and max for every numeric column

### Part B: MongoDB and visualisation
- `part_b.py`: loads the CSVs with pandas, stores them in a **local MongoDB** database and draws line, bar, heatmap and scatter charts
- `part_b_mongodb_atlas.py`: connects to a **MongoDB Atlas** cloud cluster, with credentials read from environment variables

## 🛠️ Tech Stack
Python · pandas · MongoDB (pymongo) · Matplotlib · Seaborn

## 🚀 How to Run
```bash
pip install -r requirements.txt
python part_a.py
python part_b.py        # needs MongoDB running on localhost:27017
```
For the Atlas version, set `MONGO_USER`, `MONGO_PASSWORD` and `MONGO_CLUSTER` as environment variables first.

## 📂 Data
The CSV files are not included. Place `World_Happiness_2019.csv` and `WHO COVID-19 data.csv` next to the scripts.

## 👤 Author
Masooma, MSc Applied AI, Year 1
