import sys #ugly boilerplate
if sys.version_info[0] == 2:
  import Tkinter as
else:
  import tkinter
import argparse

if __name__ == "__main__":
  root = tkinter.Tk()
  w = tkinter.Label(root, text="Hello")
  w.pack()
  root.tkinter.mainloop()
