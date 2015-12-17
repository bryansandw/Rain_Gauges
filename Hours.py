#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from: Steven B.                                               #
# Purpose: Condense Minute rain gauge readings in to hourly readings and    #
#         merge into one text file that can then be used in the GIS         #
# Created: 12/16/15                                                         #
# Copyright: (c) City of Bryan                                              #
# ArcGIS Version: 10.2.2                                                    #
# Python Version: 2.7                                                       #
#############################################################################
#Import arcpy module
import arcpy

# set workspace
arcpy.env.overwriteOutput = True
work_space = 'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'

# input tables
GolfCourse = './GolfCourse_Minute.txt' 
Plant1 = './Plant 1_Minute.txt'
Luza = './Luza 3_Minute.txt' 
LiftStation = './LiftStation158_Minute.txt'
Burgess = './Burgess LS_Minute.txt'
LSPS = './LSPS Weather_Hour.txt'

table_list = [GolfCourse, Plant1, Luza, LiftStation, Burgess]
x_and_y = ['3545415,10218330', '3557931,10219830', '3546713,10227320', '3558420,10230450', '3538420,10203200']
print_list = ["GolfCourse", "Plant1", "Luza", "LiftStation", "Burgess"]

# output table
out = './Hours_xy.txt'
out1 = open(out, 'w')

# Create Headers in Output Text File
out1.write("X"+',')
out1.write("Y"+',')
out1.write("TIMESTAMP"+',')
out1.write("Rain_in_Tot"+'\n')

# Create point
# Local variables:
Hour_xy_Layer = "Minute_xy_Layer"
shp = './Minute_xy.shp'
Hour_xy = './Minute_xy.shp'

# Variable for while loop
i = 0

while i < len(table_list):

    with open(table_list[i], "r") as f:
    	# read the lines and skip 4 line header
        lines = f.readlines()[4:] 

	# need a local variable
        last_date = ""
        minute = 0
        last_hour = 99
        rain = 0.00
    
        for line in lines:
            items  = line.split(',') 
            date, clock = items[0].split()
            hour = clock.split(":")[0]

            if hour == last_hour:
                rain_str = items[2]
                rain += float(rain_str)
                last_hour = hour
                minute +=  1
                if minute == 60:
                    minute = 0
                    rain_string = str(rain)
                    out1.write( x_and_y[i] + ',' + date + ' ' + hour + 
                        ':00:00"' + ',' + rain_string + '\n')

            else:
                minute = 1
                last_hour = clock.split(":")[0]
                rain_str = items[2]
                rain = float(rain_str)
        print print_list[i]
        i += 1

#LSPS
x = '3528380' 
y = '10245400' 
print 'Starting on LSPS' 

with open(LSPS, "r") as f:
    # read the lines and skip 4 line header
    lines = f.readlines()[4:] 
    for line in lines:
        #print line.split(',');
        item = line.split(',');
        #rain = item[4].split('\n');
        out1.write( x + ',' + y + ',' + item[0] + ',' + item[14] )
out1.close()
