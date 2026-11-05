# part_a.py
import math



#create a parent class for loading file
class Fileloader:
    def __init__(self, filename,num_rows):
        self.filename = filename
        self.num_rows = num_rows
        self.data=[]
        self.column_names=[]

    def load_file(self):
        with open(self.filename, "r") as file:
            lines = file.readlines()[:self.num_rows+1]
            self.column_names = lines[0].strip().split(",")
            for line in lines[1:]:
                values = line.strip().split(",")
                row = {}
                for i, header in enumerate(self.column_names):
                    # Try to convert numeric values to float
                    try:
                        row[header] = float(values[i])
                    except ValueError:
                        row[header] = values[i]
                self.data.append(row)
        return self.data

class ComputeStatistics(Fileloader):
    def __init__(self, filename,num_rows):
        super().__init__(filename,num_rows)


    def get_numeric_columns(self):
        """
        Identify numeric columns in the dataset.
        :return: A list of numeric column names.
        """
        numeric_columns = []
        if not self.data:
            return numeric_columns

        for column in self.column_names:
            # Check if the first row's value for the column is numeric
            if isinstance(self.data[0][column], (int, float)):
                numeric_columns.append(column)
        return numeric_columns

    def calculate_mean(self, column):
        """
        Calculate the mean of a numeric column.
        :param column: The column name.
        :return: The mean value.
        """
        values = [row[column] for row in self.data if isinstance(row[column], (int, float))]
        if not values:
            return None
        return sum(values) / len(values)

    def calculate_median(self, column):
        """
        Calculate the median of a numeric column.
        :param column: The column name.
        :return: The median value.
        """
        values = [row[column] for row in self.data if isinstance(row[column], (int, float))]
        if not values:
            return None
        values.sort()
        mid = len(values) // 2
        if len(values) % 2 == 0:
            return (values[mid - 1] + values[mid]) / 2
        return values[mid]

    def calculate_variance(self, column):
        """
        Calculate the variance of a numeric column.
        :param column: The column name.
        :return: The variance value.
        """
        mean = self.calculate_mean(column)
        if mean is None:
            return None
        values = [row[column] for row in self.data if isinstance(row[column], (int, float))]
        return sum((x - mean) ** 2 for x in values) / len(values)

    def calculate_std_dev(self, column):
        """
        Calculate the standard deviation of a numeric column.
        :param column: The column name.
        :return: The standard deviation value.
        """
        variance = self.calculate_variance(column)
        if variance is None:
            return None
        return math.sqrt(variance)

    def find_min(self, column):
        """
        Find the minimum value in a column.
        :param column: The column name.
        :return: The minimum value.
        """
        values = [row[column] for row in self.data if isinstance(row[column], (int, float))]
        if not values:
            return None
        return min(values)

    def find_max(self, column):
        """
        Find the maximum value in a column.
        :param column: The column name.
        :return: The maximum value.
        """
        values = [row[column] for row in self.data if isinstance(row[column], (int, float))]
        if not values:
            return None
        return max(values)

    def describe_numeric_columns(self):
        """
        Describe numeric columns (mean, median, variance, std dev, min, max).
        """
        numeric_columns = self.get_numeric_columns()
        for column in numeric_columns:
            print(f"\nColumn: {column}")
            print(f"Mean: {self.calculate_mean(column)}")
            print(f"Median: {self.calculate_median(column)}")
            print(f"Variance: {self.calculate_variance(column)}")
            print(f"Standard Deviation: {self.calculate_std_dev(column)}")
            print(f"Min: {self.find_min(column)}")
            print(f"Max: {self.find_max(column)}")




# Main function to test Part A
if __name__ == "__main__":
    # Load Happiness Dataset (10 rows)
    happiness_statistics=ComputeStatistics('World_Happiness_2019.csv',10)
    happiness_statistics.load_file()
    print("Describing numeric columns of Happiness:")
    happiness_statistics.describe_numeric_columns()

    # Load covid dataset
    covid_statistics=ComputeStatistics('WHO COVID-19 data.csv',10)
    covid_statistics.load_file()
    print("Describing numeric columns of COVID:")
    covid_statistics.describe_numeric_columns()

    #