#!/usr/bin/env python

import subprocess
import shutil
from gi.repository import Gtk
import generator


class ResumeMaker():

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("resume-maker.ui")
        self.builder.connect_signals(self)
        self._initialize_widgets()

    def _initialize_widgets(self):
        self.main_window = self.builder.get_object("main_window")
        self.file_chooser_btn = self.builder.get_object("filechooserbutton")
        self.save_dialog = self.builder.get_object("filechooserdialog")
        self.html_btn = self.builder.get_object("html_button")
        self.pdf_btn = self.builder.get_object("pdf_button")

    def on_html_button_clicked(self, widget):
        self._generate_button_clicked(widget, generator.create_html_file)

    def on_pdf_button_clicked(self, widget):
        self._generate_button_clicked(widget, generator.create_pdf_file)

    def _generate_button_clicked(self, widget, generator_method):
        try:
            yaml_file = self.file_chooser_btn.get_filename()
            tempfile = generator_method(yaml_file)
        except TypeError:
            print "Please choose a yaml file"
            return False

        response = self.save_dialog.run()
        self.save_dialog.hide()
        if response == 1:
            dest_file = self.save_dialog.get_filename()
            shutil.move(tempfile, dest_file)

if __name__ == "__main__":

    app = ResumeMaker()
    app.main_window.connect("delete-event", Gtk.main_quit)
    app.main_window.show_all()
    Gtk.main()
