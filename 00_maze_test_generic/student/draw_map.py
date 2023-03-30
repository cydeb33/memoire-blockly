import svgwrite
from svgwrite import image

dwg = svgwrite.Drawing('test.svg', profile='tiny')
img = image.Image(href="https://inginious.org/course/blockly/$common/maze_media/background.png")
dwg.add(img)
dwg.save()

def draw_map(matrix):
    # background
    for row in matrix:
        for column in row:
            pass
            # path
            # character
            # goal
            # monsters


