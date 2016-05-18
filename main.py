from drag_rect import DraggableRectangle
import matplotlib.pyplot as plt


# Read the list of rectangle objects we need to find space for

# Read previously saved user input if applicable - should be calling line arg

# Plot the two rooms and all of their prohibited regions
fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.set_xlim(0, 406)
ax1.set_ylim(0, 353)
ax1.set_xlabel('X [in]')
ax1.set_ylabel('Y [in]')
prohibited_rects1 = [[0, 0, 132.5, 98],
                     [114, 338, 18.5, 15],
                     [401, 0, 5, 14.5],
                     [401, 338.5, 5, 14.5],
                     [323, 0, 40, 40],
                     [280, 313, 80, 40]]
for rect in prohibited_rects1:
    ax1.bar(left=rect[0], bottom=rect[1],
            width=rect[2], height=rect[3],
            color='red', alpha=0.5)

ax2 = fig.add_subplot(122)
ax2.set_xlim(0, 281)
ax2.set_ylim(0, 353)
ax2.set_xlabel('X [in]')
ax2.set_ylabel('Y [in]')
prohibited_rects2 = [[14, 313, 40, 40],
                     [221, 313, 40, 40],
                     [267, 0, 14, 147],
                     [221, 0, 40, 40],
                     [133, 0, 16, 14],
                     [133, 339, 16, 14]]
for rect in prohibited_rects2:
    ax2.bar(left=rect[0], bottom=rect[1],
            width=rect[2], height=rect[3],
            color='red', alpha=0.5)

# Plot all of the rectangle objects on top of the rooms
desks = [[30, 60],
         [36, 60],
         [30, 45.5]]
drag_rects = []
for desk in desks:
    rect = ax1.bar(left=0, bottom=0,
                   width=desk[0], height=desk[1],
                   color='blue', alpha=0.5)
    drag_rect = DraggableRectangle(rect[0])
    drag_rect.connect()
    drag_rects.append(drag_rect)

plt.show()

# Save locations for future loading
