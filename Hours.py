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
xPos = ['3545415', '3557931', '3546713', '3558420', '3538420']
yPos = ['10218330', '10219830', '10227320', '10230450', '10203200']
print_list = ["GolfCourse", "Plant1", "Luza", "LiftStation", "Burgess"]

with open(r'./Hours_xy.txt', 'w') as outFile:

    # Create Headers in Output Text File
    outFile.write("X,Y,TIMESTAMP,Rain_in_Tot\n")

    # Create point
    # Local variables: UNUSED!!!!!
    #Hour_xy_Layer = "Minute_xy_Layer"
    #shp = r'./Minute_xy.shp'
    #Hour_xy = r'./Minute_xy.shp'

    for f, x, y, station in zip(table_list, xPos, yPos, print_list):
        print 'Starting on', station
        with open(f, "r") as f:
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
                        #print "Date is: " + date
                        #print "Hour is: " + hour
                        #print "Rain is: " + str(rain)
                        minute = 0
                        rain_string = str(rain)
                        #print rain_string
                        outFile.write( x + ',' + y + ',' + date + ' ' + hour +
                            ':00:00"' + ',' + rain_string + '\n')

                else:
                    minute = 1
                    last_hour = clock.split(":")[0]
                    rain_str = items[2]
                    rain = float(rain_str)

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
