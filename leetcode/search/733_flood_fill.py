class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(x, y):
            """
            if not in area, not origColor, or visited: return
            fill in newColor
            call fill on 4 directions
            """
            if not (0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] != -1 and image[x][y] == origColor):
                return
            image[x][y] = -1
            for dir in dirs:
                fill(x+dir[0], y+dir[1])
            image[x][y] = newColor
        
        origColor = image[sr][sc]
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        fill(sr, sc)
        return image
