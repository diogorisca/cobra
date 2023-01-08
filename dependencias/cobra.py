import pygame, random
from sys import exit
from pygame.math import Vector2

class COBRA:
    def __init__(self):
        y = (altura/corpo_cobra)/2
        self.corpo = [Vector2(5, y), Vector2(4, y), Vector2(3, y)]
        self.direcao = Vector2(1, 0)
        self.novo_corpo = False
        self.tempo = 80

        self.cabeca_cima = pygame.image.load('dependencias/imagens/cabeca_cima.png').convert_alpha()
        self.cabeca_baixo = pygame.image.load('dependencias/imagens/cabeca_baixo.png').convert_alpha()
        self.cabeca_esquerda = pygame.image.load('dependencias/imagens/cabeca_esquerdo.png').convert_alpha()
        self.cabeca_direita = pygame.image.load('dependencias/imagens/cabeca_direito.png').convert_alpha()

        self.cauda_cima = pygame.image.load('dependencias/imagens/cauda_cima.png').convert_alpha()
        self.cauda_baixo = pygame.image.load('dependencias/imagens/cauda_baixo.png').convert_alpha()
        self.cauda_esquerda = pygame.image.load('dependencias/imagens/cauda_esquerdo.png').convert_alpha()
        self.cauda_direita = pygame.image.load('dependencias/imagens/cauda_direito.png').convert_alpha()

        self.corpo_horizontal = pygame.image.load('dependencias/imagens/corpo_horizontal.png').convert_alpha()
        self.corpo_vertical = pygame.image.load('dependencias/imagens/corpo_vertical.png').convert_alpha()

        self.corpo_bl = pygame.image.load('dependencias/imagens/corpo_dobra_bl.png').convert_alpha()
        self.corpo_br = pygame.image.load('dependencias/imagens/corpo_dobra_br.png').convert_alpha()
        self.corpo_tl = pygame.image.load('dependencias/imagens/corpo_dobra_tl.png').convert_alpha()
        self.corpo_tr = pygame.image.load('dependencias/imagens/corpo_dobra_tr.png').convert_alpha()

        self.som_comer = pygame.mixer.Sound('dependencias/audio/comer.wav')
        self.som_morreu = pygame.mixer.Sound('dependencias/audio/game_over.mp3')

    def desenhar_cobra(self):
        self.update_cabeca()
        self.update_cauda()

        for index, bloco in enumerate(self.corpo):
            pos_x = bloco.x * corpo_cobra
            pos_y = bloco.y * corpo_cobra
            bloco_rect = pygame.Rect(pos_x, pos_y, corpo_cobra, corpo_cobra)

            if index == 0:
                janela.blit(self.cabeca, bloco_rect)
            elif index == len(self.corpo) -1:
                janela.blit(self.cauda, bloco_rect)
            else:
                bloco_antes = self.corpo[index + 1] - bloco
                bloco_depois = self.corpo[index - 1] - bloco
                if bloco_antes.x == bloco_depois.x:
                    janela.blit(self.corpo_vertical, bloco_rect)
                elif bloco_antes.y == bloco_depois.y:
                    janela.blit(self.corpo_horizontal, bloco_rect)
                else:
                    if bloco_antes.x == -1 and bloco_depois.y == -1 or bloco_antes.y == -1 and bloco_depois.x == -1:
                        janela.blit(self.corpo_tl, bloco_rect)
                    elif bloco_antes.x == 1 and bloco_depois.y == -1 or bloco_antes.y == -1 and bloco_depois.x == 1:
                        janela.blit(self.corpo_tr, bloco_rect)
                    elif bloco_antes.x == -1 and bloco_depois.y == 1 or bloco_antes.y == 1 and bloco_depois.x == -1:
                        janela.blit(self.corpo_bl, bloco_rect)
                    elif bloco_antes.x == 1 and bloco_depois.y == 1 or bloco_antes.y == 1 and bloco_depois.x == 1:
                        janela.blit(self.corpo_br, bloco_rect)

    def update_cabeca(self):
        direcao_cabeca = self.corpo[1] - self.corpo[0]
        if direcao_cabeca == Vector2(1, 0):
            self.cabeca = self.cabeca_esquerda
        elif direcao_cabeca == Vector2(-1, 0):
            self.cabeca = self.cabeca_direita
        elif direcao_cabeca == Vector2(0, 1):
            self.cabeca = self.cabeca_cima
        elif direcao_cabeca == Vector2(0, -1):
            self.cabeca = self.cabeca_baixo

    def update_cauda(self):
        direcao_cauda = self.corpo[-2] - self.corpo[-1]
        if direcao_cauda == Vector2(1, 0):
            self.cauda = self.cauda_esquerda
        elif direcao_cauda == Vector2(-1, 0):
            self.cauda = self.cauda_direita
        elif direcao_cauda == Vector2(0, 1):
            self.cauda = self.cauda_cima
        elif direcao_cauda == Vector2(0, -1):
            self.cauda = self.cauda_baixo

    def mover_cobra(self):
        if self.novo_corpo == True:
            copia_corpo = self.corpo[:]
            copia_corpo.insert(0, copia_corpo[0] + self.direcao)
            self.corpo = copia_corpo[:]
            self.novo_corpo = False

            copia_tempo = self.tempo
            copia_tempo = random.randint(10, 80)
            self.tempo = copia_tempo
        else:
            copia_corpo = self.corpo[:-1]
            copia_corpo.insert(0, copia_corpo[0] + self.direcao)
            self.corpo = copia_corpo[:]

    def add_corpo(self):
        self.novo_corpo = True
        self.novo_UPDATE_JANELA = True

    def som(self):
        self.som_comer.play()

    def som_morrer(self):
        self.morreu = True
        self.som_morreu.play()


    def parar_som_morrer(self):
        self.som_morreu.stop()

    def reset(self):
        y = (altura/corpo_cobra)/2
        self.corpo = [Vector2(5, y), Vector2(4, y), Vector2(3, y)]
        self.direcao = Vector2(1, 0)

    def velocidade(self):
        self.UPDATE_JANELA = pygame.USEREVENT
        tempo = self.tempo
        pygame.time.set_timer(self.UPDATE_JANELA, tempo)
        return self.UPDATE_JANELA

