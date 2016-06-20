#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from: S. Boada                                                #
# Purpose: add new data to the existing Minute_Rainfall_Events.txt doc      #
# Created: 6/16/2016                                                        #
# Copyright: (c) City of Bryan                                              #
# Python Version: 2.7                                                       #
#############################################################################
# at some point I need to set it up to pull 
# Import module
import datetime
import numpy as np

# set workspace
work_space = 'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'

#existing doc 
doc = './Minute_Rainfall_Events.txt'

# input tables
GolfCourse = './GolfCourse_Minute.txt'
Plant1 = './Plant 1_Minute.txt'
Luza = './Luza 3_Minute.txt'
LiftStation = './LiftStation158_Minute.txt'
Burgess = './Burgess LS_Minute.txt'
LSPS = './LSPS Weather_Hour.txt'

table_list = [GolfCourse, Plant1, Luza, LiftStation, Burgess, LSPS]
print_list = ["GolfCourse", "Plant1", "Luza", "LiftStation", "Burgess", "LSPS"]

# Local variables:  
dates = []
one_day = datetime.timedelta(days = 1)

# date list
d_now = datetime.date.today()
d_first = datetime.date(2015,4,20)
hours = [ "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"] 
minutes = [ "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59" ] 

# create a date list to find values to append to file
i = d_first
while i <= d_now:
    for hour in hours:
        for minute in minutes:
            if hour == "24" and minute == "01":
                break
            elif hour == "00" and minute == "00":
                pass
            else:
                dates.append('"' + str(i) + " " + hour +':'+ minute +':00"')
    new_date = i + one_day 
    i = new_date

# need to read doc and find last date listed and set that as d_fisrt
with open(doc, 'r') as outFile:
    my_first = (list(outFile)[-1]).split(',')[0]
    print my_first    

new_dates = dates[dates.index(my_first)+ 1:]
print new_dates[0]
print new_dates[200]
    
# Create an array to store the values in the text files in
my_array = np.zeros((len(new_dates),), dtype=[('Date', 'a', 21),
    ('GolfCourse', '<f'),
    ('Plant1', '<f'),
    ('Luza', '<f'),
    ('LiftStation', '<f'),
    ('Burgess', '<f'),
    ('LSPS', '<f'),
])

#Go through and assign the dates and times to the first column of the array
my_array.fill(-9999.9)
my_array['Date'] = new_dates

print my_array[2]	
print my_array[200]

#open the txt files and find the line where the date exists

for f, station in zip(table_list, print_list):
    with open(f, "r") as f:
    # read the lines and skip 4 line header		
        lines = f.readlines()[4:] 
        for line in lines:
            item = line.split(',')
            try:
                if station == 'LSPS':
                    my_array[new_dates.index(item[0])][station] = item[14].rstrip('\n')
                else:
                    my_array[new_dates.index(item[0])][station] = item[2].rstrip('\n')
            except:
                pass

print my_array[2]	
print my_array[200]	

with open(doc, 'a') as outFile:
    for date in new_dates:
        day_time = my_array[dates.index(date)][0].strip("'")
        golf = str(my_array[dates.index(date)][1])
        plant = str(my_array[dates.index(date)][2])
        luz = str(my_array[dates.index(date)][3])
        lif_sta = str(my_array[dates.index(date)][4])
        bur = str(my_array[dates.index(date)][5])
        low_pump = str(my_array[dates.index(date)][6]) 
        outFile.write(day_time + ', '+ golf + ', ' + plant + ', ' + luz + ', ' + lif_sta + ', ' + bur + ', ' + low_pump + '\n')
