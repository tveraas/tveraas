import pygame
import random

pygame.init()

# Variáveis iniciais
x = 64
y = 64
velocidade = 64
direcao = "PARADO"
bloco = 64

# Definindo a janela do jogo
janela = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("Jogo da cobrinha")
maca = pygame.image.load('images/apple.png')
maca = pygame.transform.scale(maca, (64, 64))

# Cores dos tiles
tile_parede = pygame.Surface((bloco, bloco))
tile_parede.fill((89, 138, 51))

tile_verde_claro = pygame.Surface((bloco, bloco))
tile_verde_claro.fill((170, 215, 81))

tile_verde_escuro = pygame.Surface((bloco, bloco))
tile_verde_escuro.fill((157, 203, 69))

# Carregar os sprites da cobra
# Cabeça da cobra
cabeça_cima = pygame.image.load('images/head_up.png')
cabeça_cima = pygame.transform.scale(cabeça_cima, (64, 64))

cabeça_baixo = pygame.image.load('images/head_down.png')
cabeça_baixo = pygame.transform.scale(cabeça_baixo, (64, 64))

cabeça_direita = pygame.image.load('images/head_right.png')
cabeça_direita = pygame.transform.scale(cabeça_direita, (64, 64))

cabeça_esquerda = pygame.image.load('images/head_left.png')
cabeça_esquerda = pygame.transform.scale(cabeça_esquerda, (64, 64))

# Corpo da cobra
corpo_horizontal = pygame.image.load('images/body_horizontal.png')
corpo_horizontal = pygame.transform.scale(corpo_horizontal, (64, 32))

corpo_vertical = pygame.image.load('images/body_vertical.png')
corpo_vertical = pygame.transform.scale(corpo_vertical, (32, 64))

# Cauda da cobra
cauda_cima = pygame.image.load('images/tail_down.png')
cauda_cima = pygame.transform.scale(cauda_cima, (32, 64))

cauda_baixo = pygame.image.load('images/tail_up.png')
cauda_baixo = pygame.transform.scale(cauda_baixo, (32, 64))

cauda_direita = pygame.image.load('images/tail_left.png')
cauda_direita = pygame.transform.scale(cauda_direita, (64, 32))

cauda_esquerda = pygame.image.load('images/tail_right.png')
cauda_esquerda = pygame.transform.scale(cauda_esquerda, (64, 32))


# Função para definir posição aleatória da maçã
def posicao_random(posicao_x: list, posicao_y: list):
    posicao_maca_x = random.choice(posicao_x)
    posicao_maca_y = random.choice(posicao_y)
    return posicao_maca_x, posicao_maca_y

# Função para verificar se o jogador pegou a maçã
def jogador_pega_maca(maca_x, maca_y, corpo_cobra):
    for segmento in corpo_cobra:
        if segmento == (maca_x, maca_y):
            return True
    return False

# Mapa do jogo
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

# Função para desenhar o mapa
def desenha_mapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 1:
                janela.blit(tile_parede, (j * bloco, i * bloco))
            elif mapa[i][j] == 2:
                janela.blit(tile_verde_claro, (j * bloco, i * bloco))
            elif mapa[i][j] == 3:
                janela.blit(tile_verde_escuro, (j * bloco, i * bloco))

# Função para desenhar a cobra com sprites específicos
def desenha_cobra(corpo_cobra, direcao):
    for i, (segmento_x, segmento_y) in enumerate(corpo_cobra):
        if i == 0:  # Cabeça
            if direcao == 'CIMA':
                janela.blit(cabeça_cima, (segmento_x, segmento_y))
            elif direcao == 'BAIXO':
                janela.blit(cabeça_baixo, (segmento_x, segmento_y))
            elif direcao == 'DIREITA':
                janela.blit(cabeça_direita, (segmento_x, segmento_y))
            elif direcao == 'ESQUERDA':
                janela.blit(cabeça_esquerda, (segmento_x, segmento_y))
        elif i == len(corpo_cobra) - 1:  # Cauda
            cauda_img = (
                cauda_cima if corpo_cobra[-2][1] > segmento_y else
                cauda_baixo if corpo_cobra[-2][1] < segmento_y else
                cauda_direita if corpo_cobra[-2][0] < segmento_x else
                cauda_esquerda
            )
            if cauda_img == cauda_cima:
                janela.blit(cauda_img, (segmento_x+16, segmento_y))
            if cauda_img == cauda_baixo:
                janela.blit(cauda_img, (segmento_x+16, segmento_y))
            if cauda_img == cauda_direita:
                janela.blit(cauda_img, (segmento_x, segmento_y+16))
            if cauda_img == cauda_esquerda:
                janela.blit(cauda_img, (segmento_x, segmento_y+16))
            
        else:  # Corpo
            if corpo_cobra[i - 1][0] == segmento_x and corpo_cobra[i + 1][0] == segmento_x:
                janela.blit(corpo_vertical, (segmento_x, segmento_y))
            else:
                janela.blit(corpo_horizontal, (segmento_x, segmento_y))

# Posicionar a maçã
lista_maca_x = [64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768, 832, 896]
lista_maca_y = [64, 128, 192, 256, 320, 384, 448, 512, 576, 640]
posicao_maca_x, posicao_maca_y = posicao_random(lista_maca_x, lista_maca_y)

# Loop principal do jogo
janela_aberta = True
corpo_cobra = [(x, y)]
contador_pontos = 0

while janela_aberta:
    pygame.time.delay(150)

    # Eventos do teclado
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

    # Atualizar a posição da cabeça somente se a direção for diferente de "PARADO"
    if direcao != "PARADO":
        if direcao == 'CIMA':
            novo_segmento = (corpo_cobra[0][0], corpo_cobra[0][1] - velocidade)
        elif direcao == 'BAIXO':
            novo_segmento = (corpo_cobra[0][0], corpo_cobra[0][1] + velocidade)
        elif direcao == 'ESQUERDA':
            novo_segmento = (corpo_cobra[0][0] - velocidade, corpo_cobra[0][1])
        elif direcao == 'DIREITA':
            novo_segmento = (corpo_cobra[0][0] + velocidade, corpo_cobra[0][1])

        # Insere o novo segmento da cabeça
        corpo_cobra.insert(0, novo_segmento)

        # Checa se pegou a maçã
        if jogador_pega_maca(posicao_maca_x, posicao_maca_y, corpo_cobra):
            posicao_maca_x, posicao_maca_y = posicao_random(lista_maca_x, lista_maca_y)
            contador_pontos += 1
        else:
            corpo_cobra.pop()  # Remove o último segmento para simular o movimento

    # Desenha o mapa e a cobra
    janela.fill((0, 0, 0))
    desenha_mapa()
    janela.blit(maca, (posicao_maca_x, posicao_maca_y))
    desenha_cobra(corpo_cobra, direcao)
    pygame.display.update()


pygame.quit()