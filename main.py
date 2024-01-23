#créé par Enzo Sanchez Valero et Mikolai Szychowski
#créé le 10\01\24
#TP4


import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle():
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color


    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
           de votre jeu à l'écran.
        """


        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
        #arcade.draw_circle_filled()


    def update(self, cercle_change_x, cercle_change_y, rayon):

        self.x += cercle_change_x
        self.y += cercle_change_y

        if self.x < rayon:
            pass
        if self.x > SCREEN_WIDTH - rayon:
            pass
        if self.y < rayon:
            pass
        if self.y > SCREEN_HEIGHT - rayon:
            pass
        if self.x < rayon:
            self.x *= -1


class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.liste_balle = []


        def setup(self):

            pass

        def on_update(self, delta_time: float):
            pass

        def on_draw(self):

            arcade.start_render()

            for i in self.liste_balle:
                i.on_draw(arcade.color.BLUE)
                i.on_draw(arcade.color.RED)
                i.on_draw(arcade.color.GREEN)

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            ball = Balle(x,y, random.randint(0,50), random.randint(0,50), random.randint(0,50), self.liste_balle)
            self.liste_balle.append(ball)


def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()
