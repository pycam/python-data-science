import csv

# initialise variables
dataset = []

# read GapMinder dataset from file and filter the years of interest using CSV
with open('data/gapminder.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for record in reader:
        dataset.append(record)

# define function to filter the dataset based on year and extract one column
def filter_dataset(dataset, column_name, year):
    results = []
    for data in dataset:
        if data['year'] == year:
            results.append(data[column_name])
    return results


# scatter plots
import matplotlib.pyplot as mpyplot
mpyplot.xlabel('Life Expectancy')
mpyplot.ylabel('GDP per Capita')
mpyplot.title('GapMinder world data over 50 years')
mpyplot.scatter(filter_dataset(dataset, 'lifeExp', '1957'), filter_dataset(dataset, 'gdpPercap', '1957'), c='b', label='1957')
mpyplot.scatter(filter_dataset(dataset, 'lifeExp', '2007'), filter_dataset(dataset, 'gdpPercap', '2007'), c='g', label='2007')
mpyplot.legend()
mpyplot.grid(True)
mpyplot.show()
