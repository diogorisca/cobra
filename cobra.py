import pygame
import random
from sys import exit
 
pygame.init()
 
branco = (255, 255, 255)
amarelo = (255, 255, 102)
preto = (0, 0, 0)
vermelho = (255, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)
 
comprimento = 600
altura = 400
 
janela = pygame.display.set_mode((comprimento, altura))
pygame.display.set_caption('Jogo da Cobra')
 
relogio = pygame.time.Clock()
 
corpo_cobra = 10
 
fonte = pygame.font.SysFont("bahnschrift", 25)
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

def pontuacao(pontos):
    valor = fonte_pontuacao.render(str(pontos), True, amarelo)
    janela.blit(valor, [15, 0])

def cobra(corpo_cobra, lista_cobra):
    for i in lista_cobra:
        pygame.draw.rect(janela, azul, [i[0], i[1], corpo_cobra, corpo_cobra])

def mensagem1(msg, cor):
    mesg = fonte.render(msg, True, cor)
    janela.blit(mesg, [comprimento/3, altura-250])

def mensagem2(msg, cor):
    mesg = fonte.render(msg, True, cor)
    janela.blit(mesg, [comprimento/5, altura-200])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = comprimento / 2
    y1 = altura / 2
 
    x1_novo = 0
    y1_novo = 0
 
    lista_cobra = []
    comprimento_cobra = 1
 
    comida_x = round(random.randrange(0, comprimento - corpo_cobra) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - corpo_cobra) / 10.0) * 10.0
 
    velocidade_cobra = 15

    while not game_over:
 
        while game_close == True:
            janela.fill(preto)
            mensagem1("Mataste a Cobra!", vermelho)
            mensagem2("C para Continuar ou S para Sair", vermelho)
 
            pygame.display.update()
 
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        gameLoop()
 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_novo = -corpo_cobra
                    y1_novo = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_novo = corpo_cobra
                    y1_novo = 0
                elif evento.key == pygame.K_UP:
                    x1_novo = 0
                    y1_novo = -corpo_cobra
                elif evento.key == pygame.K_DOWN:
                    x1_novo = 0
                    y1_novo = corpo_cobra

        if x1 == comprimento:
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_UP, pygame.K_DOWN):
                    x1 = 0
            else:
                x1 = -10
        elif x1 == -10:
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_UP, pygame.K_DOWN):
                    x1 = comprimento - 10
            else:
                x1 = comprimento
        elif y1 == -10:
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    y1 = altura - 10
            else:
                y1 = altura
        elif y1 == altura:
            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_RIGHT, pygame.K_LEFT):
                    y1 = 0
            else:
                y1 = -10
        elif y1 == 0:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    y1 = altura
        elif y1 == altura - 10:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    y1 = -10
        elif x1 == comprimento - 10:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    x1 = -10
        elif x1 == 0:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1 = comprimento


        x1 += x1_novo
        y1 += y1_novo
        janela.fill(preto)
        pygame.draw.rect(janela, verde, [comida_x, comida_y, corpo_cobra, corpo_cobra])
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]
 
        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                game_close = True
 
        cobra(corpo_cobra, lista_cobra)
        pontuacao(comprimento_cobra - 1)
 
        pygame.display.update()
 
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, comprimento - corpo_cobra) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - corpo_cobra) / 10.0) * 10.0
            comprimento_cobra += 1

            for i in range(5, 1001, 5):
                if comprimento_cobra - 1 == i:
                    velocidade_cobra = velocidade_cobra + random.randint(-10, 30)
                    if velocidade_cobra < 15:
                        velocidade_cobra = 15
                        velocidade_cobra = velocidade_cobra + random.randint(0, 30)

        relogio.tick(velocidade_cobra)
 
    pygame.quit()
    exit()
 
gameLoop()