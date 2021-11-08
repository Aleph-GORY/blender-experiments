from ..midicontroller import linear_interpolation
from triangle import Triangle


animation_speed = 50

# Setting up the triangles
delta_width = 100
delta_height = 100
cols = 23
rows = 11
n_triangles = cols * rows
triangles = []

# Lowering this leads to fadeytrails.
background_opacity = 100


def setup():
    # size(1920,1080,P3D);
    # fullScreen(P3D);
    # colorMode(HSB, 100);
    # background(0);
    # smooth();

    # MidiBus.list(); // List all available Midi devices on STDOUT. This will show each device's index and name.
    # myBus = new MidiBus(this, 1, 2); // Create a new MidiBus object

    # Create an array of all the triangles
    for i in range(n_triangles):
        row = i // cols
        col = i % cols
        triangles.append(Triangle(col, row, i))


def draw():

    # draw the background huge and far away - if it's at the regular position in the z axis, it cuts into the triangles as they rotate
    #   fill(0,0,0,backgroundOpacity);
    #   translate(-width*2, -height*2, -500);
    #   rect(0,0,width*5,height*5);
    #   translate(width*2, height*2, 500);

    # Update and draw all the triangles
    for i in range(n_triangles):
        triangles[i].update()
        if triangles[i].row < rows and triangles[i].col < cols:
            triangles[i].display()

    # Print the framerate - for troubleshooting


#    fill(100,0,100);
#    textSize(30);
#    text(frameRate, 10, 50);


# //void keyPressed(){

# //  // If you don't have a midicontroller, you can control variables in steps using a keyboard
# //  if (keyCode == UP){
# //    for (int i=0; i<numOfTriangles; i++){
# //      triangles[i].newSize+=10;
# //    }
# //  }

# //  if (keyCode == DOWN){
# //    for (int i=0; i<numOfTriangles; i++){
# //      triangles[i].newSize-=10;
# //    }
# //  }

# //   if (keyCode == LEFT){
# //    backgroundOpacity-=10;
# //  }

# //  if (keyCode == RIGHT){
# //    backgroundOpacity+=10;
# //  }

# //}
