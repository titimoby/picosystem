# Bounce example
This contains the example from [Learn Adafruit portal](https://learn.adafruit.com/circuitpython-stage-game-library)

I had to adapt the original code.

First, I needed to extend the grid used, from 10 by 8 on Pybadge/Pygamer to 16 by 16 for the Picosystem

```
background = stage.Grid(bank, 16, 16)
```

As the screen is here 240 by 240, I had to modify the x and y limiter to trigger the bounce. The new value is 240 (screen) - 16 (ball sprite) => 224

```
if not 0 < self.x < 224:
    self.dx = -self.dx
if not 0 < self.y < 224:
    self.dy = -self.dy```