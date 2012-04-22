#!/usr/bin/python

import tempfile
import subprocess
import os.path

from gi.repository import Gtk
import generator

PDF_COMMAND = "wkhtmltopdf -s letter -B 1in -L 1in -R 1in -T .70in"

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
        file_path = self.file_chooser_btn.get_filename()
        html = self._generate_html(file_path)
        response = self.save_dialog.run()
        self.save_dialog.hide()
        
        html_file = self.save_dialog.get_filename()
        with open(html_file, 'w') as f:
            f.write(html)
        
        subprocess.call(['xdg-open', html_file])
    
    def on_pdf_button_clicked(self, widget):
        file_path = self.file_chooser_btn.get_filename()
        print self._generate_pdf(file_path)
            
    def _generate_html(self, yaml_file):
        html = generator.render_html(yaml_file)
        return html
    
    def _generate_pdf(self, yaml_file):
        html = self._generate_html(yaml_file)
        temp = tempfile.NamedTemporaryFile(suffix=".html")
        temp.write(html)
        html_file = temp.name
        pdf_file = os.path.splitext(temp.name)[0] + ".pdf"
        
        full_command = PDF_COMMAND.split() + [html_file, pdf_file]
        subprocess.call(full_command)
        
        return pdf_file

if __name__ == "__main__":

    app = ResumeMaker()
    app.main_window.connect("delete-event", Gtk.main_quit)
    app.main_window.show_all()
    Gtk.main()
