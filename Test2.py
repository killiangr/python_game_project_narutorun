import arcade
import time
from JoueurNaruto import JoueurNaruto
from Kunai import Kunai

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "NarutoRun"
PLAYER_SPEED = 9
KUNAI_SPEED = 15
SCALE = 1.2
DEFAULT_FRICTION = 0.2
DEFAULT_MASS = 1
PLAYER_1_DEFAULT_POSITION = "right"
PLAYER_2_DEFAULT_POSITION = "left"
ACCELERATION = 1
DECELERATION = 0.6
TILE_SCALING = 1
TILE_X = 32
TILE_Y = 32
GRAVITY = 1.5
DOWN_GRAVITY = 19
PLAYER_JUMP_SPEED = 5
PLAYER_MAX_HEIGHT = 400
PLAYER_MIN_HEIGHT = 228


class MyGame(arcade.Window):
    def __init__(self):         #initialisation
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_sprite = JoueurNaruto(600, 700, PLAYER_1_DEFAULT_POSITION, SCALE, 150, 700, 0.75)
        self.player_sprite_2 = JoueurNaruto(1000, 700, PLAYER_2_DEFAULT_POSITION, SCALE, 1150, 700, 0.75)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.m_pressed = False
        self.l_pressed = False
        self.pressed = False
        self.left_pressed2 = False
        self.right_pressed2 = False
        self.up_pressed2 = False
        self.down_pressed2 = False
        self.g_pressed = False
        self.r_pressed = False
        self.pressed2 = True
        self.isGrounding = False
        self.isGrounding2 = False
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_sprite_2.change_x = 0
        self.player_sprite_2.change_y = 0
        self.collide_delta = 0
        self.collide_delta_2 = 0
        self.jump_delta = 6
        self.jump_delta_2 = 6
        self.isOut = False
        # self.processing_time = 0
        # self.draw_time = 0
        # self.frame_count = 0
        # self.fps_start_timer = None
        # self.fps = None
        self.music = None

    def playMusic(self):        #pour jouer la musique de fond
        self.music = arcade.Sound("assets/backgrounds/Opening 1 Naruto Shippuden.mp3")
        self.music.player.play().loop
        self.music.play()

    def setup(self):        #setup des variables
        # self.player_sprite.setup_sprites()
        self.playMusic()        #on joue la musique
        self.logo = arcade.SpriteList()
        self.fight = arcade.Sprite("assets/backgrounds/Fight.png", 0.70)        #image "fight"
        self.fight.center_x = SCREEN_WIDTH / 2
        self.fight.center_y = SCREEN_HEIGHT / 2
        self.logo.append(self.fight)
        self.background_list = arcade.SpriteList(use_spatial_hash=True)     #
        self.platforme_list = arcade.SpriteList(use_spatial_hash=True)      #
        self.sol_list = arcade.SpriteList(use_spatial_hash=True)            #les différentes listes pour le décors et l'arriere plan
        self.terrain_list = arcade.SpriteList(use_spatial_hash=True)        #
        self.decors_list = arcade.SpriteList(use_spatial_hash=True)         #
        self.kunai_list = arcade.SpriteList()       #kunai joueur1
        self.kunai_list_2 = arcade.SpriteList()     #kunai joueur2

        map_name = "assets/backgrounds/map_naruto.tmx"      #la map avec decors et arriere plan
        my_map = arcade.tilemap.read_tmx(map_name)      #on la lit

        self.background_list = arcade.tilemap.process_layer(my_map, 'Background', TILE_SCALING)
        self.sol_list = arcade.tilemap.process_layer(my_map, 'Sol', TILE_SCALING)
        self.platforme_list = arcade.tilemap.process_layer(my_map, 'Platforme', TILE_SCALING)
        self.terrain_list = arcade.tilemap.process_layer(my_map, 'terrain', TILE_SCALING)
        self.decors_list = arcade.tilemap.process_layer(my_map, 'Décors', TILE_SCALING)

    def on_draw(self):      #pour l'affiche des différents sprites
        # draw_start_time = timeit.default_timer()
        #
        # if self.frame_count % 60 == 0:
        #     if self.fps_start_timer is not None:
        #         total_time = timeit.default_timer() - self.fps_start_timer
        #         self.fps = 60 / total_time
        #     self.fps_start_timer = timeit.default_timer()
        # self.frame_count += 1

        arcade.start_render()
        self.sol_list.draw()            #
        self.background_list.draw()     #
        self.terrain_list.draw()        #pour l'affichage des décors et de l'arriere plan
        self.decors_list.draw()         #
        self.platforme_list.draw()      #
        while self.isOut:
            smoke = arcade.AnimatedTimeBasedSprite("assets/sprites/naruto_sheet.gif", 3, image_x=108, image_y=691,
                                                   image_width=48,
                                                   image_height=57, center_x=640, center_y=750)         #fumer en haut de l'ecran quand le joueur meurt
            smoke.draw()
            self.isOut = False

        # arcade.draw_texture_rectangle(
        #     SCREEN_WIDTH // 2,
        #     SCREEN_HEIGHT // 2,
        #     SCREEN_WIDTH,
        #     SCREEN_HEIGHT,
        #
        #
        #     #self.background
        # )

        self.kunai_list.draw()          #affichage kunai joueur1
        self.kunai_list_2.draw()        #affichage kunai joueur2
        self.player_sprite_2.draw()     #affichage joueur1
        self.player_sprite.draw()       #affichage joueur2
        self.logo.draw()                #affichage "fight"
        # self.player_sprite.kunai.kunai_list.draw()
        # self.player_sprite.kunai.kunai_list.draw()

        # arcade.draw_text(f"X Speed: {self.player_sprite.change_x:6.3f}", 10, 50, arcade.color.BLACK)
        # arcade.draw_text(f"Y Speed: {self.player_sprite.change_y:6.3f}", 10, 70, arcade.color.BLACK)
        # arcade.draw_text(f"Position X: {self.player_sprite.animations.get_sprite().center_x:6.3f}", 200, 50, arcade.color.BLACK)
        # arcade.draw_text(f"Position Y: {self.player_sprite.animations.get_sprite().center_y:6.3f}", 200, 70, arcade.color.BLACK)
        # arcade.draw_text(f"Y Hitbox:{self.hit_list:6.3f}",10,700,arcade.color.BLACK)
        # arcade.draw_text(f"X Speed: {self.player_sprite_2.change_x:6.3f}", 1000, 50, arcade.color.BLACK)
        # arcade.draw_text(f"Y Speed: {self.player_sprite_2.change_y:6.3f}", 1000, 70, arcade.color.BLACK)
        # arcade.draw_text(f"Position X: {self.player_sprite_2.animations.get_sprite().center_x:6.3f}", 1150, 50,arcade.color.BLACK)
        # arcade.draw_text(f"Position Y: {self.player_sprite_2.animations.get_sprite().center_y:6.3f}", 1150, 70,arcade.color.BLACK)
        #
        # if self.fps is not None:
        #     output = f"FPS: {self.fps:.0f}"
        #     arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.BLACK, 10)
        #
        # self.draw_time = timeit.default_timer() - draw_start_time

    def gravity(self, player):      #fonction gravité
        player.change_y -= 1.6      #elle nous fait tomber de tel valeur
        player.animations.get_sprite().center_y += player.change_y      #la position suit la vitesse

    def jump_1(self):       #fonction saut joueur1
        self.jump_delta = 0         #
        self.isGrounding = False       #pas sur le sol
        if self.collide_delta < 6 and self.jump_delta < 6:
            self.jump_delta = 6 * 2
            self.player_sprite.change_y += 20       #on saute à une vitesse de tel valeur
            self.collide_delta += 6         #changer cette valeur si on veut double saut
            self.jump_delta += 6

    def jump_2(self):       #fonction saut joueur2 (meme principe que saut joueur1)
        self.jump_delta_2 = 0
        self.isGrounding2 = False
        if self.collide_delta_2 < 6 and self.jump_delta_2 < 6:
            self.jump_delta_2 = 6 * 2
            self.player_sprite_2.change_y += 20
            self.collide_delta_2 += 6
            self.jump_delta_2 += 6

    def hit(self, pressed, gm_pressed, player_sprite, player_sprite_2):     #fonction qui detecte la frappe
        self.hit_list = arcade.check_for_collision(player_sprite.animations.get_sprite(),       #verifie si collision entre les joueurs
                                                   player_sprite_2.animations.get_sprite())
        if self.hit_list and not pressed and gm_pressed:        #si collision et touche frappe active
            player_sprite_2.animations.get_sprite().center_x += 4       #recul du joueur
            player_sprite_2.health.health -= 1      #perd de la vie
            player_sprite_2.health.health_after_hit()       #rectangle de la vie qui perd de sa largeur
            # if player_sprite_2.health.health <= 0:
            #     player_sprite_2.damaged(pressed2)
        elif self.hit_list and pressed and gm_pressed:      #meme principe
            player_sprite_2.animations.get_sprite().center_x -= 4
            player_sprite_2.health.health -= 1
            player_sprite_2.health.health_after_hit()
            # if player_sprite_2.health.health <= 0:
            #     player_sprite_2.damaged(pressed2)

    def kunai_hit(self, player, kunai_list):        #fonction frappe kunai
        for kunai in kunai_list:
            kunai_hit_list = arcade.check_for_collision_with_list(kunai, player.animations.player_list)     #verifie collision entre le joueur et le kunai
            if len(kunai_hit_list) > 0:     #si il y a un kunai de lancer et que touche le joueur
                kunai.remove_from_sprite_lists()        #supprime le kunai
                player.health.health -= 2       #joueur perd de la vie
                player.health.health_after_hit()        #rectangle de la vie perd de sa largeur
                # if player.health.health <= 0:
                # player.damaged(pressed)

    def plateforme_hit_1(self):     #fonction pour verifier si collision joueur/plateforme
        for platforme in self.platforme_list:
            if arcade.check_for_collision(self.player_sprite.animations.get_sprite(), platforme):       #si collision entre joueur et plateforme
                self.player_sprite.change_y = 0     #vitesse joueur en y = 0
                self.player_sprite.animations.get_sprite().center_y = platforme.top + 16  #position joueur sur le dessus de la plateforme
                self.isGrounding = True     #il est sur la terre
                self.collide_delta = 0      #il peut resauter
                self.jump_delta = 0         #il peut resauter
            else:
                self.isGrounding = False        #sinon il est pas sur terre

        if not self.isGrounding:     #si pas sur terre
            self.gravity(self.player_sprite)        #applique gravité

    def plateforme_hit_2(self):     #meme principe
        for platforme in self.platforme_list:
            if arcade.check_for_collision(self.player_sprite_2.animations.get_sprite(), platforme):
                self.player_sprite_2.change_y = 0
                self.player_sprite_2.animations.get_sprite().center_y = platforme.top + 16
                self.isGrounding2 = True
                self.collide_delta_2 = 0
                self.jump_delta_2 = 0
            else:
                self.isGrounding2 = False

        if not self.isGrounding2:
            self.gravity(self.player_sprite_2)

    def isOutofMap(self, player_sprite, pressed):       #fonction pour le hors zone
        if player_sprite.animations.get_sprite().center_y <= -300:      #si hors zone
            self.isOut = True       #le joueur est dit hors zone
            player_sprite.animations.get_sprite().center_y = 800        #on le replace en haut milieu de l'écran
            player_sprite.animations.get_sprite().center_x = 640
            player_sprite.health.health -= 10       #on le fait perdre un peu de vie
            player_sprite.health.health_after_hit()     #rectangle de la vie qui baisse
            # if player_sprite.health.health <= 0:
            #     player_sprite.damaged(pressed)

    def sol_hit_1(self):        #fonction collision entre joueur et sol
        for sol in self.sol_list:
            if arcade.check_for_collision(self.player_sprite.animations.get_sprite(), sol):     #verifie si collision joueur sol
                self.player_sprite.animations.get_sprite().center_y = sol.top + 16      #position sur le sol
                self.player_sprite.change_y = 0     #vitesse en y=0
                self.collide_delta = 0      #il peut resauter

    def sol_hit_2(self):  #meme principe
        for sol in self.sol_list:
            if arcade.check_for_collision(self.player_sprite_2.animations.get_sprite(), sol):
                self.player_sprite_2.animations.get_sprite().center_y = sol.top + 16
                self.player_sprite_2.change_y = 0
                self.collide_delta_2 = 0

    def deceleration(self, player_sprite, pressed):     #fonction deceleration
        if player_sprite.change_x > DECELERATION:       #si vitesse sup à deceleration et vers la droite
            player_sprite.change_x -= DECELERATION      #on lui fait perdre de la vitesse
        elif player_sprite.change_x < -DECELERATION:        #si vitesse sup à deceleration et vers la gauche
            player_sprite.change_x += DECELERATION      #on lui fait perdre de la vitesse
        elif (player_sprite.health.health > 0):  #si il a tj 1point de vie
            player_sprite.change_x = 0
            player_sprite.stop(pressed)     #il peut stand quand vitesse à 0

    def acceleration(self, left_pressed, right_pressed, player_sprite): #fonction acceleration
        if left_pressed and not right_pressed:      #si joueur deplace vers gauche
            player_sprite.change_x += -ACCELERATION     # on augmente la vitesse
        elif right_pressed and not left_pressed:        #si joueur deplace vers la droite
            player_sprite.change_x += ACCELERATION      #on augmente la vitesse
        if player_sprite.change_x > PLAYER_SPEED and right_pressed:     #si vitesse sup à vitesse max
            player_sprite.change_x = PLAYER_SPEED  #vitesse = vtmax
        elif player_sprite.change_x < -PLAYER_SPEED and left_pressed:  #si vitesse sup à vitesse max
            player_sprite.change_x = -PLAYER_SPEED      #vitesse=vtmax

    def allRounderAnimations_1(self):       #fonction animation joueur 1
        if self.up_pressed and self.player_sprite.health.health > 0:  #animation saut
            self.jump_1()
            self.player_sprite.jump(self.player_sprite.change_x, self.player_sprite.change_y)
        elif self.up_pressed and (self.right_pressed or self.left_pressed) and self.player_sprite.health.health > 0:        #animation saut
            self.jump_1()
            self.player_sprite.jump(self.player_sprite.change_x, self.player_sprite.change_y)
        # elif not self.up_pressed2:
        #     self.jump_delta=6

        if self.m_pressed and self.player_sprite.health.health > 0:  #animation frappe
            self.player_sprite.attack(self.player_sprite.change_x, self.pressed, PLAYER_SPEED)
            # self.player_sprite.change_x=0.2

        if self.l_pressed and not self.m_pressed:       #animation kunai
            self.player_sprite.thraw(self.player_sprite.change_x, self.pressed)

        if self.player_sprite.change_x != 0 and not self.m_pressed and not self.l_pressed and not self.up_pressed and self.player_sprite.health.health > 0:     #animation deplacement
            self.player_sprite.start(self.player_sprite.change_x)       #commencement du deplacement
            if self.player_sprite.change_x == PLAYER_SPEED or self.player_sprite.change_x == -PLAYER_SPEED and self.player_sprite.health.health > 0:
                self.player_sprite.move(self.player_sprite.change_x)        #deplacement vitesse max

    def allRounderAnimations_2(self):  #fonction animations joueur2 meme principe que joeuur1
        if self.up_pressed2 and self.player_sprite_2.health.health > 0:
            self.jump_2()
            self.player_sprite_2.jump(self.player_sprite_2.change_x, self.player_sprite_2.change_y)
        elif self.up_pressed2 and (
                self.right_pressed2 or self.left_pressed2) and self.player_sprite_2.health.health > 0:
            self.jump_2()
            self.player_sprite_2.jump(self.player_sprite_2.change_x, self.player_sprite_2.change_y)
        # elif not self.up_pressed2:
        #     self.jump_delta=6

        if self.g_pressed and self.player_sprite_2.health.health > 0:  # and (self.player_sprite.change_x==PLAYER_SPEED or self.player_sprite.change_x==-PLAYER_SPEED):
            self.player_sprite_2.attack(self.player_sprite_2.change_x, self.pressed2, PLAYER_SPEED)
            # self.player_sprite.change_x=0.2

        if self.r_pressed and not self.g_pressed:
            self.player_sprite_2.thraw(self.player_sprite_2.change_x, self.pressed2)

        if self.player_sprite_2.change_x != 0 and not self.g_pressed and not self.r_pressed and not self.up_pressed2 and self.player_sprite_2.health.health > 0:
            self.player_sprite_2.start(self.player_sprite_2.change_x)
            if self.player_sprite_2.change_x == PLAYER_SPEED or self.player_sprite_2.change_x == -PLAYER_SPEED and self.player_sprite_2.health.health > 0:
                self.player_sprite_2.move(self.player_sprite_2.change_x)

    def on_update(self, delta_time: float):     #fonction qui regarde toute les 0,0016s ce qu'il se passe
        if time.process_time() >= 1.3:
            self.fight.change_x += 5
            self.fight.center_x += self.fight.change_x
            if time.process_time() >= 5:
                self.fight.kill()
        self.hit(self.pressed, self.m_pressed, self.player_sprite, self.player_sprite_2)
        self.hit(self.pressed2, self.g_pressed, self.player_sprite_2, self.player_sprite)
        self.plateforme_hit_1()
        self.plateforme_hit_2()
        self.sol_hit_1()
        self.sol_hit_2()
        self.deceleration(self.player_sprite, self.pressed)
        self.deceleration(self.player_sprite_2, self.pressed2)
        self.acceleration(self.left_pressed, self.right_pressed, self.player_sprite)
        self.acceleration(self.left_pressed2, self.right_pressed2, self.player_sprite_2)
        self.allRounderAnimations_1()
        self.allRounderAnimations_2()
        self.isOutofMap(self.player_sprite, self.pressed)
        self.isOutofMap(self.player_sprite_2, self.pressed2)
        # self.player_sprite.kunai.kunai_list.update()
        # self.player_sprite_2.kunai.kunai_list.update()
        self.kunai_list.update()
        self.kunai_list_2.update()
        self.logo.update()
        self.kunai_hit(self.player_sprite_2, self.kunai_list)
        self.kunai_hit(self.player_sprite, self.kunai_list_2)

        if self.player_sprite_2.health.health <= 0:     #si vie<0
            self.player_sprite_2.damaged(self.pressed2)     #animation mort
            self.player_sprite_2.animations.get_sprite().center_y = 800     #joueur reapparait du haut de l'ecran
            self.player_sprite_2.animations.get_sprite().center_x = 640
            # self.player_sprite_2.health.health=100

        if self.player_sprite.health.health <= 0:       #si vie<0
            self.player_sprite.damaged(self.pressed)        #animation mort
            self.player_sprite.animations.get_sprite().center_y = 800   #joueur reapparait du haut de l'ecran
            self.player_sprite.animations.get_sprite().center_x = 640
            # self.player_sprite.health.health=100

        # if self.player_sprite.animations.get_sprite().center_y <= PLAYER_MIN_HEIGHT:
        #     self.player_sprite.animations.get_sprite().center_y = PLAYER_MIN_HEIGHT
        #     # self.isGrounding=True
        #     self.player_sprite.change_y = 0
        #     self.collide_delta= 0

        # if self.player_sprite_2.animations.get_sprite().center_y <= PLAYER_MIN_HEIGHT:
        #     self.player_sprite_2.animations.get_sprite().center_y = PLAYER_MIN_HEIGHT
        #     # self.isGrounding=True
        #     self.player_sprite_2.change_y = 0
        #     self.collide_delta_2 = 0
        self.player_sprite.animations.player_list.update_animation()
        self.player_sprite_2.animations.player_list.update_animation()
        # self.player_sprite_2.health.healthbar.update_animation()
        # self.platforme_list.update()

    def on_key_press(self, key: int, modifiers: int):       #fonction qui detecte si une touche est presse
        if key == arcade.key.UP:
            self.up_pressed = True
        if key == arcade.key.Z:
            self.up_pressed2 = True
            # self.jump_delta=0
        if key == arcade.key.DOWN:
            self.down_pressed = True
        if key == arcade.key.S:
            self.down_pressed2 = True
        if key == arcade.key.LEFT:
            self.left_pressed = True
            self.pressed = True
        if key == arcade.key.Q:
            self.left_pressed2 = True
            self.pressed2 = True
        if key == arcade.key.RIGHT:
            self.right_pressed = True
            self.pressed = False
        if key == arcade.key.D:
            self.right_pressed2 = True
            self.pressed2 = False
        if key == arcade.key.M:
            self.m_pressed = True
            self.music = arcade.Sound("assets/backgrounds/Woosh.mp3")
            self.music.play()
        if key == arcade.key.G:
            self.g_pressed = True
            self.music = arcade.Sound("assets/backgrounds/Woosh.mp3")
            self.music.play()
        if key == arcade.key.L and not self.l_pressed:
            if self.player_sprite.kunai.nb_kunai > 0:
                self.l_pressed = True
                Kunai.on_key_press(self, self.player_sprite.animations.get_sprite().center_x,
                                   self.player_sprite.animations.get_sprite().center_y,
                                   self.player_sprite_2.animations.get_sprite().center_x,
                                   self.player_sprite_2.animations.get_sprite().center_y, 1, KUNAI_SPEED,
                                   self.kunai_list)
                self.player_sprite.kunai.nb_kunai -= 1
        if key == arcade.key.R and not self.r_pressed:
            if self.player_sprite_2.kunai.nb_kunai > 0:
                self.r_pressed = True
                Kunai.on_key_press(self, self.player_sprite_2.animations.get_sprite().center_x,
                                   self.player_sprite_2.animations.get_sprite().center_y,
                                   self.player_sprite.animations.get_sprite().center_x,
                                   self.player_sprite.animations.get_sprite().center_y, 1, KUNAI_SPEED,
                                   self.kunai_list_2)
                self.player_sprite_2.kunai.nb_kunai -= 1

    def on_key_release(self, key: int, modifiers: int):     #fonction qui detecte si une touche est relache
        if key == arcade.key.UP:
            self.up_pressed = False
        if key == arcade.key.Z:
            self.up_pressed2 = False
        if key == arcade.key.DOWN:
            self.down_pressed = False
        if key == arcade.key.S:
            self.down_pressed2 = False
        if key == arcade.key.LEFT:
            self.left_pressed = False
        if key == arcade.key.Q:
            self.left_pressed2 = False
        if key == arcade.key.RIGHT:
            self.right_pressed = False
        if key == arcade.key.D:
            self.right_pressed2 = False
        if key == arcade.key.M:
            self.m_pressed = False
        if key == arcade.key.G:
            self.g_pressed = False
        if key == arcade.key.L:
            self.l_pressed = False
        if key == arcade.key.R:
            self.r_pressed = False


if __name__ == "__main__":
    window = MyGame()
    window.setup()
    arcade.run()
