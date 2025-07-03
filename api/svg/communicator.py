from svgelements import SVG
from serial import Serial

class Svg_communicator:
    def __init__(self):
        pass
    
    def communicate(self, filename):
        meu_serial = Serial("/dev/serial0", baudrate=9600)
        
        
        svg = SVG.parse(filename)
        for element in svg:
            meu_serial.write( str(len(element.points)).encode("UTF-8") )
            meu_serial.write( element.stroke.encode("UTF-8") )
            
            
            texto_recebido = "OK"
            for point in element.points:
                while texto_recebido != "OK":
                    texto_recebido = meu_serial.readline().decode().strip()
                    
                meu_serial.write( (str(point.x) + str(point.y)).encode("UTF-8") )
                

communicator = Svg_communicator()

communicator.communicate("maca.svg")
