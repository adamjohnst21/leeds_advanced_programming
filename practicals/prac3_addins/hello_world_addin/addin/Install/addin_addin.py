import arcpy
import pythonaddins

 

class ExplosionButtonClass(object):
    """Implementation for addin_addin.explosionbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        
		pythonaddins.MessageBox("Hello world", "Hello")