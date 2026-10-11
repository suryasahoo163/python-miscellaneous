import pygame
import pygame.camera

pygame.init()

gameDisplay = pygame.display.set_mode((1280,720), pygame.RESIZABLE)

pygame.camera.init()
cam = pygame.camera.Camera(0,(1280,720))
cam.start()
while True:
    img = cam.get_image()
    gameDisplay.blit(img,(0,0))
    pygame.display.update()
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            cam.stop()
            pygame.quit()
            exit()
