import pygame

pygame.init()  # Inicializa o Pygame

# Define o tamanho da janela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Janela Básica")

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))  # Pinta a tela de branco

    pygame.display.flip()  # Atualiza a tela

pygame.quit()  # Fecha o Pygame