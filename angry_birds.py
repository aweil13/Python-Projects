class AngryBird:
  def __init__(self):
    self.x = 0
    self.y = 0
  
  def move_up(self, delta):
    self.y += delta


bird = AngryBird()

print(bird.y)
bird.move_up(3)
print(bird.y)
bird.move_up(6)
print(bird.y)