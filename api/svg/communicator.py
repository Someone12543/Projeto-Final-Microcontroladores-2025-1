from svgelements import SVG
from serial import Serial
from time import sleep

class Svg_communicator:
    def __init__(self):
        pass
    
    def communicate(self, filename):
        meu_serial = Serial("COM4", baudrate=115200)
        sleep(2)
        
        count = 1
        
        
        svg = SVG.parse(filename)
        for element in svg:
            meu_serial.write(("0\n").encode("UTF-8"))
            sleep(0.05)
            
            qtd = str(len(element.points)) + "\n"
            sleep(0.05)
            
            meu_serial.write( (qtd).encode("UTF-8"))
            
            #meu_serial.write( str(len(element.points)).encode("UTF-8") )
            #meu_serial.write( str(element.stroke).encode("UTF-8") )
                   
            
            for point in element.points:
                ponto = str(int(point.x)) + ',' + str(int(point.y)) + '\n'
                meu_serial.write( (ponto).encode("UTF-8") )
                
                while 1:
                    texto_recebido = meu_serial.readline().decode(errors='ignore').strip()
                    if texto_recebido:
                        print(texto_recebido)
                        break
            print(count)
            count += 1
            sleep(0.3)
                             

communicator = Svg_communicator()

communicator.communicate("maca.svg")

