import pygame
pygame.init()
x = 512
y = 384
velocidade = 5

janela = pygame.display.set_mode((1024,768))
pygame.display.set_caption("Jogo da cobrinha")

janela_aberta = True
while janela_aberta == True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    janela.fill((0,0,0))
    pygame.draw.circle(janela,(150,150,0), (x,y),40)
    pygame.display.update()
    
pygame.quit()