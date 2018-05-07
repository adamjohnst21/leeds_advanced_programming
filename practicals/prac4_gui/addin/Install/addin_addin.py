import arcpy
import pythonaddins

class RiskButton(object):
    """Implementation for addin_addin.RiskButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("C:/Users/University/Dropbox/University/Advanced_programming/practicals/prac1_modelBuilder/models.tbx", "TraffordModelScript")