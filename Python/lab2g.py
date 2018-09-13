"""
Name: Zackery Vering
Project: Lab 2G: Planets Exercise
Date: 5 Sept 2018
Recommended Version: Python 2.7
Instructions:
-Follow TODO's below
"""


planet_string = "Mercury|Venus|Earth|Mars|Jupiter|Saturn|Uranus|Neptune"
#TODO: Convert planets_string to a list, save it to planet_list.
#changed it so planet_list goes ahead and gets defined
planet_list = planet_string.split("|")

def log_planets():
    print "Here is a list of the planets:"
    for planet in planet_list:
        print planet
    print "----------------\n\n"

log_planets()

print 'Adding "The Sun" to the beginning of the planets list.'
#TODO: Perform action above
#Inserts sun into beginning
planet_list.insert(0, "Sun")
log_planets()

print 'Adding "Pluto" to the end of the planets list.'
#TODO: Perform action above
#Append pluto to end
planet_list.append("Pluto")
log_planets()

print 'Removing "The Sun" from the beginning of the planets list.'
#TODO: Perform action above
#Remove sun
planet_list.remove("Sun")
log_planets()

print 'Removing "Pluto" from the end of the planets list.'
#TODO: Perform action above
#Remove pluto
planet_list.remove("Pluto")
log_planets()

print 'Finding and logging the index of "Earth" in the planets list.'
#TODO: Perform action above
#Get earth's index
earth_index = planet_list.index('Earth')
log_planets()

print 'Removing the planet after "Earth".'
#TODO: Perform action above.  
#Remove planet after earth and capture it's value
removed_planet = planet_list.pop((earth_index+1))
log_planets()

print 'Adding back in the planet removed after "Earth".'
#TODO: Perform action above
#Add the last removed planet
planet_list.insert((earth_index+1), removed_planet)
log_planets()

print 'Reversing the order of the planets list.'
#TODO Perform action above
#Reverse the order
planet_list.reverse()
log_planets()

print 'Sorting the planets list'
#TODO Perform action above
#Sort the list
planet_list.sort()
log_planets()