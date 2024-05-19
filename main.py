# /// script
# dependencies = [
#  "pygame-ce",
#  "cffi",
#  "pymunk",
# ]
# ///


import pymunk
import pymunk.pygame_util
import pygame
import asyncio
import cffi




async def main():

    space = pymunk.Space()
    space.gravity = 0, 200
    pygame.init()
    groundBody = pymunk.Body(100, 1, pymunk.Body.STATIC)
    groundShape = pymunk.Poly(groundBody,[(0,0), (800,0), (800,200), (0,200)] )
    groundShape.friction = 1
    groundShape.elasticity = 0.5
    groundBody.position = (0,500)
    space.add(groundBody, groundShape)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hello World")
    clock = pygame.time.Clock()
    #draw a redct
    cooldown = 0
    dos = pymunk.pygame_util.DrawOptions(screen)
    while True:
        await asyncio.sleep(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        mx,my = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and cooldown < 0:
            print(mx,my)
            body = pymunk.Body(100, 1, pymunk.Body.DYNAMIC)
            body.position = (mx,my)
            shape = pymunk.Circle(body, 20)
            shape.elasticity = 0.9
            space.add(body, shape)
            cooldown = 15
            
        screen.fill((255, 255, 255))
        space.debug_draw(dos)
        pygame.display.update()
        cooldown -= 1
        clock.tick(60)
        space.step(1/60)


asyncio.run(main())