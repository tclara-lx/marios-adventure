def on_up_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 2 2 f f f f . . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f f 2 f e f . . . 
                        . f f f 2 f e e 2 2 f f f . . . 
                        . f e 2 f f e e 2 f e e f . . . 
                        f f e f f e e e f e e e f f . . 
                        f f e e e e e e e e e e f d f . 
                        . . f e e e e e e e e f f b f . 
                        . . e f f f f f f f f 4 f b f . 
                        . . 4 f 2 2 2 2 2 e d d f c f . 
                        . . e f f f f f f e e 4 f f . . 
                        . . . f f f . . . . . . . . . .
            """),
            img("""
                . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . f f f f f 2 2 f f f f f . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e 2 f 2 f f 2 f 2 e f . . . 
                        . f f f 2 2 e e 2 2 f f f . . . 
                        f f e f 2 f e e f 2 f e f f . . 
                        f e e f f e e e e f e e e f . . 
                        . f e e e e e e e e e e f . . . 
                        . . f e e e e e e e e f . . . . 
                        . e 4 f f f f f f f f 4 e . . . 
                        . 4 d f 2 2 2 2 2 2 f d 4 . . . 
                        . 4 4 f 4 4 4 4 4 4 f 4 4 . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . f f . . f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f . . . . . . . 
                        . . . f f e e e e f f . . . . . 
                        . . f e e e f f e e e f . . . . 
                        . . f f f f 2 2 f f f f . . . . 
                        . f f e 2 e 2 2 e 2 e f f . . . 
                        . f e f 2 f f f 2 f 2 e f . . . 
                        . f f f 2 2 e e f 2 f f f . . . 
                        . f e e f 2 e e f f 2 e f . . . 
                        . f e e e f e e e f f e f f . . 
                        . f e e e e e e e e e e f f . . 
                        . f f e e e e e e e e f . . . . 
                        . f 4 f f f f f f f f e . . . . 
                        . f d d e 2 2 2 2 2 f 4 . . . . 
                        . f 4 e e f f f f f f e . . . . 
                        . . . . . . . . f f f . . . . .
            """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
    mySprite.start_effect(effects.bubbles, 500)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    mySprite.start_effect(effects.ashes, 500)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . f f e d d f 1 4 d 4 e e f . 
                        . f d d f d d d d 4 e e e f . . 
                        . f b b f e e e 4 e e f . . . . 
                        . f b b e d d 4 2 2 2 f . . . . 
                        . . f b e d d e 4 4 4 f f . . . 
                        . . . f f e e f f f f f f . . . 
                        . . . . f f f . . . f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . . f e d d f 1 4 d 4 e e f . 
                        . . . . f d d d e e e e e f . . 
                        . . . . f e 4 e d d 4 f . . . . 
                        . . . . f 2 2 e d d e f . . . . 
                        . . . f f 5 5 f e e f f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f f . . . f f . . . .
            """),
            img("""
                . . . . . f f f f f f . . . . . 
                        . . . . f 2 f e e e e f f . . . 
                        . . . f 2 2 2 f e e e e f f . . 
                        . . . f e e e e f f e e e f . . 
                        . . f e 2 2 2 2 e e f f f f . . 
                        . . f 2 e f f f f 2 2 2 e f . . 
                        . . f f f e e e f f f f f f f . 
                        . . f e e 4 4 f b e 4 4 e f f . 
                        . . f f e d d f 1 4 d 4 e e f . 
                        . f d d f d d d d 4 e e e f . . 
                        . f b b f e e e 4 e e f f . . . 
                        . f b b e d d 4 2 2 2 f . . . . 
                        . . f b e d d e 2 2 2 e . . . . 
                        . . . f f e e f 4 4 4 f . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f . . . 
                        . . f e e e e e d d d f . . . . 
                        . . . . f 4 d d e 4 e f . . . . 
                        . . . . f e d d e 2 2 f . . . . 
                        . . . f f f e e f 5 5 f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f . . . f f f . . . .
            """),
            img("""
                . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f f . . 
                        . . f e e e 4 d d d d f d d f . 
                        . . . f f e e 4 e e e f b b f . 
                        . . . . f 2 2 2 4 d d e b b f . 
                        . . . . e 2 2 2 e d d e b f . . 
                        . . . . f 4 4 4 f e e f f . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f . . . 
                        . . f e e e e e d d d f . . . . 
                        . . . . f 4 d d e 4 e f . . . . 
                        . . . . f e d d e 2 2 f . . . . 
                        . . . f f f e e f 5 5 f f . . . 
                        . . . f f f f f f f f f f . . . 
                        . . . . f f . . . f f f . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . f f f f f f . . . . . 
                        . . . f f e e e e f 2 f . . . . 
                        . . f f e e e e f 2 2 2 f . . . 
                        . . f e e e f f e e e e f . . . 
                        . . f f f f e e 2 2 2 2 e f . . 
                        . . f e 2 2 2 f f f f e 2 f . . 
                        . f f f f f f f e e e f f f . . 
                        . f f e 4 4 e b f 4 4 e e f . . 
                        . f e e 4 d 4 1 f d d e f f . . 
                        . . f e e e 4 d d d d f d d f . 
                        . . . . f e e 4 e e e f b b f . 
                        . . . . f 2 2 2 4 d d e b b f . 
                        . . . f f 4 4 4 e d d e b f . . 
                        . . . f f f f f f e e f f . . . 
                        . . . . f f . . . f f f . . . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . . f e 4 d d d d 4 e f e . . 
                        . . f e f 2 2 2 2 e d d 4 e . . 
                        . . e 4 f 2 2 2 2 e d d e . . . 
                        . . . . f 4 4 5 5 f e e . . . . 
                        . . . . f f f f f f f . . . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite)
    info.change_score_by(1)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_on_overlap)

Coins: Sprite = None
mySprite: Sprite = None
scene.set_background_color(6)
tiles.set_current_tilemap(tilemap("""
    level1
"""))
info.set_score(0)
mySprite = sprites.create(img("""
        . . . . . . f f f f . . . . . . 
            . . . . f f f 2 2 f f f . . . . 
            . . . f f f 2 2 2 2 f f f . . . 
            . . f f f e e e e e e f f f . . 
            . . f f e 2 2 2 2 2 2 e e f . . 
            . . f e 2 f f f f f f 2 e f . . 
            . . f f f f e e e e f f f f . . 
            . f f e f b f 4 4 f b f e f f . 
            . f e e 4 1 f d d f 1 4 e e f . 
            . . f e e d d d d d d e e f . . 
            . . . f e e 4 4 4 4 e e f . . . 
            . . e 4 f 2 2 2 2 2 2 f 4 e . . 
            . . 4 d f 2 2 2 2 2 2 f d 4 . . 
            . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
mySprite.set_bounce_on_wall(True)
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile1
""")):
    Coins = sprites.create(img("""
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
                    6 6 6 6 6 6 f f f f f 6 6 6 6 6 
                    6 6 6 6 f f 5 5 5 5 5 f f 6 6 6 
                    6 6 6 f 5 5 5 5 5 5 5 5 5 f 6 6 
                    6 6 6 f 5 5 5 4 4 4 5 5 5 f 6 6 
                    6 6 f 5 5 5 4 4 5 5 5 5 5 5 f 6 
                    6 6 f 5 5 4 5 5 5 5 5 5 5 5 f 6 
                    6 6 f 5 5 4 5 5 5 5 5 5 5 5 f 6 
                    6 6 f 5 5 4 5 5 5 5 5 4 5 5 f 6 
                    6 6 f 5 5 5 5 5 5 5 4 4 5 5 f 6 
                    6 6 6 f 5 5 5 5 5 4 4 5 5 f 6 6 
                    6 6 6 f 5 5 5 5 5 5 5 5 5 f 6 6 
                    6 6 6 6 f f 5 5 5 5 5 f f 6 6 6 
                    6 6 6 6 6 6 f f f f f 6 6 6 6 6 
                    6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
        """),
        SpriteKind.player)
    tiles.place_on_tile(Coins, value)
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))

def on_forever():
    for index in range(4):
        music.play(music.string_playable("C - C E F G B C5 ", 300),
            music.PlaybackMode.UNTIL_DONE)
    for index2 in range(2):
        music.play(music.string_playable("B A G C5 - C5 - C5 ", 300),
            music.PlaybackMode.UNTIL_DONE)
forever(on_forever)
