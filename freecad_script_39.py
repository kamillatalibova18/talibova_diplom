
import FreeCAD, Part

doc = FreeCAD.newDocument('House')
foundation = Part.makeBox(6000.0, 6000.0, 500.0)
foundation_obj = doc.addObject("Part::Feature", "Foundation")
foundation_obj.Shape = foundation

outer_wall = Part.makeBox(6000.0, 6000.0, 2700.0)
inner_wall = Part.makeBox(
    6000.0-2*150.0, 
    6000.0-2*150.0, 
    2700.0-500.0
)
inner_wall.translate(FreeCAD.Vector(150.0, 150.0, 500.0))
walls = outer_wall.cut(inner_wall)
walls_obj = doc.addObject("Part::Feature", "Walls")
walls_obj.Shape = walls

points = [FreeCAD.Vector(0,0,0), FreeCAD.Vector(6000.0/2,0,2700.0/2), FreeCAD.Vector(6000.0,0,0)]
roof = Part.Face(Part.makePolygon(points)).extrude(FreeCAD.Vector(0,6000.0,0))

roof_obj = doc.addObject("Part::Feature", "Roof")
roof_obj.Shape = roof
roof_obj.Placement.Base = FreeCAD.Vector(0,0,2700.0)

doc.recompute()
doc.saveAs(r"3d_model\дача_6x6.FCStd")
