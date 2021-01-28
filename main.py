# импортируем библиотеки pygame как pg чтобы меньше писать
import pygame as pg 
# импортируется волшебная библиотека случайностей
import random

# класс отрисовки матрицы
class MatrixLetters:
    # инициализируем класс
    def __init__(self, app):
        # сохраняем здесь значения из другого класса
        self.app = app
        # символы которые будут использованны
        self.letters = "1234567890"
        # размер символов
        self.font_size = 16
        # устанавливаем шрифт символов, размер, жирный
        self.font = pg.font.SysFont('verdana', self.font_size, bold=True)
        # создаём колонки
        self.columns = app.razmer.current_w // self.font_size
        # создаем список с позициями символов на экране в начале это единица
        self.drops = [1 for i in range(0, self.columns)]
    # функция отрисовки матрицы    
    def draw(self):
        # пробегаемся по каждому символу из списка и отрисрвываем его
        for i in range(0, len(self.drops)):
            # берём случайный символ из строчки с символами
            char = random.choice(self.letters)
            # отрисовываем символы
            char_render = self.font.render(char, False, (0,255,0))
            # позиции символов по X и Y
            pos = i * (self.font_size + 1), (self.drops[i] - 1) * self.font_size
            # обращаемся к поверхности отрисовки что отбражаем и где
            self.app.surface.blit(char_render, pos)
            # если позиция символов превышает границу экрана и значения от 0 до 1 то
            if self.drops[i] * self.font_size > app.razmer.current_h and random.uniform(0,1) > 0.975:
                # то премещаем в начало если нет
                self.drops[i] = 0
            # то сдвигаем на одну позицию в низ
            self.drops[i] = self.drops[i] + 1
    # вызов функции отрисовки на экране
    def run(self):
        self.draw()
        
# основной класс
class MatrixApp:
    def __init__(self):
        # инициализируем pygame
        pg.init()
        # узнаём размер экрана компьютера
        self.razmer = pg.display.Info()
        # переменной RES передаём значения ширины и длины экрана 
        self.RES = self.razmer.current_w, self.razmer.current_h
        # создаём обьект экран нужного размера pg.FULLSCREEN развернёт во весь экран
        self.screen = pg.display.set_mode(self.RES,pg.FULLSCREEN)
        # поверхность для отрисовки обьектов pg.SRCALPHA нужен для прозрачности
        self.surface = pg.Surface(self.RES, pg.SRCALPHA)
        # для отслеживания времени в pygame
        self.clock = pg.time.Clock()
        # передаём в обьект класс MatrixLetters(инициализируем самих себя, то есть класс MatrixApp)
        self.matrixLetters = MatrixLetters(self)
    # функция отрисовки экрана
    def draw(self):
        # заполнение экрана чёрным цветом (R,G,B,прозрачность поверхности) 
        self.surface.fill((0,0,0,8))
        # выполняет функцию run() из класса MatrixLetters()
        self.matrixLetters.run()
        # выводит на экран поверхность отрисовки
        self.screen.blit(self.surface, (0,0))
    # функция запускающая программу    
    def run(self):
        # основной цикл программы (бесконечный)
        while True:
            # отрисовка экрана
            self.draw()
            # закрытие окна по нажатию клавиши ЕND
            [exit() for i in pg.event.get() if i.type == pg.KEYDOWN and i.key == pg.K_END]
            # обновление экрана
            pg.display.flip()
            # частота кадров в секунду
            self.clock.tick(30)
# проверка что файл не импортируется (является исполняемым)
if __name__ == '__main__':
    # обьект арр принадлежит классу MatrixApp, при создании обьекта арр
    # он инициальзируется и выполняется код из функции def __init__(self)
    # класса MatrixApp()
    app = MatrixApp()
    # выполняется метод run() из основного класса MatrixApp()
    app.run()