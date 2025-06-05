
import FreeCAD, Part

doc = FreeCAD.newDocument('House')
foundation = Part.makeBox(10000.0, 4000.0, 300.0)
foundation_obj = doc.addObject("Part::Feature", "Foundation")
foundation_obj.Shape = foundation

outer_wall = Part.makeBox(10000.0, 4000.0, 4000.0)
inner_wall = Part.makeBox(
    10000.0-2*300.0, 
    4000.0-2*300.0, 
    4000.0-300.0
)
inner_wall.translate(FreeCAD.Vector(300.0, 300.0, 300.0))
walls = outer_wall.cut(inner_wall)
walls_obj = doc.addObject("Part::Feature", "Walls")
walls_obj.Shape = walls

points = [FreeCAD.Vector(0,0,0), FreeCAD.Vector(10000.0,0,4000.0/2), FreeCAD.Vector(10000.0,0,0)]
roof = Part.Face(Part.makePolygon(points)).extrude(FreeCAD.Vector(0,4000.0,0))

roof_obj = doc.addObject("Part::Feature", "Roof")
roof_obj.Shape = roof
roof_obj.Placement.Base = FreeCAD.Vector(0,0,4000.0)

doc.recompute()
doc.saveAs(r"C:\Users\Professional\Desktop\diplomTalibova\3d_model\house_31.FCStd")
