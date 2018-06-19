import math
import numpy as np


def angle(a):
    x, y = a[0], a[1]
    if x in range(201) and y in range(201):
        slope = float((200 - y) / float(200 - x))
        return math.atan(slope) * 180.0 / math.pi + 90
    elif x in range(201, 401) and y in range(201):
        slope = float((200 - y) / float(x - 200))
        return math.atan(slope) * 180.0 / math.pi
    elif x in range(201) and y in range(201, 401):
        slope = float((y - 200) / float(200 - x))
        return math.atan(slope) * 180.0 / math.pi + 180
    elif x in range(201, 401) and y in range(201, 401):
        slope = float((y - 200) / float(x - 200))
        return math.atan(slope) * 180.0 / math.pi + 270


print angle([333, 67, 0])
