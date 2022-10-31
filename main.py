#import
#нам понадобится библиотека для работы с матрицами и, возможно, кватернионами:)

class Landmark():
    #класс-ориентир содержит основную информацию об ориентире:
    #идентификатор, тип, габариты,
    """описание дома"""
    def __init__ (self, id, type, size_parameters, location):#self обязательно предшествует всем остальным свойствам класса
        """свойства дома"""
        self.id = id#целый номер
        self.type = type#шифр объекта
        self.size_parameters = size_parameters #массив, либо другая структура
        self.location = location #массив, либо другая структура

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('HI')

