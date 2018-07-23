
class Polygon:
  def __init__(self, *sides):
    self.sides = sides
  
  def get_sides(self):
    return self.sides
  
  def perimeter(self):
    return sum(self.sides)

class Triangle(Polygon):
  def __init__(self, a, b, c):
    self.sides = [a, b, c]
  
class PerfectTriangleRectangle(Triangle):
  def __init__(self, a, b, c):
    if(a!=b): 
      raise Exception("Not a triangle rectangle")
    Triangle.__init__(self, a, b, c)

  def get_hypotenuse(self):
    return self.sides[-1] 

def test_triangle():
  triangleA = {'a':2, 'c':5, 'b':2} 
  polygon = PerfectTriangleRectangle(**triangleA)
  print("The sides are " + str(polygon.get_sides()))
  print("The hypotenuse is " + str(polygon.get_hypotenuse()))
  print(type(polygon.get_sides()))

if __name__ == '__main__':
  test_triangle()