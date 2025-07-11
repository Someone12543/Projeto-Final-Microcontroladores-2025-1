from svgelements import SVG
from serial import Serial
from time import sleep
import xml.etree.ElementTree as ET

class Svg_communicator:
    def __init__(self):
        pass
    
    def communicate(self, filename):
        try:
            meu_serial = Serial("COM30", baudrate=115200)
            sleep(2)
            # meu_serial = Serial("/dev/ttyACM0", baudrate=115200)
        except Exception as e:
            print(e)
            raise e
        

        count = 1
        print(filename)
        infos = ET.parse(filename).getroot()
        width = infos.get('width')
        height = infos.get('height')

        
        svg = SVG.parse(filename)
        for element in svg:
            try:
                #print(type(element.stroke.value))
                color = (element.stroke.value)
                if color == 255:
                    color = "0\n"
                elif color == 122:
                    color = "1\n"
                else:
                    color = "2\n"
            except:
                color = "0\n"
            
            meu_serial.write( (color).encode("UTF-8"))
            sleep(0.05)
            
            qtd = str(len(element.points)) + "\n"            
            meu_serial.write( (qtd).encode("UTF-8"))
            sleep(0.05)
                           
            for point in element.points:
                if (int(width) < 600) or (int(height) < 600):
                    ponto = str(int(point.x) * 2) + ',' + str(int(point.y) * 2) + '\n'
                else:
                    ponto = str(int(point.x) ) + ',' + str(int(point.y)) + '\n'
                meu_serial.write( (ponto).encode("UTF-8") )
                
                while 1:
                    texto_recebido = meu_serial.readline().decode(errors='ignore').strip()
                    if texto_recebido:
                        print(texto_recebido)
                        break
            print(count)
            count += 1
                             

if __name__ == "__main__":
    communicator = Svg_communicator()
    communicator.communicate("circle.svg")
    #communicator.communicate("../output/image.svg")
