from random import randint

class Track:

    def __init__(self, sx, sy, length, width, dir) -> None:
        self.startx = sx
        self.starty = sy
        self.endx = sx+length if dir == "HOR" else sx
        self.endy = sy if dir == "HOR" else sy-length
        self.length = length
        self.width = width
        self.dir = dir


class TrackBuilder:

    def __init__(self) -> None:
        self.sections = []

    def build_track(self, width, height):

        lastmoves = ["empty", "empty"]
        x = randint(width/4,width-(width/4))
        y = height
        direction = "VER"
        while True:

            if x < 0 or x > width or y < 0 or y > height:
                break
            
            temp:Track = Track(x, y, randint(50,100), 30, direction)
            self.sections.append(Track(x, y, randint(50,100), 30, direction))
            if direction == "HOR":
                direction = "VER"
                x = temp.endx+(temp.width/2)
                y = temp.endy+(temp.width/2)
            else:
                direction = "HOR"
                x = temp.endx-(temp.width/2)
                y = temp.endy-(temp.width/2)


          
