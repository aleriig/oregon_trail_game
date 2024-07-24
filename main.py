from oregon_trail_game import WIDTH, HEIGHT
from oregon_trail_game.game import Oregon

if __name__ == "__main__":
    print(f"The size screen is {WIDTH}x{HEIGHT}")
    game = Oregon()
    game.start()