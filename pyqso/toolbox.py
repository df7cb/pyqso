#!/usr/bin/env python
# File: toolbox.py

#    Copyright (C) 2013 Christian Jacobs.

#    This file is part of PyQSO.

#    PyQSO is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    PyQSO is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with PyQSO.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GObject
import logging

from pyqso.dx_cluster import *
from pyqso.grey_line import *
from pyqso.awards import *

class Toolbox(Gtk.Frame):
   
   def __init__(self, root_window):
         
      Gtk.Frame.__init__(self)
      self.set_label("Toolbox")
      self.root_window = root_window

      self.tools = Gtk.Notebook()

      self.dx_cluster = DXCluster(self.root_window)
      self.tools.insert_page(self.dx_cluster, Gtk.Label("DX Cluster"), 0)
      self.grey_line = GreyLine(self.root_window)
      self.tools.insert_page(self.grey_line, Gtk.Label("Grey Line"), 1)
      self.awards = Awards(self.root_window)
      self.tools.insert_page(self.awards, Gtk.Label("Awards"), 2)

      self.add(self.tools)
      self.tools.connect_after("switch-page", self._on_switch_page)

      return

   def toggle_visible_callback(self, widget=None):
      self.set_visible(not self.get_visible())
      return

   def _on_switch_page(self, widget, label, new_page):
      if(type(label) == GreyLine):
         label.draw() # Note that 'label' is actually a GreyLine object.
      return
