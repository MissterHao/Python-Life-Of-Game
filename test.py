


# class A:
#     _xd = "XDDDD"

#     def __init__(self):
#         self._xd = "QQ"


# # 一開始
# print(A._xd)   # XDDDD
# print(A()._xd) # QQ

# # 改 宣告的
# A()._xd = "YOOOOOOOOOOO"
# print(A._xd)   # XDDDD
# print(A()._xd) # QQ

# # 改 原始的
# A._xd = "HEYYYYYYYY"
# print(A._xd)   # HEYYYYYYYY
# print(A()._xd) # QQ




class World:
    
    def __init__(self):
        self.map = [[0,1,2],[3,4,5],[6,7,8]]
    
    def __str__(self):
        """讓世界架構更好看清楚"""
        print(self.map)
        return ""

    def __getitem__(self, coordinate):
        return self.map[coordinate[1]][coordinate[0]]

    def __setitem__(self, coordinate, value):
        x = coordinate[0]
        y = coordinate[1]
        self.map[y][x] = value