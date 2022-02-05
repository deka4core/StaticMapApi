import pygame


class Button:
    """Класс кнопки"""

    def __init__(self, screen, width, height, inactive_color, active_color, color_text=(255, 255, 255),
                 border_radius=0):
        """Инициализация"""
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.screen = screen
        self.color_text = color_text
        self.border_radius = border_radius

    def draw(self, x, y, action=None):
        """Отрисовка прямоугольника кнопки"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Курсор НА / НЕ НА кнопке
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height),
                             border_radius=self.border_radius)
            if click[0] == 1:
                if action is not None:
                    action()
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height),
                             border_radius=self.border_radius)