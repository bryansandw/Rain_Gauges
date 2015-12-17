#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from: S. Boada                                                #
# Purpose: Condense minute rain gauge readings in to hourly readings and    #
#          merge into one text file that can then be used in the GIS        #
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

# FOR GIS 
# Create point
# Local variables: 
#Hour_xy_Layer = "Minute_xy_Layer"
out_shp = './Hour_xy.shp'

prjfile = './NAD 1983 StatePlane Texas Central FIPS 4203 (US Feet).prj'
spatialref =  arcpy.SpatialReference(prjfile)


#Hour_xy = r'./Minute_xy.shp'
'''
#### Formating the rain data for use in the GIS ####
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
                        minute = 0
                        rain_string = str(rain)
                        outFile.write( x + ',' + y + ',' + date + ' ' + hour +
                            ':00:00"' + ',' + rain_string + '\n')

                else:
                    minute = 1
                    last_hour = clock.split(":")[0]
                    rain_str = items[2]
                    rain = float(rain_str)

    #LSPS is in an hour format already
    x = '3529217'
    y = '10245474'
    print 'Starting on LSPS'

    with open(LSPS, "r") as f:
        # read the lines and skip 4 line header
        lines = f.readlines()[4:]
        for line in lines:
            item = line.split(',');
            outFile.write( x + ',' + y + ',' + item[0] + ',' + item[14] )
'''
#### Converting the rain data into a point shapefile ####

hour_shp = arcpy.management.CreateFeatureclass(work_space, out_shp, 'POINT', '', '', '', spatialref)

arcpy.AddField_management(hour_shp,"Day", "TEXT", "", "", "", "",
    "NULLABLE","NON_REQUIRED","")
arcpy.AddField_management(hour_shp,"Hour", "TEXT", "", "", "", "",
    "NULLABLE","NON_REQUIRED","")
arcpy.AddField_management(hour_shp,"Rain_Total", "FLOAT", "", "", "", "",
    "NULLABLE","NON_REQUIRED","")

with open(r'./Hours_xy.txt', 'r') as inFile:
    # variable 
	
    in_cur = arcpy.da.InsertCursor(hour_shp, ['SHAPE@', 'Day', 'Hour', 'Rain_Total'])

    pnt = arcpy.Point()
    #ary = arcpy.Array()
	# skip header
    next(inFile)
	
	# Goes through the txt file that was just created and uses the data 
    # to create a point shapefile
    for line in inFile:
        rln = line.split(',')
        pnt.X = int(rln[0])
        pnt.Y = int(rln[1])
        day = rln[2][1:11]
        hour = rln[2][12:14]
        in_cur.insertRow((pnt, day, hour,rln[3]))
    
del in_cur
print 'done'
