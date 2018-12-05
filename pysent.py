import sys #ugly boilerplate
if sys.version_info[0] == 2:
  import Tkinter
else:
  from tkinter import *

class Reader: # needs tighter integration and dynamic loading,
              # shouldn't store entire presentation at once
  def __init__(self, filename):
    self.filename = filename
    self.page_holder = []
    self.presentation = []
    
  def _send_current_page(self):
    return self.page_holder
  
  def create_presentation(self):
    with open(self.filename, "r") as f:
      for line in f:
        if line.isspace():
          self.presentation.append(self._send_current_page())
          self.page_holder = []
        else:
          self.page_holder.append(line)
    self.presentation.append(self._send_current_page())
    return self.presentation


def right_key(event):
    global num
    if num < (len(slides) - 1):
      num = num + 1
    w.config(text=''.join(slides[num]))

def left_key(event):
    global num
    if num > 0:
      num = num - 1
    w.config(text=''.join(slides[num]))

if __name__ == "__main__":
  num = 0
  script, filename = sys.argv[0], sys.argv[1]
  reader = Reader(filename)
  slides = reader.create_presentation()

  root = Tk()
  root.bind('<Right>', right_key)
  root.bind('<Left>', left_key)
  w = Label(root, text=''.join(slides[num]))
  w.pack(side=TOP, expand=YES, fill=BOTH)
  root.mainloop()
