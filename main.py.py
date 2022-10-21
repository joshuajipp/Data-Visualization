# SHIVAM DESAI and JOSHUA JIPP

# ENDG 233 F21, BLOCK 2, Group 30

# A terminal-based application to process and plot data based on given user input and provided csv files.

 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Info:

    """A class used to create a Info object.

        Attributes:
            subregion (str): String that represents the name of the subregion name
            country (str): String that represents the country name
    """
 
    def __init__(self, subregion, country):
        self.subregion = subregion
        self.country = country
 
    def print_info_line(self):
        """A function that prints the subregion name and country name for the Info instance.
 
        Parameters: None
        Return: None
 
       """
        print('\n ***Displaying statistics for {0} and {1}*** \n'.format(self.subregion, self.country))
 
def find_region(region):
    """Creates a list of all the regions then checks if the users input region exists in that list
 
    Parameters:
    user_region -- string representing the region to check if it exists
 
    Returns:
    Returns True if the users region is in the list and exists
 
    """
    regions = []
    for i in array_country:

       regions.append(i[2])
    if region in regions:
        return True
 
def find_country(region, country):
    """Goes through array and makes a list of countries in the region and then checks if the users input country exists in that region
 
    Parameters:
    user_region -- string representing the region
    user_coutry -- string representing the country to check if it is in that region
 
    Returns:
    Returns True if the users country exists in that region
 
    """
    countries_in_region = []
    for i in array_country:
        if region == i[2]:
            countries_in_region.append(i[0])
    if country in countries_in_region:
        return True
 
data_country = pd.read_csv (r'Country_Data.csv')
data_population = pd.read_csv (r'Population_Data.csv')
data_threatened_species = pd.read_csv (r'Threatened_Species.csv')
 
array_country = data_country.to_numpy()
array_population = data_population.to_numpy()
array_threatened_species = data_threatened_species.to_numpy()
 
