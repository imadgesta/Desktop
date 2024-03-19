import pygame, random
from superwires import games, color

def main():
    games.init(screen_width = 1280, screen_height = 720, fps = 60)
    games.screen.background = games.load_image("back.jpg", transparent = False)
    games.screen.mainloop()

main()


