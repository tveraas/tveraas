import pygame
import random
pygame.init()

# Definindo as variáveis iniciais
x = 64
y = 64
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

def jogador_pega_maca(maca_x, maca_y,corpo_cobra):
    for segmento in corpo_cobra:
        if segmento == (maca_x, maca_y):  # Se a maçã está na mesma posição de um segmento
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
corpo_cobra = [(x, y)]
while janela_aberta:
    pygame.time.delay(150)

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
            direcao = 'PARADO'
            x, y = 64, 64  # Reseta a posição inicial
            corpo_cobra = [(x, y)]  # Reseta o corpo da cobra
            contador_pontos = 0  # Para ao bater na borda superior
    elif direcao == 'BAIXO':
        if y < 608:  # Limite inferior
            y += velocidade
        else:
            direcao = 'PARADO'
            x, y = 64, 64  # Reseta a posição inicial
            corpo_cobra = [(x, y)]  # Reseta o corpo da cobra
            contador_pontos = 0  # Para ao bater na borda inferior
    elif direcao == 'ESQUERDA':
        if x > 96:  # Limite esquerdo
            x -= velocidade
        else:
            direcao = 'PARADO'
            x, y = 64, 64  # Reseta a posição inicial
            corpo_cobra = [(x, y)]  # Reseta o corpo da cobra
            contador_pontos = 0  # Para ao bater na borda esquerda
    elif direcao == 'DIREITA':
        if x < 864:  # Limite direito
            x += velocidade
        else:
            direcao = 'PARADO'
            x, y = 64, 64  # Reseta a posição inicial
            corpo_cobra = [(x, y)]  # Reseta o corpo da cobra
            contador_pontos = 0  # Para ao bater na borda direita
    # Preencher o fundo da janela com uma cor (fundo preto)
    janela.fill((0, 0, 0))
    if corpo_cobra[0] in corpo_cobra[1:]:
        # Se a cabeça colidir com qualquer outro segmento, reinicia a fase
        x, y = 64, 64  # Reseta a posição inicial
        corpo_cobra = [(x, y)]  # Reseta o corpo da cobra
        contador_pontos = 0  # Reseta o contador de pontos
        continue
    # Desenhar o mapa
    desenha_mapa()
    janela.blit(maca,(posicao_maca_x,posicao_maca_y))
    if jogador_pega_maca(posicao_maca_x,posicao_maca_y,corpo_cobra):
        posicao_maca_x,posicao_maca_y = posicao_random(lista_maca_x,lista_maca_y)
        contador_pontos += 1
        corpo_cobra.append(corpo_cobra[-1]) 
    # Desenhar o "personagem" (vamos usar um círculo para o personagem por enquanto)
    # Inicialização do corpo da cobra com a cabeça na posição inicial
      # Lista que armazena as posições dos segmentos da cobra

    # Verificação de colisão com a maçã
    
    # Insere a nova posição da cabeça no início da lista do corpo da cobra
    corpo_cobra.insert(0, (x, y))
    

    # Remove o último segmento da cobra apenas se o comprimento atual for menor que o contador de pontos
    if len(corpo_cobra) > contador_pontos:
        corpo_cobra.pop()  # Remove o último segmento para simular o movimento

    # Desenha cada segmento da cobra na tela
    for segmento in corpo_cobra:
        pygame.draw.rect(janela, (255, 0, 0), (segmento[0], segmento[1], bloco, bloco))

    # Atualiza a tela
    pygame.display.update()

# Fechar o Pygame
pygame.quit()