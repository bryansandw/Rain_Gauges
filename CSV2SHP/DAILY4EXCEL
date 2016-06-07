#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from: S. Boada                                                #
# Purpose: Condense daily rain gauge readings in to one text file that      #
#          allows for the user to easily compare rain by day                #
# Created: 6/7/2016                                                         #
# Copyright: (c) City of Bryan                                              #
# Python Version: 2.7                                                       #
#############################################################################
# Import arcpy module
import datetime
import os

# set workspace
work_space = 'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'

# Local variables:  
dates = []
one_day = datetime.timedelta(days = 1)

# input tables
GolfCourse = './GolfCourse_Daily.txt' 
Plant1 = './Plant 1_Daily.txt'
Luza = './Luza 3_Daily.txt' #xy
LiftStation = './LiftStation158_Daily.txt' #xy
Burgess = './Burgess LS_Daily.txt'
LSPS = './LSPS Weather_Daily.txt'

table_list = [GolfCourse, Plant1, Luza, LiftStation, Burgess, LSPS]
#xPos = ['3545415', '3557931', '3546713', '3558420', '3538420']
#yPos = ['10218330', '10219830', '10227320', '10230450', '10203200']
print_list = ["GolfCourse", "Plant1", "Luza", "LiftStation", "Burgess", "LSPS"]

#date list
d_now = datetime.date.today()
d_first = datetime.date(2015,4,20)
#t = datetime.time(00,0,0)
#date_now = datetime.datetime.combine(d_now, t) 
#first_date = datetime.datetime.combine(d_first, t)

i = d_first
while i <= d_now:
    dates.append('"' + str(i) + ' 24:00:00"')
    new_date = i + one_day 
    i = new_date


with open('./Daily_Rainfall_Events.txt', 'w') as outFile:

    # Create Headers in Output Text File
    outFile.write('RAINFALL DATA\nRecorded from COB Rain Gauges\n' + str(d_first) + ' to ' + str(d_now) +'\nDate,GolfCourse(in),Plant1(in),Luza(in),LiftStation(in),Burgess(in),LSPS(in)\n')
    for date in dates:
		print 'Starting on', date	
		for f, station in zip(table_list, print_list):
			with open(f, "r") as f:
            # read the lines and skip 4 line header		
				lines = f.readlines()[4:] 
				for line in lines:
					item = line.split(',')
					if station == "GolfCourse":
						if item[0] == date:
							gc = item[3].rstrip('\n')
							break
						else:
							gc = "N/A"
					elif station == "Plant1":
						if item[0] == date:
							p1 = item[3].rstrip('\n')
							break
						else:
							p1 = "N/A"
					elif station == "Luza":
						if item[0] == date:
							lz = item[3].rstrip('\n')
							break
						else:
							lz = "N/A"
					elif station == "LiftStation":
						if item[0] == date:
							ls = item[3].rstrip('\n')
							break
						else:
							ls = "N/A"
					elif station == "Burgess":
						if item[0] == date:
							bg = item[3].rstrip('\n')
							break
						else:
							bg = "N/A"
					elif station == "LSPS":
						if item[0] == date:
							lsps = item[4].rstrip('\n')
							break
						else:
							lsps = "N/A"			
		outFile.write(str(date) + ',' + gc + ',' + p1 + ',' + lz + ',' + ls + ',' + bg + ',' + lsps + '\n')
