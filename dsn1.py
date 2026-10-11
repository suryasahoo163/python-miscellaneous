import pygame


pygame.init()
aa=10
bb=80
c=(0,0,0)
fps=1000
clock=pygame.time.Clock()
color=(0,255,0)
screen=pygame.display.set_mode((300,1200))
mouse=pygame.mouse.get_pos()
x=10
ab=10
y=10
xc=5
yc=7
cu= pygame.image.load("images.png")
ci=pygame.transform.scale(cu,(100,100))
iu=pygame.transform.scale(cu,(800,1500))
screen.fill(color)
ct=pygame.transform.scale(ci,(200,40))
while True:
	
	for event in pygame.event.get():
		if event.type==quit:
			pygame.quit()
	screen.blit(ct,(aa,bb))
	if aa>550:
		ab=-5
	if aa<10:
		ab=5
	aa+=ab

	if x>610:
		xc=-5
	if y>1340:
		yc=-7
	if x<10:
		xc=5
	if y<10:
		yc=7
	x+=xc
	y+=yc
	
	fps+=50
	clock.tick(fps)
	pygame.display.update()
	pygame.display.flip()
	screen.blit(ci,(x,y))
