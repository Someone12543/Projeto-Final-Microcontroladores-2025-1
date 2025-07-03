from svgelements import SVG

class Svg_communicator:
    def __init__(self):
        pass
    
    def communicate(self, filename):
        svg = SVG.parse(filename)
        for element in svg:
            print(len(element.points))
            print(element.stroke)
            for point in element.points:
                print(point.x, point.y)
                input("Awating OK")

communicator = Svg_communicator()

communicator.communicate("maca.svg")
