import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, GLib, Gdk
import cv2

class Page1(Gtk.Grid):

    def __init__(self, main_window, stack):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.drawing_area = Gtk.DrawingArea()
        self.drawing_area.connect("draw", self.on_draw)
        self.add(self.drawing_area)
    
    def on_draw(self, widget, cr):
        # Set line color
        cr.set_source_rgb(0.15, 0.55, 0.25)

        # Set line width
        cr.set_line_width(8)

        # Move to the starting point (x1, y1)
        x = 100  # X-coordinate of the top-left corner
        y = 100  # Y-coordinate of the top-left corner
        width = 200  # Width of the rectangle
        height = 150  # Height of the rectangle

        cr.rectangle(x, y, width, height)
        cr.stroke()