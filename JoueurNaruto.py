import arcade
from Joueur import Joueur
from heath import Healthbar
from Kunai import Kunai


class JoueurNaruto(Joueur):
    def __init__(self, x, y, direction, SCALE, xh, yh, sh):     #initialisation
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.direction = direction
        # self.player_list = arcade.SpriteList()
        self.animations = AnimationNaruto(self.center_x, self.center_y, self.direction, SCALE)
        self.health = Healthbar(xh, yh, sh)
        self.x_h = xh
        self.y_h = yh
        self.s_h = sh
        self.kunai = Kunai()

    def start(self, change_x):      #appel animation
        self.animations.get_sprite().center_x += change_x
        self.animations.start_x(self.animations.get_sprite().center_x, change_x)

    def move(self, change_x): #appel animation
        self.animations.get_sprite().center_x += change_x
        self.animations.move_x(self.animations.get_sprite().center_x, change_x)

    def jump(self, change_x, change_y): #appel animation
        self.animations.jump_y(self.animations.get_sprite().center_x, self.animations.get_sprite().center_y, change_x,
                               change_y)

    def stop(self, pressed):  #appel animation
        self.animations.stop_move(pressed)

    def attack(self, change_x, pressed, PLAYER_SPEED):  #appel animation
        self.animations.get_sprite().center_x += change_x
        self.animations.attack_move(self.animations.get_sprite().center_x, change_x, pressed, PLAYER_SPEED)

    def damaged(self, pressed):  #appel animation
        self.animations.damaged_move(pressed)
        self.health.__init__(self.x_h, self.y_h, self.s_h)

    def thraw(self, change_x, pressed):  #appel animation
        self.animations.get_sprite().center_x += change_x
        self.animations.thraw_move(self.animations.get_sprite().center_x, pressed)

    def draw(self):
        self.animations.draw()
        self.health.draw()
        # self.kunai.draw()

    def update(self):  #update
        self.animations.update()
        self.health.update()
        self.kunai.update()


