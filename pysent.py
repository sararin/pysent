import sys #ugly boilerplate
if sys.version_info[0] == 2:
  import Tkinter
else:
  import tkinter

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
        self.page_holder.append(line)
    return self.presentation

if __name__ == "__main__":
  script, filename = sys.argv[0], sys.argv[1]
  reader = Reader(filename)
  slides = reader.create_presentation()
  # root = tkinter.Tk()
  # w = tkinter.Label(root, text="Hello")
  # w.pack()
  # root.tkinter.mainloop()
