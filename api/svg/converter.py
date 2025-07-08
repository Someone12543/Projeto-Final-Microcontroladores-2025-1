from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import cv2 as cv
import svgwrite
from skimage.morphology import skeletonize

class Svg_converter:
    def __init__(self):
        
        # Data storage
        self.x_data = []
        self.y_data = []
    
    def convert(self, image_path, svg_path):
        # Load theimage

        image = Image.open(image_path).convert("L")  # Convert to grayscale

        # Convert image to numpy array
        image_np = np.array(image)

        # Apply a threshold
        _, binary = cv.threshold(image_np, 150, 255, cv.THRESH_TOZERO_INV)
        
        # Skeletonize (single-pixel-wide lines)
        skeleton = skeletonize(binary)
        skeleton = (skeleton * 255).astype(np.uint8)
        
        # Find contours with this threshold
        contours, _ = cv.findContours(skeleton, cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
        
        # Create new SVG with contours
        dwg = svgwrite.Drawing(size=(image.width, image.height))
        for contour in contours:
            points = [(int(p[0][0]), int(p[0][1])) for p in contour]
            dwg.add(dwg.polyline(points=points, stroke='black', fill='none', stroke_width=1))
            
            new_line_x = []
            new_line_y = []
            
            for point in points:
                new_line_x.append(point[0])
                new_line_y.append(image.height-point[1])
                #self.x_data.append(point[0])
                #self.y_data.append(image.height-point[1])
                
            self.x_data.append(new_line_x)
            self.y_data.append(new_line_y)
        
        fig, ax = plt.subplots()
        
        x = []
        y = []
        
        self.line_count = 0
        self.atual_size = len(self.x_data[self.line_count])
        self.anterior_size = 0
        
        # update function to update data and plot
        def update(frame):
            # updating the data by adding one more point
            if self.atual_size - frame + self.anterior_size > 0:
                x.append(self.x_data[self.line_count][frame - self.anterior_size])
                y.append(self.y_data[self.line_count][frame - self.anterior_size])
            else:
                self.line_count += 1
                self.anterior_size += self.atual_size
                self.atual_size = len(self.x_data[self.line_count])
                x.append(self.x_data[self.line_count][frame - self.anterior_size])
                y.append(self.y_data[self.line_count][frame - self.anterior_size])
                print(self.line_count)
            
            ax.clear()  # clearing the axes
            ax.scatter(x,y, c = 'r' if self.line_count % 2 == 0 else 'b')  # creating new scatter chart with updated data
            fig.canvas.draw()  # forcing the artist to redraw itself

        # anim = animation.FuncAnimation(fig, update, interval=0)
        # plt.show()
        
        # Save the SVG
        dwg.saveas(svg_path)


if __name__ == '__main__':
    Converter = Svg_converter()

    #Converter.convert("vaporwave.png", "vaporwave.svg")
    Converter.convert("maca.png", "maca.svg")
