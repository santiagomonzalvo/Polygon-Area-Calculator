class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = (self.width * self.height)
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2)**.5
    return diagonal

  def get_picture(self):
    if self.width < 50 and self.height < 50:
      shape = ("*" * self.width + "\n") * self.height
    else:
      shape = "Too big for picture."
    return shape

  def get_amount_inside(self, shape):
    if isinstance(shape, Rectangle):
      width_fit = self.width // shape.width
      height_fit = self.height // shape.height
      return width_fit * height_fit
    elif isinstance(shape, Square):
      fit = self.width // shape.side
      return fit * fit

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    #output: Rectangle(width=5, height=10)


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)
    self.side = side

  def set_side(self, side):
    self.side = side
    self.width = side
    self.height = side

  def __str__(self):
    return f'Square(side={self.side})'
    #output: Square(side=9)
  def set_width(self, width):
    self.set_side(width)
  def set_height(self, height):
    self.set_side(height)
