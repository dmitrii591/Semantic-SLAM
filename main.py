# import
# нам понадобится библиотека для работы с матрицами и, возможно, кватернионами:)
# import numpy as np

class Point3D:
    # Точка
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Location:
    # Позиционирование объекта.
    # Углы Эйлера: yaw - рысканье, roll - крен, pitch - тангаж
    def __init__(self, point, a=0, b=0, g=0):  # Point3D(point)
        self.position = point
        self.yaw = a
        self.roll = b
        self.pitch = g


# Какая-либо метка на местности. Например, место ожидания, целевая точка итд
class Landmark:
    #ориентир
    def __init__(self, id, location):  # Location(location)
        self.id = id  # целочисленный номер
        self.location = location  # экземпляр Location (включая ориентацию робота по курсу)


# class VolumeLandmark(Landmark):
#    """трехмерный ориентир"""
#    def __init__(self, size_parameters, type, id, location):
#        super().__init__(id, location)

# Параллелипипед
class Box(Landmark):
    def __init__(self, id, location, a, b, c):
        super().__init__(id, location)
        self.length = a
        self.width = b
        self.height = c


# Цилиндр
class Cylider(Landmark):
    def __init__(self, id, location, r, h):
        super().__init__(id, location)
        self.radius = r
        self.height = h


class PlateLandmark(Landmark):
    # Плоскость
    def __init__(self, id, location, points):  # Point3D(points)
        super().__init__(id, location)
        self.points = points  # Список крайних точек


ZoneType = {'WorkZone': 1, 'WayZone': 2};


class Zone:
    """зона"""

    def __init__(self, id, type):
        self.id = id  # целочисленный номер
        self.type = type  # тип зоны


"""
class WorkZone(Zone):
    #рабочая зона
    def __init__(self, Landmarks, id, type=ZoneType['WorkZone']):
        super().__init__(id, type)
        self.landmarks = Landmarks  #список


class WayZone(Zone):
    # Зона без точного картографирования
    def __init__(self, Landmarks, id, type=ZoneType['WayZone']):
        super().__init__(id, type)
        self.landmarks = Landmarks

"""


class Map:
    """карта местности"""

    def __init__(self, id, Zones):
        self.id = id
        self.zones = Zones


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('HI')

