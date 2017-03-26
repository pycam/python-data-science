# initialise variables
life_expectancy_data_old = []
gdp_per_capita_data_old = []

life_expectancy_data_new = []
gdp_per_capita_data_new = []

# read GapMinder dataset from file and filter the years of interest
with open('data/gapminder.txt') as f:
    for line in f:
        country, continent, year, life_expectancy, pop, gdp_per_capita = line.strip().split('\t')
        if country == 'country':
            continue
        if year == '1957':
            life_expectancy_data_old.append(float(life_expectancy))
            gdp_per_capita_data_old.append(float(gdp_per_capita))
        elif year == '2007':
            life_expectancy_data_new.append(float(life_expectancy))
            gdp_per_capita_data_new.append(float(gdp_per_capita))


# scatter plots
import matplotlib.pyplot as mpyplot
mpyplot.xlabel('Life Expectancy')
mpyplot.ylabel('GDP per Capita')
mpyplot.title('GapMinder world data over 50 years')
mpyplot.scatter(life_expectancy_data_old, gdp_per_capita_data_1957, c='b', label='1957')
mpyplot.scatter(life_expectancy_data_new, gdp_per_capita_data_2002, c='g', label='2007')
mpyplot.legend()
mpyplot.grid(True)
mpyplot.show()