class AnimationNaruto(object):
    chem_sprite: str = "assets/sprites/naruto_sheet.gif"

    def __init__(self, x, y, direction, scale):  #initialisation
        super().__init__()
        self.scale = scale
        self.player_list = arcade.SpriteList()
        move_sprite = arcade.AnimatedTimeSprite(scale=self.scale)
        move_sprite.position = [x, y]
        move_sprite.textures = self.stand_animation(direction)
        self.player_list.append(move_sprite)

    def start_move_animation(self, direction) -> [arcade.Texture]:  #commencement deplacement
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 5, 100, 50, 55, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 60, 100, 51, 55, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 117, 106, 58, 55, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 189, 106, 62, 55, mirrored=mirror)
        im5 = arcade.load_texture(self.chem_sprite, 279, 108, 54, 44, mirrored=mirror)
        im6 = arcade.load_texture(self.chem_sprite, 362, 106, 55, 43, mirrored=mirror)
        im7 = arcade.load_texture(self.chem_sprite, 456, 109, 51, 39, mirrored=mirror)
        im8 = arcade.load_texture(self.chem_sprite, 549, 111, 50, 39, mirrored=mirror)
        im9 = arcade.load_texture(self.chem_sprite, 47, 173, 62, 41, mirrored=mirror)
        im10 = arcade.load_texture(self.chem_sprite, 165, 173, 62, 41, mirrored=mirror)
        im11 = arcade.load_texture(self.chem_sprite, 293, 174, 54, 44, mirrored=mirror)
        return [im10, im11, im1, im2, im3, im4, im5, im6, im7, im8, im9]

    def move_animation(self, direction) -> [arcade.Texture]:        #deplacement max
        mirror = (direction == "left")
        im12 = arcade.load_texture(self.chem_sprite, 4, 236, 57, 47, mirrored=mirror)
        im13 = arcade.load_texture(self.chem_sprite, 62, 242, 51, 41, mirrored=mirror)
        im14 = arcade.load_texture(self.chem_sprite, 114, 242, 63, 41, mirrored=mirror)
        im15 = arcade.load_texture(self.chem_sprite, 177, 240, 63, 43, mirrored=mirror)
        im16 = arcade.load_texture(self.chem_sprite, 240, 243, 53, 39, mirrored=mirror)
        im17 = arcade.load_texture(self.chem_sprite, 302, 236, 62, 46, mirrored=mirror)
        return [im12, im13, im14, im15, im16, im17]

    def stand_animation(self, direction) -> [arcade.Texture]:       #reste debout
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 15, 18, 41, 55, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 63, 18, 41, 55, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 111, 18, 41, 55, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 160, 18, 41, 55, mirrored=mirror)
        return [im1, im2, im3, im4]

    def attack_animation(self, direction) -> [arcade.Texture]:      #attaque
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 14, 453, 47, 49, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 78, 452, 41, 50, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 134, 454, 54, 48, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 208, 452, 46, 50, mirrored=mirror)
        im5 = arcade.load_texture(self.chem_sprite, 271, 453, 41, 49, mirrored=mirror)
        im6 = arcade.load_texture(self.chem_sprite, 342, 455, 39, 47, mirrored=mirror)
        im7 = arcade.load_texture(self.chem_sprite, 395, 455, 47, 47, mirrored=mirror)
        im8 = arcade.load_texture(self.chem_sprite, 460, 464, 53, 38, mirrored=mirror)
        im9 = arcade.load_texture(self.chem_sprite, 524, 465, 54, 37, mirrored=mirror)
        im10 = arcade.load_texture(self.chem_sprite, 594, 453, 47, 49, mirrored=mirror)
        im11 = arcade.load_texture(self.chem_sprite, 11, 513, 53, 45, mirrored=mirror)
        im12 = arcade.load_texture(self.chem_sprite, 80, 517, 50, 41, mirrored=mirror)
        im13 = arcade.load_texture(self.chem_sprite, 145, 520, 48, 38, mirrored=mirror)
        im14 = arcade.load_texture(self.chem_sprite, 207, 514, 36, 44, mirrored=mirror)
        return [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12, im13, im14]

    def dash_attack_animation(self, direction) -> [arcade.Texture]:     #attaque coup de pied
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 299, 615, 47, 43, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 361, 608, 41, 50, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 415, 610, 54, 48, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 482, 614, 52, 44, mirrored=mirror)
        im5 = arcade.load_texture(self.chem_sprite, 561, 622, 48, 37, mirrored=mirror)
        return [im1, im2, im3, im4, im5]

    def jump_animation(self, direction) -> [arcade.Texture]:        #saut
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 7, 308, 46, 52, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 63, 311, 46, 51, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 120, 307, 32, 55, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 174, 307, 32, 55, mirrored=mirror)
        im5 = arcade.load_texture(self.chem_sprite, 239, 321, 33, 41, mirrored=mirror)
        return [im1, im2, im3, im4, im5]

    def damaged_animation(self, direction) -> [arcade.Texture]:     #mort
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 20, 1958, 42, 49, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 76, 1965, 32, 42, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 130, 1969, 37, 38, mirrored=mirror)
        im4 = arcade.load_texture(self.chem_sprite, 183, 1984, 55, 25, mirrored=mirror)
        im5 = arcade.load_texture(self.chem_sprite, 250, 1972, 61, 35, mirrored=mirror)
        im6 = arcade.load_texture(self.chem_sprite, 322, 1969, 61, 40, mirrored=mirror)
        im7 = arcade.load_texture(self.chem_sprite, 395, 1972, 62, 38, mirrored=mirror)
        im8 = arcade.load_texture(self.chem_sprite, 474, 1974, 62, 34, mirrored=mirror)
        im9 = arcade.load_texture(self.chem_sprite, 545, 1973, 75, 33, mirrored=mirror)
        im10 = arcade.load_texture(self.chem_sprite, 22, 2038, 74, 22, mirrored=mirror)
        im11 = arcade.load_texture(self.chem_sprite, 105, 2031, 71, 29, mirrored=mirror)
        im12 = arcade.load_texture(self.chem_sprite, 187, 2028, 71, 32, mirrored=mirror)
        im13 = arcade.load_texture(self.chem_sprite, 270, 2027, 51, 31, mirrored=mirror)
        im14 = arcade.load_texture(self.chem_sprite, 333, 2040, 51, 21, mirrored=mirror)
        im15 = arcade.load_texture(self.chem_sprite, 403, 2026, 38, 35, mirrored=mirror)
        return [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12, im13, im14, im15]

    def thraw_animation(self, direction) -> [arcade.Texture]:       #kunai
        mirror = (direction == "left")
        im1 = arcade.load_texture(self.chem_sprite, 18, 864, 34, 49, mirrored=mirror)
        im2 = arcade.load_texture(self.chem_sprite, 72, 868, 46, 45, mirrored=mirror)
        im3 = arcade.load_texture(self.chem_sprite, 143, 870, 54, 43, mirrored=mirror)
        return [im1, im2, im3]

    def get_sprite(self) -> arcade.AnimatedTimeSprite:
        return self.player_list[0]

    def start_x(self, x, change_x):
        anim = self.get_sprite()
        # anim.center_x = x

        if change_x > 0:
            anim.textures = self.start_move_animation("right")
            # anim.textures = self.move_animation("right")
        else:
            anim.textures = self.start_move_animation("left")
            # anim.textures = self.move_animation("left")

    def move_x(self, x, change_x):
        anim = self.get_sprite()
        # anim.center_x = x

        if change_x > 0:
            # anim.textures = self.start_move_animation("right")
            anim.textures = self.move_animation("right")
        else:
            # anim.textures = self.start_move_animation("left")
            anim.textures = self.move_animation("left")

    def jump_y(self, x, y, change_x, change_y):
        anim = self.get_sprite()
        # anim.center_x=x
        # anim.center_y=y
        anim.center_x += change_x
        anim.center_y += change_y
        # self.get_sprite().center_y+=change_y
        # y+=change_y
        if change_x >= 0 and change_y > 0:
            anim.textures = self.jump_animation("right")
        elif change_x <= 0 and change_y > 0:
            anim.textures = self.jump_animation("left")
        elif change_x >= 0 and change_y < 0:
            anim.textures = self.jump_animation("right")
        else:
            anim.textures = self.jump_animation("left")

    def stop_move(self, pressed):
        anim = self.get_sprite()
        if not pressed:
            anim.textures = self.stand_animation("right")
        else:
            anim.textures = self.stand_animation("left")

    def attack_move(self, x, change_x, pressed, PLAYER_SPEED):
        anim = self.get_sprite()
        anim.center_x = x
        if not pressed and (change_x == 0 or (change_x < PLAYER_SPEED)):
            anim.textures = self.attack_animation("right")
        elif not pressed and change_x == PLAYER_SPEED:
            anim.textures = self.dash_attack_animation("right")

        elif pressed and (change_x == 0 or (change_x > -PLAYER_SPEED)):
            anim.textures = self.attack_animation("left")
        elif pressed and change_x == -PLAYER_SPEED:
            anim.textures = self.dash_attack_animation("left")

    def damaged_move(self, pressed):
        anim = self.get_sprite()
        if not pressed:
            anim.textures = self.damaged_animation("right")
        else:
            anim.textures = self.damaged_animation("left")

    def thraw_move(self, x, pressed):
        anim = self.get_sprite()
        if not pressed:
            anim.textures = self.thraw_animation("right")
        else:
            anim.textures = self.thraw_animation("left")

    def draw(self):
        self.player_list.draw()

    def update(self):
        self.get_sprite().center_x += self.change_x
        self.get_sprite().center_y += self.change_y
        # if self.left < 0:
        #     self.left = 0
        # elif self.right > SCREEN_WIDTH - 1:
        #     self.right = SCREEN_WIDTH - 1
        self.player_list.update()
