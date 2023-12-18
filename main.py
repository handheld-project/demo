import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Radio Button Example")
        self.set_border_width(10)
        self.set_default_size(800, 480)
        self.radio_button = Gtk.RadioButton.new_with_label_from_widget(None, "Toggle Me")
        self.radio_button.connect("clicked", self.on_radio_clicked)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.pack_start(self.radio_button, True, True, 0)

        self.add(box)

    def on_radio_clicked(self, button):
        # Add your custom logic here to determine when the RadioButton should be toggled
        should_toggle = True  # Change this condition based on your requirements

        if should_toggle:
            button.set_active(not button.get_active())

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
