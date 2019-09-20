#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.

import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.fillcolor(turtle_color)
  my_turtles.append(t)
  
#  this is where the start x and starty is 0
startx = 0
starty = 0 

# move the turtle around
for t in my_turtles:
	t.goto(startx, starty)
	t.right(45)     
	t.forward(50)
    
	# it adds 50 to the starts
	startx = t.xcor()
	starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
