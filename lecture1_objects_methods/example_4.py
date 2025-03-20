# Author:       Nerea Salamero Labara
# Date:         15/01/2025
# File:         example_4.py
# Description:  Objects and methods. 

def average_city(city_1, city_2, city_3):
    def calculate_population_density(city):
        population = city.get('population', 0)
        area = city.get('area', 1)
        if area > 0:
            return population / area
        else:
            return 1

    density_city_1 = calculate_population_density(city_1)
    density_city_2 = calculate_population_density(city_2)
    density_city_3 = calculate_population_density(city_3)

    highest_density = max(density_city_1, density_city_2, density_city_3)
    
    if highest_density == density_city_1:
        return city_1.get('name', 'city 1')
    elif highest_density == density_city_2:
        return city_2.get('name', 'city 2')
    else:
        return city_3.get('name', 'city 3')
    
city_1 = {'name': 'Metropolis', 'population': 1000000, 'area': 250}
city_2 = {'name': 'Megacity', 'population': 15000000, 'area': 1000}
city_3 = {'name': 'Smalltown', 'population': 5000, 'area': 0}

result = average_city(city_1, city_2, city_3)
print("The city with the highest population density is: ", result)