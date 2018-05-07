import arcpy
import pythonaddins

 #add the below in somewhere
 #object = pythonaddins.GPToolDialog(toolboxpath, tool_name) 

class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
	
        object = pythonaddins.GPToolDialog("C:\Users\University\Dropbox\University\Advanced_programming\practicals\prac1_modelBuilder\models.tbx", "explosionscript2") 
		
		Input_Features = arcpy.GetParameterAsText(0)

		Distance__value_or_field_ = arcpy.GetParameterAsText(1)

		Layer = arcpy.GetParameterAsText(2)

		Intersect__3_ = arcpy.GetParameterAsText(3)
		if Intersect__3_ == '#' or not Intersect__3_:
			Intersect__3_ = "C:\\Users\\University\\Dropbox\\University\\Advanced_programming\\practicals\\advPrg.gdb\\Intersect" # provide a default value if unspecified

		Output_Feature_Class = arcpy.GetParameterAsText(4)

		try:
			try:
				arcpy.ImportToolbox("C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac1_modelBuilder/models.tbx", "models")
			except arcpy.ExecuteError as e:
				print("Import toolbox error", e)
			try:
				arcpy.Explosion_models(Input_Features, Distance__value_or_field_, Layer, Intersect__3_, Output_Feature_Class) # don't forget to remove the " " when changing to parameter based inputs
			except arcpy.ExecuteError as e:
				print("Model run error", e)
		except Exception as e:
			print(e)