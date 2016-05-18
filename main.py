from drag_rect import DraggableRectangle
import matplotlib.pyplot as plt


# Read the list of rectangle objects we need to find space for

# Read previously saved user input if applicable - should be calling line arg

# Plot the two rooms and all of their prohibited regions
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(0, 406)
ax.set_ylim(0, 353)
ax.set_xlabel('X [in]')
ax.set_ylabel('Y [in]')
prohibited_rects = [[0, 0, 132.5, 98],
                    [114, 338, 18.5, 15],
                    [401, 0, 5, 14.5],
                    [401, 338.5, 5, 14.5],
                    [323, 0, 40, 40],
                    [280, 313, 80, 40]]
for rect in prohibited_rects:
    ax.bar(left=rect[0], bottom=rect[1],
           width=rect[2], height=rect[3],
           color='red', alpha=0.5)

# Plot all of the rectangle objects on top of the rooms
desks = [[30, 60],
         [36, 60],
         [30, 45.5]]
drag_rects = []
for desk in desks:
    rect = ax.bar(left=0, bottom=0,
                  width=desk[0], height=desk[1],
                  color='blue', alpha=0.5)
    drag_rect = DraggableRectangle(rect[0])
    drag_rect.connect()
    drag_rects.append(drag_rect)

plt.show()

# Save locations for future loading
