#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from:                                                         #
# Purpose: Use Daily rain totals processed in Daily.py to create a series   #
#          of maps that show the total rain each day                        #
# Created: 1/13/2016                                                        #
# Copyright: (c) City of Bryan                                              #
# ArcGIS Version: 10.2.2                                                    #
# Python Version: 2.7                                                       #
#############################################################################
# This code is only efficient for one month, the more months that are
# included the less efficient the script becomes.  Need to come up with a 
# better method, but this works for now.
#Import arcpy module
import arcpy
import datetime
import os


# set workspace
arcpy.env.overwriteOutput = True
work_space = 'G:/GIS_PROJECTS/WATER_SERVICES/Rain_Gauges'
map_doc = work_space + '/Rain_Guage_Map.mxd'
daily_xy = work_space + '/Daily_xy.shp'
daily_shp = work_space + '/Daily.shp'

# Local Variables
months = []
dates = []
one_day = datetime.timedelta(days = 1)

# Functions
def assure_path_exists(my_path):
    dir = os.path.dirname(my_path)
    if not os.path.exists(dir):
        os.mkdir(dir)

def get_date(raw_user):
        month, year = raw_user.split('-')
        d = datetime.date(int(year), int(month), 1)
        t = datetime.time(00,0,0)
        date_ = datetime.datetime.combine(d, t)    
        return (date_)	

def add_one_month(dt0): 
    dt1 = dt0.replace(day = 1) 
    dt2 = dt1 + datetime.timedelta(days = 32) 
    dt3 = dt2.replace(day = 1) 
    return dt3 		
		
# Get the user to input the dates to produce the desired maps 
print "Please input the first month in m-yyyy."
try:
    first_date = get_date(raw_input(">   "))
    print first_date
except:
    print "You input a bad date, we will use the first data record..."
    d = datetime.date(2015,4,1)
    t = datetime.time(00,0,0)
    first_date = datetime.datetime.combine(d, t)

print "Please input the last month in m-yyyy."
try:
    my_date = get_date(raw_input(">   "))
    last_date = add_one_month(my_date) - one_day
    print last_date
except:
    print "Today will do..."
    last_date = datetime.datetime.now()     		

# while loop fills in the dates list		
i = first_date.date().month
j = first_date

while j <= last_date :
    myr = str(i) + '-' + str(j.date().year)
    months.append(myr)
    new_date = add_one_month(j)
    i = new_date.date().month
    j = add_one_month(j)
print months

# while loop fills in the dates list		
k = first_date
while k <= last_date :
    dates.append(k)
    new_date = k + one_day
    k = new_date


#use the dates list and months to create daily rain maps
for month in months:
    for date in dates:
        # could add to query to only select hours where it rained
        query = "\"Day\" = date'" + str(date) + \
            "' AND \"Month\" = '" + str(month) + "'"
        arcpy.Select_analysis( daily_xy, daily_shp, query)
        result = arcpy.GetCount_management(daily_shp)
        count = int(result.getOutput(0))		
        if count == 0:
            print "There were no records for %s." % (date)
        else:
            my_mapdoc = arcpy.mapping.MapDocument(map_doc)
            
            for text in arcpy.mapping.ListLayoutElements(my_mapdoc, 
                    "TEXT_ELEMENT"): 
                if text.text == "Text":
                    text.text = "Date: " + str(date.date())
                         
                else:
                    pass
            arcpy.RefreshActiveView() 
            arcpy.RefreshTOC()
            c_date = str(date.date())
            map_output = work_space + "/Rain_Maps/Month" + month + "/rain_" + c_date + ".gif"
            assure_path_exists(map_output)
        
            print map_output
            arcpy.mapping.ExportToGIF(my_mapdoc, map_output)
            del my_mapdoc
