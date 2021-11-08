import math


class Triangle(object):
    def __init__(self, col, row, idx):
        self.col = col
        self.row = row
        self.id = idx
        self.size = 30
        self.new_size = 30
        # self.location = new PVector((col*delta_width) + delta_width, (row * delta_height) + delta_height);
        # self.newLocation = new PVector((col*delta_width) + delta_width, (row * delta_height) + delta_height);

        # Each triangle has a location and then its points are calculated from that one point.
        self.calc_size()
        self.hue = self.id / 10
        self.hue_change = 0.1
        self.hue_offset = 0
        self.new_hue_offset = 0
        self.inner_opacity = 30

        self.x_spin = 0
        self.y_spin = 0
        self.z_spin = 0
        self.x_spin_change = 0.01
        self.y_spin_change = 0.01
        self.z_spin_change = 0.01
        self.spin_offset = 0
        self.new_spin_offset = 0

        self.thickness = 2

    def update(self):
        # Spin and update hue
        self.x_spin += self.x_spin_change
        self.y_spin += self.y_spin_change
        self.z_spin += self.z_spin_change
        self.hue += self.hue_change

        # Animate towards new location when the x and y value change due to number of cols/rows changing
        # PVector direction = PVector.sub(newLocation, location);
        # direction = direction.div(animation_speed);
        # location = location.add(direction);

        # Animate towards new size
        delta_size = self.new_size - self.size
        delta_size = delta_size / animation_speed
        self.size += delta_size

        # Animate towards new spin offset
        delta_spin = self.new_spin_offset - self.spin_offset
        delta_spin = delta_spin / animation_speed
        self.spin_offset += delta_spin

        # Animate towards new hue offset
        delta_hue = self.new_hue_offset - self.hue_offset
        delta_hue = delta_hue / animation_speed
        self.hue_offset += delta_hue

        # Recalc the trigonometry that finds the points, since the size of the triangle might have changed
        self.calc_size()

    # def display():
    #     fill((hue+hueOffset)%100,80,100,innerOpacity);
    #     stroke((hue+hueOffset)%100, 100,100);
    #     strokeWeight(thickness);

    #     pushMatrix();
    #     translate(centre.x+100,centre.y,id*3);
    #     rotateZ(zSpin + spinOffset);
    #     rotateX(self.x_spin + spinOffset);
    #     rotateY(self.y_spin + spinOffset);
    #     triangle(pointA.x, pointA.y, pointB.x, pointB.y, pointC.x, pointC.y);
    #     popMatrix();

    # Trigonomentry.
    def calc_size(self):
        self.h = math.sin(1.0472) * self.size
        self.ch = math.sin(0.523599) * (self.h / 2)

        if self.id % 2:
            # centre = new PVector (location.x, location.y-h+ch);
            # pointA = new PVector(-(size/2), -ch);
            # pointB = new PVector(0, h-ch);
            # pointC = new PVector(size/2, -ch);
            centre = 2
        else:
            # centre = new PVector (location.x-size/2, location.y-ch);
            # pointA = new PVector(-(size/2), ch);
            # pointB = new PVector(size/2, ch);
            # pointC = new PVector(0, ch-h);
            centre = 3

    # figure out new locations when the number of cols or rows changes
    def recalc_x(self):
        self.new_location.x = (self.col * delta_width) + delta_width

    def recalc_y(self):
        self.new_location.y = (self.row * delta_height) + delta_height
