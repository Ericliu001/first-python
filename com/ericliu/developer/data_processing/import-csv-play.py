import csv

with open("/Users/ericliu/Developer/census_data/2011_WPP_ALL_for_NSW_long-header/2011 Census WPP All Geographies for NSW/LGA/NSW/2011Census_W01A_NSW_LGA_long.csv") as csvfile:
    workingPopulation = list(csv.DictReader(csvfile))

print(len(workingPopulation))

# get the the value of key 'Males_45_49_years_Employed_Worked_part_time' from the first row
workingPopulation[0]['Males_45_49_years_Employed_Worked_part_time']


# for col_name in workingPopulation[0].keys():
#     print(col_name)

# average persons Persons_25_29_years_Employed_Away_from_work
avg_num = sum(float(d['Persons_25_29_years_Employed_Away_from_work']) for d in workingPopulation)/len(workingPopulation)
print('The average number of Persons_25_29_years_Employed_Away_from_work in each suburb is: ' + str(avg_num));