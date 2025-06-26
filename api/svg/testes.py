from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
import svgwrite
from skimage.morphology import skeletonize

class Svg_converter:
    def __init__(self):
        pass
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

        ax = plt.subplot(1, 1, 1)
        
        # Create new SVG with contours
        dwg = svgwrite.Drawing(size=(image.width, image.height))
        for contour in contours:
            points = [(int(p[0][0]), int(p[0][1])) for p in contour]
            dwg.add(dwg.polyline(points=points, stroke='black', fill='none', stroke_width=1))

            for point in points:
                ax.plot(point[0], point[1], 'o')
                plt.show()

            
        
        # Save the SVG
        dwg.saveas(svg_path)

Converter = Svg_converter()

Converter.convert("maca.png", "maca.svg")
