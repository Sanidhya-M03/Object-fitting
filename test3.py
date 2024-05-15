import math
import matplotlib.pyplot as plt
import numpy as np
with open("output.txt", "w") as file:
    file.write("")
with open('L.txt', 'r') as f:
    L = f.read()
with open('B.txt', 'r') as f:
    B = f.read()
with open('S1.txt', 'r') as f:
    S1 = f.read()
with open('S2.txt', 'r') as f:
    S2 = f.read()
with open('S3.txt', 'r') as f:
    S3 = f.read()
with open('S4.txt', 'r') as f:
    S4 = f.read()
with open('C1.txt', 'r') as f:
    C1 = f.read()
with open('C2.txt', 'r') as f:
    C2 = f.read()
with open('C3.txt', 'r') as f:
    C3 = f.read()
width = float(B)
height = float(L)
x = 0
y = 0
fig, ax = plt.subplots()
rect = plt.Rectangle((x, y), width, height, linewidth=1, edgecolor='b', facecolor='none')
ax.add_patch(rect)
ax.set_xlim([x-1, x+width+1])
ax.set_ylim([y-1, y+height+1])
ax.axis('equal')
s4 = float(S4)
if (height>s4+float(C1) and width>s4):
    with open('output.txt', 'a') as file:
        file.write(f"Cordinates of vertices of square4 are (0,0),({s4},0),({s4},{s4}),(0,{s4})")
    x = [0, s4, s4, 0, 0]
    y = [0, 0, s4, s4, 0]    
    plt.fill(x, y, 'b')
else:
    plt.title('The box is small for all objects to fit in')
    pass
s1 = float(S1)
if (height>(s4+s1+float(C1) and width>s1)):
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of vertices of square1 are (0,{s4}),({s1},{s4}),({s1},{(s1+s4)}),(0,{(s1+s4)})")
    x = [0, s1, s1, 0, 0]
    y = [s4, s4, (s1+s4), (s1+s4), s4]
    plt.fill(x, y, 'g')
else:
    plt.title('The box is small for all objects to fit in')
    pass
s2 = float(S2)
if (height>(s2+s2+s4+float(C1)) and width>s2 ):
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of vertices of square2 are(0,{(s4+s1)}),({s2},{(s4+s1)}),({s2},{(s2+s1+s4)}),(0,{(s1+s4)})")
    x = [0 ,s2 ,s2 ,0 ,0] 
    y = [(s4+s1), (s4+s1), (s2+s4+s1), (s2+s1+s4), (s1+s4)]
    plt.fill(x, y, 'y')
else:
    plt.title('The box is small for all objects to fit in')
    pass
s3 = float(S3)
if (height>(s1+s2+s3+s4+float(C1)) and width>s3):
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of vertices of square3 are (0,{(s4+s2+s1)}),({s3},{(s4+s2+s1)}),({s3},{(s1+s2+s3+s4)}),(0,{(s1+s2+s3+s4)})")
    x = [0, s3,s3,0,0]
    y = [(s4+s2+s1),(s4+s2+s1),(s1+s2+s3+s4),(s1+s2+s3+s4),(s2+s1+s4)]
    plt.fill(x,y,'r')
else:
    plt.title('The box is small for all objects to fit in')
    pass
from matplotlib.patches import Circle
r3 = float(C3)
x_cen3, y_cen3 = width-r3, r3
if(width > (s4+2*r3)):
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of center circle1 are {x_cen3}, {y_cen3}")
    circle = Circle((x_cen3, y_cen3), r3, fill=True, color='y')
    ax.add_patch(circle)
else:
    plt.title('The box is small for all objects to fit in')
    pass
r2 = float(C2)
x_cen2, y_cen2 = width-2*r3-r2, r2
if(width > (s4+2*r2+2*r3)):
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of center circle1 are {x_cen2}, {y_cen2}")
    circle = Circle((x_cen2, y_cen2), r2, fill=True, color='g')
    ax.add_patch(circle)
else:
    plt.title('The box is small for all objects to fit in')
    pass
r1= float(C1)
if (width> 2*r1):
    x_cen1,y_cen1 = r1, height-r1
    with open('output.txt', 'a') as file:
        file.write("\n")
        file.write(f"Cordinates of center circle1 are {x_cen1}, {y_cen1}")
    circle = Circle((x_cen1, y_cen1), r1, fill=True, color = 'r')
    ax.add_patch(circle)
else:
    plt.title('The box is small for all objects to fit in')
    pass
plt.show()