def main():
    user_input_region = input('Please enter a sub-region: ')   # Asks for user input for sub-region
    user_region_lower = user_input_region.lower()  # Changes user input to lowercase
    user_region = user_region_lower.title()        # Makes first letter of user input uppercase
    while find_region(user_region) != True:              # If region does not exist then the user is asked to enter again
        user_region = input('Please enter a correct sub-region: ')
   
    user_input_country = input('Please enter a country in that sub-region: ')
    user_country_lower = user_input_country.lower()        # Changes user input to lowercase
    user_country = user_country_lower.title()              # Makes first letter of user input uppercase
    while find_country(user_region, user_country) != True:     # Calls function to check if the country exists in the region or else input is asked for again
        print('Your country was invalid')
        user_country = input('Please enter a correct country in that sub-region: ')
 
    country_info = Info(user_region, user_country)   # Calls and stores value in class
    country_info.print_info_line()                       # Calls function from class
   
    # loop to find population density
    for i in array_population:
        if user_country == i[0]:
            array1 = array_country[:,0]                             # Creates an array of country names
            list1 = list(array1)                                    # Changes that array to a list
            index = list1.index(i[0])                               # Finds index value of that country
            pop_density_20 = i[6] / (array_country[index][3])      # Calculates population density
    print ('The population density in {0} in 2020 is {1:.6f} people per sq km'.format(user_country, pop_density_20))
    # loop to find change in population density
    for i in array_population:
        if user_country == i[0]:
            array1 = array_country[:,0]                             # Creates an array of country names
            list1 = list(array1)                                    # Changes that array to a list
            index = list1.index(i[0])                               # Finds index value of that country
            pop_density_15 = i[1] / (array_country[index][3])      # Calculates population density in 2015
            change_in_pop_density = pop_density_20 - pop_density_15    # Calculates difference in population density between 2020 and 2015
    print ('The change in population density in {0} from 2015 to 2020 is {1:.6f} people per sq km'.format(user_country, change_in_pop_density))
    # loop to find threatened animal species per sq km
    for i in array_country:
        if user_region == i[2]:
            array1 = array_country[:,0]
            list1 = list(array1)
            index = list1.index(i[0])
            country_threat_spieces = [array_threatened_species[index][1], array_threatened_species[index][2], array_threatened_species[index][3]]  # Creates list of threatned animal species
            total_threat_spieces_area = (np.sum(country_threat_spieces)) / array_country[index][3]         # Uses numpy method to get sum of list then divides my country area
    print(f'The threatened animal species per sq km in {user_country} is {total_threat_spieces_area:.6f} species per sq km.')
    # loop to calculate area of the whole sub-region
    total_area = 0
    for i in array_country:
        if user_region == i[2]:
            total_area += i[3]
    print ('The size of the {} sub-region is {} sq km'.format(user_region, total_area))
   

   # loop to calculate change in population of each country in the sub-region and dislpays it as a table
    print(f'\nThe change in population for each country in the {user_region} subregion from 2015 to 2020: \n')
    format_string = '{country:<25}{change:>5}'    # Guidelines for column widths in table
    print(format_string.format(country = 'Country', change = 'Population Change'))    # Prints titles of table columns
    pop_change_list = []                      # Creates a list of changes in population to later be used in graph
    for i in array_country:
        if user_region == i[2]:         # Only executes if the countries corresponding region matches user input
            array1 = array_country[:,0]       # Creates an array of country names
            list1 = list(array1)              # Changes that array to a list
            index = list1.index(i[0])         # Finds index value of that country
            population_change = array_population[index][6] - array_population[index][1]
            pop_change_list.append(population_change)      # Adds value of population change to list
            print(format_string.format(country = array_country[index][0], change = population_change))  # Adds country name and population change to table
 
    countries_in_region = []
    total_threat_spieces_list = []
    print(f'\nThe total number of threatened animal species in each country in the {user_region} sub-region:\n')
    format_string = '{country:<25}{total:>5}'      # Guidelines for column widths in table
    print(format_string.format(country = 'Country', total = ''))     # Prints titles of table columns
    for i in array_country:
        if user_region == i[2]:                    # Only executes if the countries corresponding region matches user input
            array1 = array_country[:,0]                  # Creates an array of country names
            list1 = list(array1)                         # Changes that array to a list
            index = list1.index(i[0])                    # Finds index value of that country
            countries_in_region.append(i[0])
            country_threat_spieces = [array_threatened_species[index][1], array_threatened_species[index][2], array_threatened_species[index][3]]   # Creates list of threatned animal species
            total_threat_spieces = np.sum(country_threat_spieces)         # Using numpy method to calculate sum of list above
            print(format_string.format(country = array_country[index][0], total = total_threat_spieces)) # Adds country name and total animal threatned species to table
            total_threat_spieces_list.append(total_threat_spieces)
   
    print(f'\nThe average number of threatened animal species in each country in the {user_region} sub-region:\n')
    format_string = '{country:<25}{average:<5}'     # Guidelines for column widths in table
    print(format_string.format(country = 'Country', average = ''))
    for i in array_country:
        if user_region == i[2]:                      # Only executes if the countries corresponding region matches user input
            array1 = array_country[:,0]                    # Creates an array of country names
            list1 = list(array1)                           # Changes that array to a list
            index = list1.index(i[0])                      # Finds index value of that country
            country_threat_spieces = [array_threatened_species[index][1], (array_threatened_species[index][2]), array_threatened_species[index][3]]   # Creates list of threatned animal species
            average_threat_spieces = (np.mean(country_threat_spieces))    # Using numpy method to calculate mean of list above
            print(format_string.format(country = array_country[index][0], average = average_threat_spieces))  # Adds country name and average animal threatned species to table
   
 
    # Displays a bar graph for the total threatned species for each country in that region
    fig = plt.figure(figsize =(10, 7))
    plt.bar(countries_in_region, total_threat_spieces_list, color ='blue', width = 0.4)
    plt.xlabel("Country")
    plt.ylabel("Number of species")
    plt.title("Total Number of Threatened Animal Species")
   
    # Displays a bar graph for the change in population for each country in that region
    fig = plt.figure(figsize =(10, 7))
    plt.bar(countries_in_region, pop_change_list, color ='red', width = 0.4)
    plt.xlabel("Country")
    plt.ylabel("Change in Population")
    plt.title(f"Change in Population for each country in the {user_region} sub-region")
   
    plt.show()
 
if __name__ == '__main__':
    main()
 
 