# We want a new version of DraggableRectangle which allows for rotation
# on right clicks and for names to be displayed


class OfficeObject:
    def __init__(self, rect):
        self.rect = rect
        self.press = None

    def connect(self):
        '''connect to all the events we need'''
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        '''on button press we will see if the mouse is over us and store
        some data'''
        if event.inaxes != self.rect.axes:
            return

        contains, _attrd = self.rect.contains(event)
        if not contains:
            return

        if event.button == 1:
            x0, y0 = self.rect.xy
            self.press = x0, y0, event.xdata, event.ydata
        else:
            w, h = self.rect.get_width(), self.rect.get_height()
            self.rect.set_width(h)
            self.rect.set_height(w)

    def on_motion(self, event):
        '''on motion we will move the rect if the mouse is over us'''
        if self.press is None:
            return
        if event.inaxes != self.rect.axes:
            return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        self.rect.figure.canvas.draw()

    def on_release(self, event):
        '''on release we reset the press data'''
        self.press = None
        self.rect.figure.canvas.draw()

    def disconnect(self):
        '''disconnect all the stored connection ids'''
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)