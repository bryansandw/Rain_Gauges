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
map_doc = work_space + '\Rain_Guage_Map.mxd'

hours_xy = work_space + '\Hour_xy.shp'
hour_shp = work_space + '\hour.shp'

mapdoc = arcpy.mapping.MapDocument(map_doc)
data_frame = arcpy.mapping.ListDataFrames(mapdoc)[0]
#print data_frame.name
#print data_frame.scale
legend = arcpy.mapping.ListLayoutElements(mapdoc, "LEGEND_ELEMENT", 
        "Legend")[0] 

hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
dates = []
one_day = datetime.timedelta(days = 1)

print "Do you wish to produce maps for all of the hours since Sep 24th, 2014?"
print "Please answer Yes or No."

answer1 = raw_input(">   ")

if answer1 == "Yes" or answer1 == "yes":
    print "This may take a while."
    last_date = datetime.datetime.now() 
    # could not get datetime.datetime(2014,09,24[,00[,00[,00[,00000[,None]]]]]) to work
    d = datetime.date(2014,9,23)
    t = datetime.time(00,0,0)
    first_date = datetime.datetime.combine(d, t)
	
elif answer1 == "No" or answer1 == "no":
    print """
Great!
You will be asked to input the first and last date in the range you are 
interested in, for example you might input 12-1-2015 for the first date 
and 12-7-2015 for the last date.
"""
    # need to make a function 
    print "Please input the first date in m-d-yyyy."
    answer2 = raw_input(">   ")
    print answer2
    #items = answer2.split('-')
    f_mounth, f_day, f_year = answer2.split('-')
    fd = datetime.date(int(f_year), int(f_mounth), int(f_day))
    ft = datetime.time(00,0,0)	
    first_date = datetime.datetime.combine(fd, ft)
    
    print "Is %s-%s-%s the date you wanted for the first date?" % (f_mounth, f_day, f_year)
    answer3 = raw_input(">   ")
    if answer3 == "No" or answer3 == "no":
        # need to make a function 
        print "Please input the first date in m-d-yyyy."
        answer2 = raw_input(">   ")
        #items = answer2.split('-')
        f_mounth, f_day, f_year = answer2.split('-')
        fd = datetime.date(f_year, f_mounth, f_day)
        ft = datetime.time(00,0,0)	
        first_date = datetime.datetime.combine(fd, ft)
    else:
        print "Great."

    print "Please input the last date in m-d-yyyy."
    answer4 = raw_input(">   ")
    print answer2
    #items = answer2.split('-')
    l_mounth, l_day, l_year = answer4.split('-')
    ld = datetime.date(int(l_year), int(l_mounth), int(l_day))
    lt = datetime.time(00,0,0)	
    last_date = datetime.datetime.combine(ld, lt)    

    print "Is %s-%s-%s the date you wanted for the last date?" % (l_mounth, l_day, l_year)
    answer3 = raw_input(">   ")
    if answer3 == "No" or answer3 == "no":
        # need to make a function 
        print "Please input the last date in m-d-yyyy."
        answer5 = raw_input(">   ")
        #items = answer2.split('-')
        l_mounth, l_day, l_year = answer5.split('-')
        ld = datetime.date(l_year, l_mounth, l_day)
        lt = datetime.time(00,0,0)	
        last_date = datetime.datetime.combine(ld, lt)
    else:
        print "Great."
		
		
i = first_date
while i <= last_date :
    dates.append(i)
    new_date = i + one_day
    #print new_date
    i = new_date
#print dates

#s_cur = arcpy.da.SearchCursor(hours_xy, 
#        ['Day', 'Hour', 'Rain_Total'])

#Export to PDF not working
for date in dates:
    for hour in hours:
        query = "\"Day\" = date'" + str(date) +"' AND \"Hour\" = " + str(hour)
        #print query
        #try:
        arcpy.Select_analysis( hours_xy, hour_shp, query)
            #for text in arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT"): 
            #    if text.text == "Date: Text":
            #        text.text = "Date: ", date
            #    else:
            #        pass
            #    if text.text == "Hour: Text":
            #        text.text = "Hour: ", hour
            #    else:
            #        pass
        arcpy.RefreshActiveView() 
        map_output = work_space + "\Rain_Maps\rain" + str(date) + "_" + str(hour) + ".pdf"
        arcpy.mapping.ExportToPDF(mapdoc, map_output)
        print "Created Map for ", date, hour
            #print "selected" , hour, date
        #except:
            #print "was unable to select", hour, date
            #break #pass
        
   


arcpy.RefreshTOC() 
