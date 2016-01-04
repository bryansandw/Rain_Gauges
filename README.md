# Rain_Gauges
This is a series of python scripts.  

There are two sets of scripts for converting csv files collected from rain gauges into a point shape file in ArcGIS.  
  1. Hours.py handles the minute increment data and aggregates it into hour segments.  
  2. Daily.py handles the daily data. 
  
There is currently one script to create maps displaying the rain data, these are still a work in progress.
  1. Hour_Rain_Map.py cycles through the shapefile created by Hours.py in a pre existing ArcMap document to create a series of maps
     (I would like this to also produce an animated gif)
