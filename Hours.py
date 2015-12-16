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
work_space = r'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'

# input tables
GolfCourse = r'./GolfCourse_Minute.txt' 
Plant1 = r'./Plant 1_Minute.txt'
Luza = r'./Luza 3_Minute.txt' 
LiftStation = r'./LiftStation158_Minute.txt'
Burgess = r'./Burgess LS_Minute.txt'
LSPS = r'./LSPS Weather_Hour.txt'

# output table
out = r'./Hours_xy.txt'
out1 = open(out, 'w')

# Create Headers in Output Text File
out1.write("X"+',')
out1.write("Y"+',')
out1.write("TIMESTAMP"+',')
out1.write("Rain_in_Tot"+'\n')

# Create point
# Local variables:
Hour_xy_Layer = "Minute_xy_Layer"
shp = r'./Minute_xy.shp'
Hour_xy = r'./Minute_xy.shp'

#### I should try and get rid of these at some point
Hour_xy__2_ = r'./Minute_xy.shp'
Hour_xy__4_ = r'./Minute_xy.shp'
Hour_xy__3_ = r'./Minute_xy.shp'
Hour_xy_Layer_shp = r'./Minute_xy_Layer.shp'

#GolfCourse
x = '3545415' 
y = '10218330'  
print 'Starting on Golf Course'

with open(GolfCourse, "r") as f:
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
                out1.write( x + ',' + y + ',' + date + ' ' + hour + 
                    ':00:00"' + ',' + rain_string + '\n')

        else:
            minute = 1
            last_hour = clock.split(":")[0]
            rain_str = items[2]
            rain = float(rain_str)
f.close()

#Plant1
x = '3557931'
y = '10219830'
print 'Starting on Plant 1'

with open(Plant1, "r") as f:
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
                out1.write( x + ',' + y + ',' + date + ' ' + hour + 
                    ':00:00"' + ',' + rain_string + '\n')

        else:
            minute = 1
            last_hour = clock.split(":")[0]
            rain_str = items[2]
            rain = float(rain_str)
f.close()

#Luza
x = '3546713' 
y = '10227320' 
print 'Starting on Luza'

with open(Luza, "r") as f:
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
                out1.write( x + ',' + y + ',' + date + ' ' + hour + 
                    ':00:00"' + ',' + rain_string + '\n')

        else:
            minute = 1
            last_hour = clock.split(":")[0]
            rain_str = items[2]
            rain = float(rain_str)
f.close()

#LiftStation 158
x = '3558420' 
y = '10230450' 
print 'Starting on Lift Station'

with open(LiftStation, "r") as f:
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
                out1.write( x + ',' + y + ',' + date + ' ' + hour + 
                    ':00:00"' + ',' + rain_string + '\n')

        else:
            minute = 1
            last_hour = clock.split(":")[0]
            rain_str = items[2]
            rain = float(rain_str)
f.close()

#Burgess
x = '3538420' 
y = '10203200' 
print 'Starting on Burgess'

with open(Burgess, "r") as f:
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
                out1.write( x + ',' + y + ',' + date + ' ' + hour + 
                    ':00:00"' + ',' + rain_string + '\n')

        else:
            minute = 1
            last_hour = clock.split(":")[0]
            rain_str = items[2]
            rain = float(rain_str)
f.close()

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
#		rain = item[4].split('\n');
        out1.write( x + ',' + y + ',' + item[0] + ',' + item[14] )
f.close()

out1.close()
