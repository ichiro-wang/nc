# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        rightX, topY = topRight.x, topRight.y
        leftX, botY = bottomLeft.x, bottomLeft.y
        if rightX < leftX or topY < botY:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        if rightX == leftX and topY == botY:
            return 1
        
        midX, midY = (rightX + leftX) // 2, (topY + botY) // 2

        return (
            self.countShips(sea, Point(midX, midY), Point(leftX, botY)) +
            self.countShips(sea, Point(rightX, topY), Point(midX + 1, midY + 1)) +
            self.countShips(sea, Point(midX, topY), Point(leftX, midY + 1)) +
            self.countShips(sea, Point(rightX, midY), Point(midX + 1, botY))
        )
        


