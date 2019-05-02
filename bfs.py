# thank you https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image?rq=1
# make sure maze is boxed with black outline. If not, just add that in whatever editor you please

import sys
from multiprocessing import Queue
# pillow
from PIL import Image

# init values
start = (385, 985)
#(10,7)
end = (404,26)
#(1768,1791)
unexplored = [start]
def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(start, end, pixels):
    unexplored = [start]
    parent = {}

    while unexplored:
        node = unexplored.pop(0)
        x,y = node

        if node == end:
            return parent

        for adjacent in getadjacent(node):
            cx,cy = adjacent
            if pixels[cx,cy] >= (180,180,180):
                pixels[cx,cy] = (127,127,127) # see note
                unexplored.append((cx,cy))
                parent[(cx,cy)] = (x,y)

    print("Queue has been exhausted. No answer was found.")

# run program
if __name__ == '__main__':

    # invoke: python mazesolver.py <mazefile> <outputfile>[.jpg|.png|etc.]
    base_img = Image.open('maze.png')
    base_img = base_img.convert('RGB')
    base_pixels = base_img.load()
    # call search algorithm
    path = BFS(start, end, base_pixels)
    # open picture to print path on
    path_img = Image.open('maze.png')
    path_pixels = path_img.load()
    #reconstruct shortest path
    current_node = end
    while current_node != start:
        x,y = current_node
        path_pixels[x,y] = (255,0,0) # red
        current_node = path[current_node]
    # save image
    path_img.save('maze1_bfs.jpg')
