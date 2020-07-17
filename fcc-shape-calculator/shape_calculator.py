class Rectangle:
  def __init__(self, width, height): 
        self.width = width
        self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    for i in range(self.height):
      for i in range(self.width):
        picture += "*"
      picture += "\n"
    return picture

  def get_amount_inside(self, another):
    return int(self.get_area()/another.get_area())

  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

class Square(Rectangle):
  def __init__(self, side):
    Rectangle.__init__(self, side, side)

  def set_side(self, side):
    Rectangle.set_width(self, side)
    Rectangle.set_height(self, side)

  def set_width(self, width):
    Rectangle.set_width(self, width)
    Rectangle.set_height(self, width)
  
  def set_height(self, height):
    Rectangle.set_width(self, height)
    Rectangle.set_height(self, height)

  def __str__(self):
    return "Square(side="+str(self.width)+")"
