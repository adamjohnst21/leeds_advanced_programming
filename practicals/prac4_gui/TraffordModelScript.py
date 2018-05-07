import arcpy

arcpy.env.workspace = "C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac4_gui"

if arcpy.Exists("crime.shp"):
    arcpy.Delete_management ("crime.shp")

Burglaries = arcpy.GetParameterAsText(0)
Distance = arcpy.GetParameterAsText(1)
Buildings = arcpy.GetParameterAsText(2)
Out = "crime.shp"

arcpy.ImportToolbox("C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac1_modelBuilder/models.tbx", "models")
arcpy.TraffordModel_models(Burglaries, Distance, Buildings, Out)

if arcpy.Exists("crime_sorted.shp"):
    arcpy.Delete_management ("crime_sorted.shp")
arcpy.Sort_management(Out, "crime_sorted", [["Join_Count", "DESCENDING"]])


#Get the current map document.
mxd = arcpy.mapping.MapDocument("CURRENT")

#Get that bit of it currently showing (there might be multiple "maps" in this document in layout view)
df = mxd.activeDataFrame 

#Make a new layer from the data.
newlayer = arcpy.mapping.Layer("crime_sorted.shp")

#Make a new layer from the example layer file.
layerFile = arcpy.mapping.Layer("albertsquare/buildings.lyr")

#Update the data layer with the symbolism from the example.
arcpy.mapping.UpdateLayer(df, newlayer, layerFile, True)

#Say that we want it coloured by the values in the "Joint_Count" column.
newlayer.symbology.valueField = "Join_Count"

#Add all the unique Joint_Count values to the symbolism (otherwise it just displays one colour)
newlayer.symbology.addAllValues() 

#Add the data layer to the map at the TOP.
arcpy.mapping.AddLayer(df, newlayer,"TOP")