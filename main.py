from drag_rect import DraggableRectangle
import matplotlib.pyplot as plt
import sys
import numpy as np
from os.path import isfile
from numpy.random import rand

# Plot the two rooms and all of their prohibited regions
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.set_xlim(0, 406+281)
ax.set_ylim(0, 353)
ax.axvline(406, color='black')
prohibited_rects = [[0, 0, 132.5, 98],
                    [114, 338, 18.5, 15],
                    [401, 0, 5, 14.5],
                    [401, 338.5, 5, 14.5],
                    [323, 0, 40, 40],
                    [280, 313, 80, 40],
                    [14+406, 313, 40, 40],
                    [221+406, 313, 40, 40],
                    [267+406, 0, 14, 147],
                    [221+406, 0, 40, 40],
                    [133+406, 0, 16, 14],
                    [133+406, 339, 16, 14]]
for rect in prohibited_rects:
    ax.bar(left=rect[0], bottom=rect[1],
           width=rect[2], height=rect[3],
           color='red', alpha=0.5)

# Read previously saved user input if applicable - should be calling arg
if len(sys.argv) == 2:
    fn = sys.argv[1]
else:
    fn = 'default.csv'
types = 'S64,S64,f8,f8,i8,f8,f8'
objs = np.genfromtxt(fn, dtype=types, delimiter=',', names=True)

# Plot all of the objects
drag_rects = []
for obj in objs:
    # Randomize starting coordinates if they're 0,0
    if obj['x0'] == 0 and obj['y0'] == 0:
        obj['x0'] = rand()*(ax.get_xlim()[1]-max(obj['wid'], obj['len']))
        obj['y0'] = rand()*(ax.get_ylim()[1]-max(obj['wid'], obj['len']))
    # Branching colors for different object types
    if obj['type'] == 'desk':
        col = 'blue'
    if obj['type'] == 'book':
        col = 'green'
    if obj['type'] == 'div':
        col = 'black'
    rect = ax.bar(left=(1-obj['rot'])*obj['x0']+obj['rot']*obj['y0'],
                  bottom=(1-obj['rot'])*obj['y0']+obj['rot']*obj['x0'],
                  width=(1-obj['rot'])*obj['len']+obj['rot']*obj['wid'],
                  height=(1-obj['rot'])*obj['wid']+obj['rot']*obj['len'],
                  color=col, alpha=0.5)
    drag_rect = DraggableRectangle(rect[0])
    drag_rect.connect()
    drag_rects.append(drag_rect)

plt.show()

# Replace the object array with our relocated objects from the plot

# Save locations for future loading
for i in range(100):
    if not isfile('save'+str(i).zfill(2)+'.csv'):
        np.savetxt('save'+str(i).zfill(2)+'.csv', objs, delimiter=',',
                   fmt=['%s', '%s', '%f', '%f', '%i', '%f', '%f'],
                   header='name,type,len,wid,rot,x0,y0',
                   comments='')
        break
    if i == 99:
        print 'No save space left!'
