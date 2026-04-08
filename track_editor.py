import pygame
import sys

WIDTH, HEIGHT = 1200, 800
TRACK_COLOR = (30, 30, 40)
THICKNESS = 60 # Cambiar ancho

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neural Racing - Track Editor")
    
    points = []
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            # Si das clic izquierdo, agregamos el punto a la lista
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    points.append(event.pos)
                    
            # Controles de teclado
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Imprime el código listo para copiar al presionar ESPACIO
                    print("\n--- COPIA ESTO EN TU main.py ---")
                    print("TRACK_POINTS = [")
                    for i in range(0, len(points), 2):
                        # Formateo bonito de a dos puntos por línea
                        chunk = points[i:i+2]
                        print("    " + ", ".join([f"({p[0]}, {p[1]})" for p in chunk]) + ",")
                    print("]")
                    print("----------------------------------\n")
                
                elif event.key == pygame.K_c:
                    # Limpia la pista al presionar 'C'
                    points = []

        # --- DIBUJO ---
        screen.fill((15, 15, 25)) # Fondo Dark
        
        # Si hay más de un punto, dibujamos el asfalto grueso
        if len(points) >= 2:
            pygame.draw.lines(screen, TRACK_COLOR, False, points, THICKNESS)
            
        # Dibujamos las curvas redondas y un puntito rojo para saber dónde diste clic
        for p in points:
            pygame.draw.circle(screen, TRACK_COLOR, p, THICKNESS // 2)
            pygame.draw.circle(screen, (255, 50, 50), p, 3) # Guía visual del clic

        # Textos de ayuda
        font = pygame.font.SysFont("Courier", 18, bold=True)
        screen.blit(font.render("Click Izquierdo: Poner punto", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render("Tecla 'C': Borrar todo", True, (255, 255, 255)), (10, 35))
        screen.blit(font.render("Tecla ESPACIO: Exportar a terminal", True, (0, 255, 100)), (10, 60))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
