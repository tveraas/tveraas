import pygame
import random
pygame.init()

# Definindo as variáveis iniciais
x = 96
y = 96
velocidade = 64
direcao = "PARADO"
# Tamanho do bloco (tile)
bloco = 64

# Definindo o tamanho da janela
janela = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Jogo da cobrinha")
maca = pygame.image.load('images/apple.png')
maca = pygame.transform.scale(maca, (64,64))

# Definindo as cores dos tiles
tile_parede = pygame.Surface((bloco, bloco))
tile_parede.fill((89, 138, 51))

tile_verde_claro = pygame.Surface((bloco, bloco))
tile_verde_claro.fill((170, 215, 81))

tile_verde_escuro = pygame.Surface((bloco, bloco))
tile_verde_escuro.fill((157, 203, 69))

def posicao_random(posicao_x:list,posicao_y:list):
    posicao_maca_x = random.choice(posicao_x)
    posicao_maca_y = random.choice(posicao_y)
    return posicao_maca_x,posicao_maca_y

def jogador_pega_maca(x, y, maca_x, maca_y):
    if x == maca_x and y == maca_y:
        return True
    return False

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
lista_maca_x = [64,128,192,256,320,384,448,512,576,640,704,768,832,896]
lista_maca_y = [64,128,192,256,320,384,448,512,576,640]

contador_pontos = 0
contador_tamanho = 0
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
posicao_maca_x,posicao_maca_y = posicao_random(lista_maca_x,lista_maca_y)
# Loop principal do jogo
janela_aberta = True
while janela_aberta:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direcao != 'BAIXO':
                direcao = 'CIMA'
            elif event.key == pygame.K_DOWN and direcao != 'CIMA':
                direcao = 'BAIXO'
            elif event.key == pygame.K_LEFT and direcao != 'DIREITA':
                direcao = 'ESQUERDA'
            elif event.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                direcao = 'DIREITA'
    if direcao == 'CIMA':
        if y > 96:  # Limite superior
            y -= velocidade
        else:
            direcao = 'PARADO'  # Para ao bater na borda superior
    elif direcao == 'BAIXO':
        if y < 672:  # Limite inferior
            y += velocidade
        else:
            direcao = 'PARADO'  # Para ao bater na borda inferior
    elif direcao == 'ESQUERDA':
        if x > 96:  # Limite esquerdo
            x -= velocidade
        else:
            direcao = 'PARADO'  # Para ao bater na borda esquerda
    elif direcao == 'DIREITA':
        if x < 928:  # Limite direito
            x += velocidade
        else:
            direcao = 'PARADO'  # Para ao bater na borda direita
    # Preencher o fundo da janela com uma cor (fundo preto)
    janela.fill((0, 0, 0))

    # Desenhar o mapa
    desenha_mapa()
    janela.blit(maca,(posicao_maca_x,posicao_maca_y))
    if jogador_pega_maca(x-32,y-32,posicao_maca_x,posicao_maca_y):
        posicao_maca_x,posicao_maca_y = posicao_random(lista_maca_x,lista_maca_y)
        contador_pontos += 1
    # Desenhar o "personagem" (vamos usar um círculo para o personagem por enquanto)
    pygame.draw.circle(janela, (255, 0, 0), (x, y), 16)
    
    for i in range(contador_pontos):
        offset = (i + 1)  # Distância entre segmentos
        pygame.draw.circle(janela, (255, 0, 0), (x + offset, y + offset), 16)
    # Atualiza a tela
    pygame.display.update()

# Fechar o Pygame
pygame.quit()