import arcade


class Healthbar(object):
    chem_sprite: str = "assets/backgrounds/healthbar.png"

    def __init__(self, x, y, scale):        #initialisation
        super().__init__()
        self.scale = scale
        self.health = 100
        self.head = arcade.Sprite("assets/backgrounds/narutohead.png", 1, center_x=x - 120, center_y=y - 8)
        # self.health_list=arcade.SpriteList()
        # self.healthsprite = arcade.Sprite(scale=self.scale)
        # self.healthsprite.texture = self.healthbar1im(self.healthbar)
        self.contourhealthbar = arcade.create_rectangle(x, y, 200, 20, arcade.color.BLACK, 1, 0, False)
        self.healthbar = arcade.create_rectangle(x, y, 200 - (2 * (100 - self.health)), 19, arcade.color.ELECTRIC_GREEN)
        self.center_x = x
        self.center_y = y
        # self.health_list.append(self.healthsprite)

    # def healthbar1im(self,healthbar) -> [arcade.Texture]:
    #     if healthbar >= 10:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 0, 361, 33)
    #     elif healthbar >= 9:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 32, 361, 33)
    #     elif healthbar >= 8:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 64, 361, 33)
    #     elif healthbar >= 7:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 96, 361, 33)
    #     elif healthbar >= 6:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 128, 361, 25)
    #     elif healthbar >= 5:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 155, 361, 33)
    #     elif healthbar >= 4:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 185, 361, 33)
    #     elif healthbar >= 3:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 215, 361, 33)
    #     elif healthbar >= 2:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 245, 361, 33)
    #     elif healthbar >= 1:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 275, 361, 33)
    #     elif healthbar >= 0:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 305, 361, 31)
    #     else:
    #         im1 = arcade.load_texture(self.chem_sprite, 0, 305, 361, 31)
    #     return im1

    # def get_sprite(self) -> arcade.Sprite:
    #     return self.health_list[0]

    def health_after_hit(self):     #animation rectangle vie
        # anim=self.get_sprite()
        # anim.texture = self.healthbar1im(self.healthbar)
        self.healthbar = arcade.create_rectangle(self.center_x, self.center_y, 200 - (2 * (100 - self.health)), 19,
                                                 arcade.color.ELECTRIC_GREEN)
        if self.health <= 0:
            self.health = 0

    def draw(self):
        # self.healthsprite.draw()
        self.contourhealthbar.draw()
        self.healthbar.draw()
        self.head.draw()

    # def update(self):
    #     # self.healthsprite.update()
    #     #self.contourhealthbar.draw()
    #       self.healthbar.draw()
    #     #self.head.update()
