import pygame
pygame.init()

# Definindo as variáveis iniciais
x = 96
y = 96
velocidade = 64

# Tamanho do bloco (tile)
bloco = 64

# Definindo o tamanho da janela
janela = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Jogo da cobrinha")
maca = pygame.image.load('images/apple.jpg')
# Definindo as cores dos tiles
tile_parede = pygame.Surface((bloco, bloco))
tile_parede.fill((89, 138, 51))

tile_verde_claro = pygame.Surface((bloco, bloco))
tile_verde_claro.fill((170, 215, 81))

tile_verde_escuro = pygame.Surface((bloco, bloco))
tile_verde_escuro.fill((157, 203, 69))

# Mapa do jogo (matriz de valores)
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1],
    [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1],
    [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1],
    [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1],
    [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1],
    [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1],
    [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1],
    [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1],
    [1, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 1],
    [1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
posicao_maca_x = [64,128,192,256,320,384,448,512,576,640,704,768,832,896]
posicao_maca_y = [64,128,192,256,320,384,448,512,576,640]
# Função para desenhar o mapa na janela
def desenha_mapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):  # Corrigido o loop interno para percorrer as colunas corretamente
            if mapa[i][j] == 1:
                janela.blit(tile_parede, (j * bloco, i * bloco))
            elif mapa[i][j] == 2:
                janela.blit(tile_verde_claro, (j * bloco, i * bloco))
            elif mapa[i][j] == 3:
                janela.blit(tile_verde_escuro, (j * bloco, i * bloco))

# Loop principal do jogo
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Controle de movimento do personagem
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        if y != 96:
            y -= velocidade
    if comandos[pygame.K_DOWN]:
        if y != 672:
            y += velocidade
    if comandos[pygame.K_RIGHT]:
        if x != 928:
            x += velocidade
    if comandos[pygame.K_LEFT]:
        if x != 96:
            x -= velocidade

    # Preencher o fundo da janela com uma cor (fundo preto)
    janela.fill((0, 0, 0))

    # Desenhar o mapa
    desenha_mapa()

    # Desenhar o "personagem" (vamos usar um círculo para o personagem por enquanto)
    pygame.draw.circle(janela, (255, 0, 0), (x, y), 16)  # Personagem (círculo vermelho)

    # Atualiza a tela
    pygame.display.update()

# Fechar o Pygame
pygame.quit()
