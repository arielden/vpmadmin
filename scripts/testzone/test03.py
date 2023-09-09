# import python modules
import os
from win32com.client import Dispatch

"""
Crea una catpart, hace un sketch básico y le realiza un pad.
Al sólido resultante, le asigna un material.
"""

# Connecting to windows COM 
CATIA = Dispatch('CATIA.Application')
# optional CATIA visibility
CATIA.Visible = True

# Create an empty part
partDocument1 = CATIA.Documents.Add("Part")

# Create the point that the plane and sketch reference
Xcoord=100
Ycoord=100
Zcoord=100
NewPoint = CATIA.ActiveDocument.Part.HybridShapeFactory.AddNewPointCoord(Xcoord, Ycoord, Zcoord)
Mainbody = CATIA.ActiveDocument.Part.MainBody
Mainbody.InsertHybridShape(NewPoint)

# Create reference plane for sketch
AxisXY = CATIA.ActiveDocument.Part.OriginElements.PlaneXY
Referenceplane = CATIA.ActiveDocument.Part.CreateReferenceFromObject(AxisXY)
Referencepoint = CATIA.ActiveDocument.Part.CreateReferenceFromObject(NewPoint)
NewPlane = CATIA.ActiveDocument.Part.HybridShapeFactory.AddNewPlaneOffsetPt(Referenceplane, Referencepoint)
Mainbody.InsertHybridShape(NewPlane)

# create sketch
sketches1 = CATIA.ActiveDocument.Part.Bodies.Item("PartBody").Sketches
reference1 = partDocument1.part.OriginElements.PlaneXY
NewSketch = sketches1.Add(reference1)
CATIA.ActiveDocument.Part.InWorkObject = NewSketch

#Drawing the sketch
NewSketch.OpenEdition()
#                                  Start (H,   V)  End(H,V)
NewLine1 = NewSketch.Factory2D.CreateLine(0  , 0  , 0   ,50)
NewLine2 = NewSketch.Factory2D.CreateLine(0  , 50 , 50  ,50)
NewLine3 = NewSketch.Factory2D.CreateLine(50 , 50 , 50  ,55)
NewLine4 = NewSketch.Factory2D.CreateLine(50 , 55 , 150 ,55)
NewLine5 = NewSketch.Factory2D.CreateLine(150, 55 , 150  ,-5)
NewLine6 = NewSketch.Factory2D.CreateLine(50, -5 , 50  ,0)
NewLine7 = NewSketch.Factory2D.CreateLine(50 , -5 , 75  ,-5)
NewLine8 = NewSketch.Factory2D.CreateLine(150 , -5 , 125  ,-5)
NewLine9 = NewSketch.Factory2D.CreateLine(125 , -5 , 125  ,25)
NewLine0 = NewSketch.Factory2D.CreateLine(125 , 25 , 75  ,25)
NewLine11 = NewSketch.Factory2D.CreateLine(75 , 25 , 75  ,-5)
NewLine12 = NewSketch.Factory2D.CreateLine(50 , 0  , 0   ,0)
NewSketch.CloseEdition()

# Create a pad from sketch
LengthBlock=50
NewBlock = CATIA.ActiveDocument.Part.ShapeFactory.AddNewPad (NewSketch, LengthBlock)
CATIA.ActiveDocument.Part.Update()

# Assign Material
MatManager=CATIA.ActiveDocument.Part.GetItem("CATMatManagerVBExt")
hk=CATIA.ActiveDocument.Part.MainBody
systempath= CATIA.SystemService.Environ("CATDocView")
path= "C:\\Program Files\\Dassault Systemes\\B28\win_b64\\startup\\materials\\Catalog.CATMaterial"
MatDoc=CATIA.Documents.Open(path)
oMaterial=MatDoc.Families.Item("Metal").Materials.Item("Steel")
MatManager.ApplyMaterialOnBody (hk,oMaterial,1)
MatDoc.Close()