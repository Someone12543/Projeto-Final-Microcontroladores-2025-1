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
            #meu_serial.write( str(len(element.points)).encode("UTF-8") )
            #meu_serial.write( str(element.stroke).encode("UTF-8") )
            
#             listinha = ''
#             
#             for point in element.points:
#                 listinha += str(int(point.x)) + "," + str(int(point.y)) + " "
                
                
#             meu_serial.write(listinha.encode("UTF-8"))
#             
#             for i in range(qtd):
#                 msg = ""
#                 while True:
#                     msg = meu_serial.readline().decode().strip()
#                     if msg:
#                         break
#                 print(msg)
#                 
            
            for point in element.points:
                meu_serial.write(("1\n").encode("UTF-8"))
                ponto = str(int(point.x)) + ',' + str(int(point.y)) + '\n'
                meu_serial.write( (ponto).encode("UTF-8") )
                
                while 1:
                    texto_recebido = meu_serial.readline().decode(errors='ignore').strip()
                    if texto_recebido:
                        print(texto_recebido)
                        if texto_recebido == "167,1061":
                            print(point.x, point.y)
                        break
            print(count)
            count += 1
                    
                
                

communicator = Svg_communicator()

communicator.communicate("maca.svg")
