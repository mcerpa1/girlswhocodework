from random import *


#Create the list of words you want to choose from.
dad_list = ["Walter","Howard","Richard", "Tony","Burt","Edward", "Larry"]
mom_list = ["Patty","Linda","Mary","Kathy","Mary Anne","Shannon","Michele"]
oldpeople_list = [dad_list, mom_list]

#Generates a random integer.
x = randint(0, len(oldpeople_list)-1)
