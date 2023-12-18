import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Page2(Gtk.Grid):

    def __init__(self, main_window, stack):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)
        self.stack = stack
        self.main_window = main_window
        self.main_window.page1.release_capture()
        self.generate_interface()
        self.set_up_page()

    def generate_interface(self):
        # Button Init
        self.back_button = Gtk.Button(label="Go Back to Page1")
        self.back_button.connect("clicked", self.on_back_button_clicked)

        # Grid init
        self.grid = Gtk.Grid()
        self.grid.set_valign(Gtk.Align.CENTER)
        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.attach(self.back_button, 0, 0, 1, 1)

        self.add(self.grid)

    def set_up_page(self):
        pass  # Add any setup code if needed for Page2

    def on_back_button_clicked(self, button):
        self.stack.set_visible_child_name("page1")

# Usage example:
# main_window = Gtk.Window()
# stack = Gtk.Stack()
# page1 = Page1(main_window, stack)
# page2 = Page2(main_window, stack)
# stack.add_named(page1, "page1")
# stack.add_named(page2, "page2")
# main_window.add(stack)
# main_window.show_all()
# Gtk.main()
