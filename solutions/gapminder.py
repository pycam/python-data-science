import statistics as stats
import csv

def gdp_stats_by_continent_and_year(gapminder_filepath, continent='Europe', year='1952'):
    """
    Returns a dictionary of the average, median and standard deviation of GDP per capita 
    for all countries of the selected continent for a given year.

    gapminder_filepath --- gapminder file path with multi-continent and multi-year data
    continent --- continent for which data is extracted
    year --- year for which data is extracted
    """
    gdppercap = []
    with open(gapminder_filepath) as f:
        reader = csv.DictReader(f, delimiter = ",")
        for data in reader: 
            if data['continent'] == continent and data['year'] == year:
                gdppercap.append(float(data['gdpPercap']))
    print(continent, 'GDP per Capita in', year)
    return {'mean': stats.mean(gdppercap), 'median': stats.median(gdppercap), 'stdev': stats.stdev(gdppercap)}


def largest_country_by_continent_and_year(gapminder_filepath, continent='Europe', year='1952'):
    """
    Returns the largest country of the selected continent for a given year.

    gapminder_filepath --- gapminder file path with multi-continent and multi-year data
    continent --- continent for which data is extracted
    year --- year for which data is extracted
    """
    pop = 0
    largest_country = ''
    with open(gapminder_filepath) as f:
        reader = csv.DictReader(f, delimiter = ",")
        for data in reader: 
            if data['continent'] == continent and data['year'] == year:
                if int(data['pop']) > pop:
                    pop = int(data['pop'])
                    largest_country = data['country']
    print(continent, 'largest country in', year)
    return largest_country, pop


def avg_life_exp_by_continent_and_year(gapminder_filepath, continent='Europe', year='1952'):
    """
    Returns the average life expectancy 
    for all countries of the selected continent for a given year.

    gapminder_filepath --- gapminder file path with multi-continent and multi-year data
    continent --- continent for which data is extracted
    year --- year for which data is extracted
    """
    life_exp = []
    with open(gapminder_filepath) as f:
        reader = csv.DictReader(f, delimiter = ",")
        for data in reader: 
            if data['continent'] == continent and data['year'] == year:
                life_exp.append(float(data['lifeExp']))
    print(continent, 'life expectancy', year)
    return stats.mean(life_exp)
