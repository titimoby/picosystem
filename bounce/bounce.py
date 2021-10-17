import ugame
import stage


class Ball(stage.Sprite):
    def __init__(self, x, y):
        super().__init__(bank, 1, x, y)
        self.dx = 2
        self.dy = 1

    def update(self):
        super().update()
        self.set_frame(self.frame % 4 + 1)
        self.move(self.x + self.dx, self.y + self.dy)
        if not 0 < self.x < 224:
            self.dx = -self.dx
        if not 0 < self.y < 224:
            self.dy = -self.dy


bank = stage.Bank.from_bmp16("ball.bmp")
background = stage.Grid(bank, 16, 16)
text = stage.Text(10, 1)
text.move(40, 100)
text.text("Hello world!")
ball1 = Ball(128, 0)
ball2 = Ball(0, 200)
ball3 = Ball(160, 160)
game = stage.Stage(ugame.display, 12)
sprites = [ball1, ball2, ball3]
game.layers = [text, ball1, ball2, ball3, background]
game.render_block()

while True:
    for sprite in sprites:
        sprite.update()
    game.render_sprites(sprites)
    game.tick()
