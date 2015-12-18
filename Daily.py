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
# Import arcpy module
import arcpy

# set workspace
arcpy.env.overwriteOutput = True
work_space = 'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'

# FOR GIS  
# Create point 
# Local variables:  
out_shp = './Daily_xy.shp' 
prjfile = './NAD 1983 StatePlane Texas Central FIPS 4203 (US Feet).prj' 
spatialref =  arcpy.SpatialReference(prjfile) 

# input tables
GolfCourse = './GolfCourse_Daily.txt' 
Plant1 = './Plant 1_Daily.txt'
Luza = './Luza 3_Daily.txt' #xy
LiftStation = './LiftStation158_Daily.txt' #xy
Burgess = './Burgess LS_Daily.txt'
LSPS = './LSPS Weather_Daily.txt'

table_list = [GolfCourse, Plant1, Luza, LiftStation, Burgess]
xPos = ['3545415', '3557931', '3546713', '3558420', '3538420']
yPos = ['10218330', '10219830', '10227320', '10230450', '10203200']
print_list = ["GolfCourse", "Plant1", "Luza", "LiftStation", "Burgess"]
'''
with open('./Daily_xy.txt', 'w') as outFile:

    # Create Headers in Output Text File
    outFile.write('X,Y,Rain_Gauge,TIMESTAMP,RECORD,BattV_Min,Rain_in_Tot\n')

    for f, x, y, station in zip(table_list, xPos, yPos, print_list):
        print 'Starting on', station	
        with open(f, "r") as f:
            # read the lines and skip 4 line header		
            lines = f.readlines()[4:] 
            for line in lines:
                outFile.write( x + ',' + y + ',' + station + ',' + line)
    #LSPS has a different table format than the other input tables
    x = '3529213' 
    y = '10245470' 
    print 'Starting on LSPS'
    with open(LSPS, "r") as f:
        lines = f.readlines()[4:] 
        for line in lines:
            item = line.split(',')
            outFile.write( x + ',' + y + ',' + 'LSPS,' + item[0] + ',' +
                item[1] + ',' + item[2] + ',' + item[4] )
'''
#### Converting the rain data into a point shapefile #### 
# Create the feature class 
daily_shp = arcpy.management.CreateFeatureclass(work_space, out_shp, 'POINT', 
    '', '', '', spatialref) 

# add Station, Day, BattV_Min, and Rain Total fields 
arcpy.AddField_management(daily_shp,"Rain_Gauge", "TEXT", "", "", "", "", 
    "NULLABLE","NON_REQUIRED","") 
arcpy.AddField_management(daily_shp,"Day", "TEXT", "", "", "", "", 
    "NULLABLE","NON_REQUIRED","") 
arcpy.AddField_management(daily_shp,"BattV_Min", "TEXT", "", "", "", "", 
    "NULLABLE","NON_REQUIRED","") 
arcpy.AddField_management(daily_shp,"Rain_Total", "FLOAT", "", "", "", "", 
    "NULLABLE","NON_REQUIRED","") 
				
with open('./Daily_xy.txt', 'r') as inFile: 
    # variable  
    in_cur = arcpy.da.InsertCursor(daily_shp,  
        ['SHAPE@', 'Rain_Gauge','Day', 'BattV_Min', 'Rain_Total']) 
    pnt = arcpy.Point() 
    # skip header 
    next(inFile) 
			
    # Goes through the txt file that was just created and uses the data  
    # to create a point shapefile 
    for line in inFile: 
        rln = line.split(',') 
        pnt.X = int(rln[0]) 
        pnt.Y = int(rln[1]) 
        day = rln[3][1:11] 
        in_cur.insertRow((pnt, rln[2], day, rln[5], rln[6])) 
     
del in_cur 
print 'done' 
	
