from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r = (255,0,0)
b = (0,0,0)
w = (255,255,255)
g = (218,165,32)

x = 1
y = 1


maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,g,r,r]]


game_over = False        


def check_wall(x,y,new_x,new_y):
  if maze[new_y][new_x] != r:
    return new_x, new_y
  elif maze[new_y][x] != r:
    return x, new_y
  elif maze[y][new_x] != r:
    return new_x, y
  else:
    return x,y

def move_marble(pitch, roll, x, y):
  new_x = x
  new_y = y
  if 1 < pitch < 179 and x != 0:
    new_x -= 1
  elif 181 < pitch < 359 and x != 7:
    new_x += 1
  elif 1 < roll < 179 and y != 7:
    new_y += 1
  elif 181 < roll < 359 and y != 0:
    new_y -= 1
  new_x, new_y = check_wall(x,y,new_x,new_y)
  return new_x, new_y

while game_over == False:
  pitch = sense.get_orientation()['pitch']
  roll = sense.get_orientation()['roll']
  x,y = move_marble(pitch, roll, x,y)
  if maze[x][y] == g:
    sense.show_message("Victory!!!!")
    game_over = True
  maze[y][x] = w
  sense.set_pixels(sum(maze,[]))
  sleep(0.05)
  maze[y][x] = b