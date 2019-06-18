#import PIL
import bpy
#import matplotlib.pyplot as plt

#see template mathematics
global sc
sc = 0.28867513459481288225

class line:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def get_children(self):
        a = self. start
        e = self.end

        j = e.x-a.x
        k = e.y-a.y

        b = coordinate((j/3)+a.x,(k/3)+a.y)
        d = coordinate(2*(j/3)+a.x,2*(k/3)+a.y)
        m = coordinate((j/2)+a.x,(k/2)+a.y)

        px = -1 * k * sc
        py = j * sc
        c = coordinate(m.x+px,m.y+py)

        A = line(a,b)
        B = line(b,c)
        C = line(c,d)
        D = line(d,e)

        return A,B,C,D
    def __str__(self):
        return 'line[{}:{}]'.format(str(self.start),str(self.end))
class coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def get_scale(self,c):
        return coordinate(self.x*c,self.y*c)
    def get_translate(self,a,b):
        return coordinate(self.x+a,self.y+b)
    def __str__(self):
        return '({},{})'.format(self.x,self.y)

def i_lines(l):
    g = [i.get_children() for i in l]
    return [item for sublist in g for item in sublist]
def getSTR_l(l):
    return '{} {} {}'.format('{','}'" , ".join([str(i) for i in l]),'}')

n = [line(coordinate(0,0),coordinate(1,0)),]
resolution = 2 #resolution here************************************************************************
for i in range(resolution):
    n = i_lines(n)

#pyplot display
"""xp = []
yp = []
for i in n:
    x = i.start.x
    y = i.start.y
    xp.append(x)
    yp.append(y)

    x = i.end.x
    y = i.end.y
    xp.append(x)
    yp.append(y)
plt.plot(xp,yp)
plt.show()"""

#blender
curveData = bpy.data.curves.new('kochCurve', type='CURVE')

polyline = curveData.splines.new('POLY')
polyline.points.add(len(n))
for e, i in enumerate(n):
    x,y = i.start.x,i.start.y
    polyline.points[e].co = (x, y, 0, 1)
x,y = n[-1].end.x,n[-1].end.y
polyline.points[len(n)].co = (x, y, 0, 1)

# create Object
curveOB = bpy.data.objects.new('kochCurveOBJ', curveData)
curveData.bevel_depth = 0.01

# attach to scene and validate context
scn = bpy.context.scene
scn.objects.link(curveOB)
scn.objects.active = curveOB
