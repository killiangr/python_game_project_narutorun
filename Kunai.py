import arcade
import math


class Kunai(object):
    def __init__(self):     #initialisation
        super().__init__()
        self.nb_kunai = 30

    # def setup(self):
    #     self.kunai_list = arcade.SpriteList()

    def on_key_press(self, x, y, xf, yf, scale, speed, kunai_list):     #deplacement kunai vers la cible
        chem_sprite: str = "assets/sprites/naruto_sheet.gif"
        kunai = arcade.Sprite(chem_sprite, scale, 363, 878, 15, 15)
        deb_x = x
        deb_y = y
        kunai.center_x = deb_x
        kunai.center_y = deb_y
        fin_x = xf
        fin_y = yf
        x_diff = fin_x - deb_x
        y_diff = fin_y - deb_y
        angle = math.atan2(y_diff, x_diff)
        kunai.angle = math.degrees(angle)
        kunai.change_x = math.cos(angle) * speed
        kunai.change_y = math.sin(angle) * speed
        kunai_list.append(kunai)
        # print("shoot")

    # def draw(self):
    #     self.kunai_list.draw()
    #
    # def update(self):
    #     self.kunai_list.update()
