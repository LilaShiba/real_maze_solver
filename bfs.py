# thank you https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image?rq=1

import sys
from multiprocessing import Queue
# pillow
from PIL import Image

#start = (400,984)
#end = (398,25)
start = (10,7)
end = (1768,1791)
def iswhite(value):
    if value >= (180,180,180):
        return True

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(start, end, pixels):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        pixel = path[-1]
        print(pixel)
        if pixel == end:
            return path
        for adjacent in getadjacent(pixel):
            x,y = adjacent
            if iswhite(pixels[x,y]):
                pixels[x,y] = (127,127,127) # see note
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    print("Queue has been exhausted. No answer was found.")


if __name__ == '__main__':

    # invoke: python mazesolver.py <mazefile> <outputfile>[.jpg|.png|etc.]
    base_img = Image.open('maze_2.png')
    base_img = base_img.convert('RGB')
    base_pixels = base_img.load()

    path = BFS(start, end, base_pixels)

    path_img = Image.open('maze_2.png')
    path_pixels = path_img.load()

    for position in path:
        x,y = position
        path_pixels[x,y] = (255,0,0) # red

    path_img.save('green.jpg')
#/myscript.py path/to/img1 path/to/img2
