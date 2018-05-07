import arcpy

arcpy.env.workspace = "C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac1_modelBuilder/data"
try:
    try:
        arcpy.ImportToolbox("C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac1_modelBuilder/models.tbx", "models")
    except arcpy.ExecuteError as e:
        print("Import toolbox error", e)
    try:
        arcpy.Explosion_models("explosion0/point", "25 Meters",  "build0/polygon", "intersect.shp", "buffer.shp") # Your parameters, here.
    except arcpy.ExecuteError as e:
        print("Model run error", e)
except Exception as e:
    print(e)
	
	
	
#syntax:	Explosion_models (Input_Features, Distance__value_or_field_, Layer, Intersect__3_, Output_Feature_Class) 