class COMIDA:
    def __init__(self):
        self.randomize()

    def desenhar_fruta(self):
        comida_ret = pygame.Rect(self.pos.x * corpo_cobra, self.pos.y * corpo_cobra, corpo_cobra, corpo_cobra)
        janela.blit(fruta_small, comida_ret)

    def randomize(self):
        self.x = random.randint(0, comprimento/corpo_cobra - 1)
        self.y = random.randint(0, altura/corpo_cobra - 1)
        self.pos = Vector2(self.x, self.y)
 
class MAIN:
    def __init__(self):
        self.cobra = COBRA()
        self.comida = COMIDA()

    def update(self):
        self.cobra.mover_cobra()
        self.comer()
        self.morte()
        self.para_outro_lado()

    def desenhar_elementos(self):
        self.comida.desenhar_fruta()
        self.cobra.desenhar_cobra()
        self.pontuacao()
        self.morte()

    def comer(self):
        if self.comida.pos == self.cobra.corpo[0]:
            self.comida.randomize()
            self.cobra.add_corpo()
            self.cobra.som()

        for bloco in self.cobra.corpo[1:]:
            if bloco == self.comida.pos:
                self.comida.randomize()

    def para_outro_lado(self):
        if self.cobra.corpo[0].x == comprimento/corpo_cobra:
            self.cobra.corpo[0].x = 0
        elif self.cobra.corpo[0].x == -1:
            self.cobra.corpo[0].x = comprimento/corpo_cobra - 1
        elif self.cobra.corpo[0].y == altura/corpo_cobra:
            self.cobra.corpo[0].y = 0
        elif self.cobra.corpo[0].y == -1:
            self.cobra.corpo[0].y = altura/corpo_cobra - 1

    def morte(self):
        for bloco in self.cobra.corpo[1:]:
            if bloco == self.cobra.corpo[0]:
                self.game_over()

    def game_over(self):     
        fim_de_jogo = False
        self.cobra.som_morrer()

        while not fim_de_jogo:
            janela.blit(fim, fim_ret)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_c:
                        self.cobra.reset()
                        fim_de_jogo = True
                        self.cobra.parar_som_morrer()
                    elif evento.key == pygame.K_s:
                        pygame.quit()
                        exit()

    def pontuacao(self):
        pontos_texto = str(len(self.cobra.corpo) - 3)
        pontos_superficie = fonte.render(pontos_texto, True,(56, 74, 12))
        pontos_x = 60
        pontos_y = 40
        pontos_ret = pontos_superficie.get_rect(center = (pontos_x, pontos_y))
        fruta_ret = fruta.get_rect(midright = (pontos_ret.left, pontos_ret.centery))

        janela.blit(pontos_superficie, pontos_ret)
        janela.blit(fruta, fruta_ret)

pygame.init()

comprimento = 1200
altura = 800
corpo_cobra = 20

janela = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('Jogo da Cobra')
relogio = pygame.time.Clock()

relva = pygame.image.load('dependencias/imagens/fundo.jpg').convert()
fruta = pygame.image.load('dependencias/imagens/apple.png').convert_alpha()
fruta_small = pygame.transform.scale(fruta, (20, 20))
fim = pygame.image.load('dependencias/imagens/game_over.png').convert_alpha()
fim_ret = fim.get_rect(center = (comprimento/2, altura/2))

fonte = pygame.font.Font('dependencias/fonte/Violet-Smile.ttf', 30)

main_game = MAIN()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == main_game.cobra.velocidade():
            main_game.update()
        if evento.type == pygame.KEYDOWN:
            if evento.key in (pygame.K_UP, pygame.K_w):
                if main_game.cobra.direcao.y != 1:
                    main_game.cobra.direcao = Vector2(0, -1)
            elif evento.key in (pygame.K_DOWN, pygame.K_s):
                if main_game.cobra.direcao.y != -1:
                    main_game.cobra.direcao = Vector2(0, 1)
            elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                if main_game.cobra.direcao.x != -1:
                    main_game.cobra.direcao = Vector2(1, 0)
            elif evento.key in (pygame.K_LEFT, pygame.K_a):
                if main_game.cobra.direcao.x != 1:
                    main_game.cobra.direcao = Vector2(-1, 0)

    janela.blit(relva, (0, 0))

    main_game.desenhar_elementos()
    pygame.display.update()

    relogio.tick(60)