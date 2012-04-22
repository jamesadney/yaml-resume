#!/usr/bin/python
from gi.repository import Gtk

class ResumeMaker():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("resume-maker.ui")
        self.builder.connect_signals(self)
        self._initialize_widgets()
        
    def _initialize_widgets(self):
        self.main_window = self.builder.get_object("main_window")
        self.file_chooser_btn = self.builder.get_object("filechooserbutton")
        self.html_btn = self.builder.get_object("html_button")
        self.pdf_btn = self.builder.get_object("pdf_button")
    
    def on_html_button_clicked(self, widget):
        print self.file_chooser_btn.get_uri()
    
    def on_pdf_button_clicked(self, widget):
        pass

if __name__ == "__main__":

    app = ResumeMaker()
    app.main_window.connect("delete-event", Gtk.main_quit)
    app.main_window.show_all()
    Gtk.main()
