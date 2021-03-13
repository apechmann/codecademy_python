# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
#Activity 1/2: 
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Write a function that returns a new list of updated damages where:
# 1) the recorded data is converted to float values 
# 2) and the missing data is retained as "Damages not recorded".
# 3) Test your function with the data stored in damages.
 
#create an empty list for the function to return as output
damages_cleaned = []

def update_damages(list):
    fl_val = 0
    suffix = ""
    damages_cleaned.clear
    for damage in damages:
        if damage == 'Damages not recorded':
            damages_cleaned.append(damage)
            continue
        suffix = damage[-1]
        
        fl_val = float(damage[:-1])
        if suffix == "M":
            fl_val = fl_val * 1000000
        else:
            fl_val = fl_val * 1000000000   
        damages_cleaned.append(fl_val)   
#Run Function, fill with damages list, print cleaned list          
update_damages(damages)
#print(list(damages_cleaned))
#output is a List damages_cleaned

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 3: 
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Write a function that constructs a dictionary made out of the lists, 
# where the keys of the dictionary are the names of the hurricanes, 
# and the values are dictionaries themselves containing a key for each piece of data 
# 
# (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.
# 
# Thus the key "Cuba I" would have the value: 
# {'Name': 'Cuba I', 
# 'Month': 'October', 
# 'Year': 1924, 
# 'Max Sustained Wind': 165,
#  'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
# 'Damage': 'Damages not recorded', 
# 'Deaths': 90}.

d_hurricanes = {}

def build_dict_hurricanes():

    for i in range(len(names)):
        d_hurricanes[names[i]] = {
            "Name": names[i], 
            "Month": months[i], 
            "Year": years[i], 
            "Max Sustained Wind": max_sustained_winds[i], 
            "Areas Affected": areas_affected[i], 
            "Damage": damages_cleaned[i], 
            "Deaths": deaths[i]
            } 

build_dict_hurricanes()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 4:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

# In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.
# 
# Write a function that converts the current dictionary of hurricanes to a new dictionary, 
# where the keys are years 
# and the values are lists 
# containing a dictionary for each hurricane that occurred in that year.

# For example, the key 1932 would yield the value: 
# {
# 'Name': 'Bahamas', 
# 'Month': 'September',
# 'Year': 1932,
# 'Max Sustained Wind': 160,
# 'Areas Affected': ['The Bahamas', 'Northeastern United States'],
# 'Damage': 'Damages not recorded',
# 'Deaths': 16
# }
d_hurricanes_by_year = {}

def build_dict_hurricanes_by_year():
    len = len(d_hurricanes)
    print(len)
    #for i in range(len(d_hurricanes)):
       # year = d_hurricanes[Year]
        #d_hurricanes_by_year[year[i]] = {

       # }




#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 5: Test your function on your hurricane dictionary.
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 6: write your count affected areas function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 7: write your find most affected area function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 8: write your greatest number of deaths function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 9: write your catgeorize by mortality function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 10: write your greatest damage function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
# Activity 11: write your catgeorize by damage function here:
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
