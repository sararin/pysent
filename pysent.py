import sys
from PIL import Image, ImageDraw, ImageFont

class Reader: # needs tighter integration and dynamic loading,
              # shouldn't store entire presentation at once
  def __init__(self, filename):
    self.filename = filename
    self.page_holder = []
    self.presentation = []
    
  def _send_current_page(self):
    return ''.join(self.page_holder)
  
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

def draw_one_slide(slide, astr):
  MAX_W, MAX_H = 1280, 720 # height and width of image
  im = Image.new('RGB', (MAX_W, MAX_H), (255, 255, 255, 0)) # create new img with those parameters
  draw = ImageDraw.Draw(im) #paint it white

  fontsize = 18
  font = ImageFont.truetype('arial.ttf', fontsize) #set font and size, we will adjust that

  diff = 0 # ratio between size of image and size of text
  while diff > 0.6 or diff < 0.2: # some arbitrary values, diff either bigger than 0.6 or smaller than 0.5
    w, h = draw.multiline_textsize(astr, font=font, spacing=10) # size of entire of text in width x heigh
    # w, h = draw.textsize(line, font=font) # less accurate tho
    diff = (w*h)/(MAX_W*MAX_H) # ratio of those
    if diff > 0.6: #arbitrary val and diff larger than 0.6
      fontsize = fontsize - 1
      font = ImageFont.truetype('arial.ttf', int(fontsize))
    if diff < 0.3: #arbitrary val and diff smaller than 0.5
      fontsize = fontsize + 1
      font = ImageFont.truetype('arial.ttf', int(fontsize))
      
  w, h = draw.multiline_textsize(astr, font=font, spacing=10)
  draw.multiline_text(((MAX_W - w) / 2, (MAX_H - h) / 2), astr, fill=(0,0,0,0), font=font, anchor="Center", spacing=10, align="left")

  im.save(location+slide+'.png')

if __name__ == "__main__":
  num = 0
  script, filename, location = sys.argv[0], sys.argv[1], sys.argv[2]
  reader = Reader(filename)
  slides = reader.create_presentation()
  for y, x in enumerate(slides):
    draw_one_slide(str(y), x, location)
