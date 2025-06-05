
import FreeCAD, Part

doc = FreeCAD.newDocument('House')
foundation = Part.makeBox(9000.0, 7000.0, 600.0)
foundation_obj = doc.addObject("Part::Feature", "Foundation")
foundation_obj.Shape = foundation

outer_wall = Part.makeBox(9000.0, 7000.0, 8000.0)
inner_wall = Part.makeBox(
    9000.0-2*220.0, 
    7000.0-2*220.0, 
    8000.0-600.0
)
inner_wall.translate(FreeCAD.Vector(220.0, 220.0, 600.0))
walls = outer_wall.cut(inner_wall)
walls_obj = doc.addObject("Part::Feature", "Walls")
walls_obj.Shape = walls
roof = Part.makeBox(9000.0, 7000.0, 100)

roof_obj = doc.addObject("Part::Feature", "Roof")
roof_obj.Shape = roof
roof_obj.Placement.Base = FreeCAD.Vector(0,0,8000.0)

doc.recompute()
doc.saveAs(r"3d_model\Центр_логистики_CL-900.FCStd")
