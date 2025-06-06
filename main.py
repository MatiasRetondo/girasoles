import turtle
import json

def draw_from_json(json_file):
  screen = turtle.Screen()
  screen.bgcolor("black")
  screen.setup(800,800)
  t = turtle.Turtle()
  t.hideturtle()
  t.speed(0)
  screen.tracer(0)


  with open(json_file) as f:
    regions = json.load(f)

  all_points = [(p[0],p[1]) for r in regions
                      for p in r['contour']]

  min_x = min(p[0] for p in all_points)
  max_x = max(p[0] for p in all_points)
  min_y = min(p[1] for p in all_points)
  max_y = max(p[1] for p in all_points)

  width = max_x - min_x
  height = max_y - min_y

  scale = min(600 / width, 600 / height)
  center_x = (min_x + max_x) / 2
  center_y = (min_y + max_y) / 2

  for region in regions:
    color = '#{:02x}{:02x}{:02x}'.format(
      int(region['color'][0]),
      int(region['color'][1]),
      int(region['color'][2]))
    t.color(color, color)

    # Dibujar el contorno
    points = region['contour']
    t.begin_fill()
    t.penup()

    x = (points[0][0] - center_x) * scale
    y = (center_y - points[0][1]) * scale
    t.goto(x,y)
    t.pendown()

    for point in points[1:]:
      x = (point[0] - center_x) * scale
      y = (center_y - point[1]) * scale
      t.goto(x,y)

    t.goto((points[0][0] - center_x) * scale,
      (center_y - points[0][1]) * scale)

    t.end_fill()
    screen.update()

  screen.mainloop()

if __name__ == "__main__":
    draw_from_json("sunflower.json")

#----------------------------------
# UNO SIN EL JSON
#import math
#import turtle


#def drawPhyllotacticPattern(turtle, t, petalstart, angle=120, size=2, cspread=4):
#    """print a pattern of circles using spiral phyllotactic data"""
    # initialize position
    # turtle.pen(outline=1,pencolor="black",fillcolor="orange")
#    turtle.color('black')
#    turtle.fillcolor("orange")
#    phi = angle * (math.pi / 180.0)
#    xcenter = 0.0
#    ycenter = 0.0

#    # for loops iterate in this case from the first value until < 4, so
#    for n in range(0, t):
#        r = cspread * math.sqrt(n)
#        theta = n * phi

#        x = r * math.cos(theta) + xcenter
#        y = r * math.sin(theta) + ycenter

#        # move the turtle to that position and draw
#        turtle.up()
#        turtle.setpos(x, y)
#        turtle.down()
#        # orient the turtle correctly
#        turtle.setheading(n * angle)
#        if n > petalstart - 1:
#            turtle.color("yellow")
#            drawPetal(turtle, x, y)
#        else:
#            turtle.stamp()


#def drawPetal(turtle, x, y):
#    turtle.penup()
#    turtle.goto(x, y)
#    turtle.pendown()
#    turtle.color('black')
#    turtle.fillcolor('yellow')
#    turtle.begin_fill()
#    turtle.right(20)
#    turtle.forward(70)
#    turtle.left(40)
#    turtle.forward(70)
#    turtle.left(140)
#    turtle.forward(70)
#    turtle.left(40)
#    turtle.forward(70)
#    turtle.penup()
#    turtle.end_fill()  # this is needed to complete the last petal

#tina = turtle.Turtle()
#tina.shape("turtle")
#tina.speed(0)  # make the turtle go as fast as possible
#drawPhyllotacticPattern(tina, 300, 120, 137.508)
#tina.penup()
#tina.forward(1000)
#tina._position = (150, -250)
#print(tina._position)
#tina._write('Pa tu', align='left', font=("Arial", 20, "normal"))
#turtle.mainloop()