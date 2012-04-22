#!/usr/bin/env python

import yaml
import jinja2

from gi.repository import Gtk

class Resume:

    # close the window and quit
    def delete_event(self, widget, event, data=None):
        Gtk.main_quit()
        return False

    def __init__(self):
        # Create a new window
        self.window = Gtk.Window()

        self.window.set_title("Resume Creator")

        self.window.set_size_request(200, 200)

        self.window.connect("delete_event", self.delete_event)
        
        with open("private_resume.yml") as f:
            resume = yaml.load(f)

        # create a TreeStore with one string column to use as the model
        self.treestore = Gtk.TreeStore(str)

        # we'll add some data now - 4 rows with 3 child rows each
        #for parent in range(4):
            #piter = self.treestore.append(None, ['parent %i' % parent])
            #for child in range(3):
                #self.treestore.append(piter, ['child %i of parent %i' %
                                              #(child, parent)])
        
        self.grep(resume, None)
        
    def grep(self, data, level):
        
        if isinstance(data, dict):
            for key in data:
                entry = self.treestore.append(level, [key])
                self.grep(data[key], entry)
        elif isinstance(data, list):
            for value in data:
                entry = self.treestore.append(level, ["value"])
                self.grep(value, level)
        elif isinstance(data, str):
            entry = self.treestore.append(level, [data])
        
        #for key in data:
            #entry = self.treestore.append(level, [key])
            #if isinstance(data[key], str):
                #self.treestore.append(entry, [data[key]])
            #else:
                #for value in data[key]:
                    #print value
                    #if isinstance(value, str):
                        #self.treestore.append(entry, [value])
                
            

        # create the TreeView using treestore
        self.treeview = Gtk.TreeView(self.treestore)

        # create the TreeViewColumn to display the data
        self.tvcolumn = Gtk.TreeViewColumn('Column 0')

        # add tvcolumn to treeview
        self.treeview.append_column(self.tvcolumn)

        # create a CellRendererText to render the data
        self.cell = Gtk.CellRendererText()

        # add the cell to the tvcolumn and allow it to expand
        self.tvcolumn.pack_start(self.cell, True)

        # set the cell "text" attribute to column 0 - retrieve text
        # from that column in treestore
        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        # make it searchable
        self.treeview.set_search_column(0)

        # Allow sorting on the column
        self.tvcolumn.set_sort_column_id(0)

        # Allow drag and drop reordering of rows
        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    Gtk.main()

if __name__ == "__main__":
    resume_app = Resume()
    main()
