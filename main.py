from display import *
from draw import *
from parser import *
from matrix import *
import math
from random import randint

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
transform = new_matrix()
scriptFile = "script"

f = open(scriptFile, "r")
filename = f.readlines()[-1].replace("\n", "")

parse_file(scriptFile, edges, polygons, transform, screen, color)
#p = Popen( ['atom', filename ], stdin=PIPE, stdout = PIPE )
#p.communicate()
