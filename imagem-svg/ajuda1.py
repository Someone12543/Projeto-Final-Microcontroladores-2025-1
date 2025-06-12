import potrace
import numpy as np
from PIL import Image
import svgwrite

def load_image_as_bitmap(path, threshold=128):
    img = Image.open(path).convert("L")  # Grayscale
    img = img.point(lambda x: 0 if x < threshold else 1, '1')  # Binarize
    return np.array(img, dtype=np.uint8)

def trace_bitmap_to_svg(bitmap, svg_path):
    bmp = potrace.Bitmap(bitmap)
    path = bmp.trace()

    height, width = bitmap.shape
    dwg = svgwrite.Drawing(svg_path, size=(width, height))

    for curve in path:
        start = curve.start_point
        d = f"M {start[0]},{start[1]} "

        for segment in curve:
            if isinstance(segment, potrace.Curve):
                c = segment.c
                d += f"C {c[0][0]},{c[0][1]} {c[1][0]},{c[1][1]} {c[2][0]},{c[2][1]} "
            else:
                end = segment.end_point
                d += f"L {end[0]},{end[1]} "

        d += "Z"  # Close path
        dwg.add(dwg.path(d=d, fill='black', stroke='none'))

    dwg.save()
    print(f"Saved traced SVG to: {svg_path}")

def convert_image_to_single_outline_svg(input_path, output_path="output.svg"):
    bitmap = load_image_as_bitmap(input_path)
    trace_bitmap_to_svg(bitmap, output_path)

convert_image_to_single_outline_svg("maca.jpg", "maca.svg")
