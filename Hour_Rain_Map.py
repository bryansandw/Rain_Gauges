#############################################################################
# Name: Elizabeth Rentschlar                                                #
# Assistantce from:                                                         #
# Purpose: Use Hourly rain totals condensed in Hours.py to create a series  #
#          of maps that show the                                            #
# Created: 12/21/15                                                         #
# Copyright: (c) City of Bryan                                              #
# ArcGIS Version: 10.2.2                                                    #
# Python Version: 2.7                                                       #
#############################################################################
#Import arcpy module
import arcpy
import datetime

# set workspace
arcpy.env.overwriteOutput = True
work_space = 'G:\GIS_PROJECTS\WATER_SERVICES\Rain_Gauges'
map_doc = '.\Rain_Gauge_Map.mxd'
map_output_folder = '.\Rain_Maps\'
hour_xy = '.\Hour_xy.py'

mapdoc = arcpy.mapping.MapDocument(map_doc)
data_frame = arcpy.mapping.ListDataFrames(mapdoc)[0]
print data_frame.name
print data_frame.scale
legend = arcpy.mapping.ListLayoutElements(mapdoc, "LEGEND_ELEMENT", 
        "Legend")[0] 

hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
dates = []
today_date = date.today()  		
# could not get datetime.datetime(2014,09,24[,00[,00[,00[,00000[,None]]]]]) to work
d = datetime.date(2014,9,24)
t = datetime.time(12,0,0)
first_date = datetime.datetime.combine(d, t)
#print first_date
one_day = datetime.timedelta(days = 1)
#i = today_date
#while i != first_date:
i = first_date
while i <= today_date :
    dates.append(i)
    new_date = i + one_day
    #print new_date
    i = new_date
#print dates

s_cur = arcpy.da.SearchCursor(hour_xy, 
        ['Day', 'Hour', 'Rain_Total'])

for text in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"): 
    if text.text == "Date: Text": 
        text.text = district + "\n" + date 
 
arcpy.RefreshActiveView() 
arcpy.RefreshTOC() 
