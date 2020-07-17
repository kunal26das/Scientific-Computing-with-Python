import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, red = 0, blue = 0, green = 0, yellow = 0):
    self.red = red
    self.blue = blue
    self.green = green
    self.yellow = yellow
    self.set_contents()
    self.total = red + blue + green + yellow
  
  def set_contents(self):
    self.contents = []
    for i in range(self.red):
      self.contents.append("red")
    for i in range(self.blue):
      self.contents.append("blue")
    for i in range(self.green):
      self.contents.append("green")
    for i in range(self.yellow):
      self.contents.append("yellow")
  
  def draw(self, n):
    try:
      balls = random.sample(self.contents, n)
      for ball in balls:
        if ball == "red":
          self.red -= 1
        elif ball == "blue":
          self.blue -= 1
        elif ball == "green":
          self.green -= 1
        elif ball == "yellow":
          self.yellow -= 1
      self.set_contents()
      return balls
    except:
      temp = self.contents
      self.red = 0
      self.blue = 0
      self.green = 0
      self.yellow = 0
      self.contents = []
      return temp

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  print(expected_balls)
  for i in range(num_experiments):
    temp = hat
    drawn_balls = {}
    for ball in temp.draw(num_balls_drawn):
      if ball in drawn_balls:
        drawn_balls[ball] += 1
      else:
        drawn_balls[ball] = 0
    print(drawn_balls)
    flag = True
    for ball in expected_balls:
      try:
        if expected_balls[ball] > drawn_balls[ball]:
          flag = False
          break
      except:
        flag = False
        break
    if flag:
      count += 1
  return count/num_experiments
