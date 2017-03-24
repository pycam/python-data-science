# initialise variables
data = []
data_years = []

# read GapMinder dataset from file
with open('data/gapminder.txt') as f:
    for line in f:
        country, continent, year, life_expectancy, pop, gdp_per_capita = line.strip().split('\t')
        if country == 'country':
            continue
        data.append({'country': country,
                     'continent': continent,
                     'year': int(year),
                     'life_expectancy': float(life_expectancy),
                     'population': int(pop),
                     'gdp_per_capita': float(gdp_per_capita)})
        data_years.append(int(year))

# find what are the oldest and youngest years in the dataset
non_redundant_years = list(set(data_years))
non_redundant_years.sort()
oldest_year = non_redundant_years[0]
youngest_year = non_redundant_years[-1]
print(oldest_year, youngest_year)

# initialise more variables
oldest_life_expectancy = []
youngest_life_expectancy = []
oldest_population = []
youngest_population = []

# calculate average life expectancy as well as global population increase between these two years
for d in data:
    if d['year'] == oldest_year:
        oldest_life_expectancy.append(d['life_expectancy'])
        oldest_population.append(d['population'])
    elif d['year'] == youngest_year:
        youngest_life_expectancy.append(d['life_expectancy'])
        youngest_population.append(d['population'])

print(oldest_year, sum(oldest_life_expectancy)/len(oldest_life_expectancy))
print(youngest_year, sum(youngest_life_expectancy)/len(youngest_life_expectancy))
life_expectancy_increased = sum(youngest_life_expectancy)/len(youngest_life_expectancy) - sum(oldest_life_expectancy)/len(oldest_life_expectancy)
population_increased = sum(youngest_population) - sum(oldest_population)
print('In', youngest_year - oldest_year, 'years, life expectancy increased by', life_expectancy_increased, 'years')
print('In', youngest_year - oldest_year, 'years, global population increased by', population_increased, 'people')

# find which country as the lowest life expectancy in 2002
lowest_life_expectancy_in_2002 = 100
country_with_lowest_life_expectancy_in_2002 = ''
for d in data:
    if d['year'] == 2002:
        if d['life_expectancy'] < lowest_life_expectancy_in_2002:
            lowest_life_expectancy_in_2002 = d['life_expectancy']
            country_with_lowest_life_expectancy_in_2002 = d['country']
print(country_with_lowest_life_expectancy_in_2002, lowest_life_expectancy_in_2002)
