import pygame
import sys
from car import Car
from neural_car import next_generation

WIDTH, HEIGHT = 1200, 800
FPS = 60
TOTAL_CARS = 50

# Puntos del circuito
TRACK_POINTS = [
    (91, 167), (328, 159),
    (519, 240), (653, 155),
    (764, 165), (814, 186),
    (852, 235), (852, 265),
    (845, 304), (800, 333),
    (755, 348), (708, 367),
    (711, 411), (719, 458),
    (732, 485), (799, 526),
    (843, 549), (905, 563),
    (970, 599), (967, 632),
    (898, 729), (750, 729),
    (195, 711), (177, 564),
    (208, 512), (256, 486),
    (271, 443), (261, 396),
    (205, 365), (96, 316),
    (86, 174),
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neural Racing Simulator")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Courier", 24, bold=True)
    
    start_x, start_y = 91, 167
    
    cars = [Car(start_x, start_y) for _ in range(TOTAL_CARS)]
    
    generation = 1
    current_frame = 0
    max_frames = 100
    
    running = True
    while running:
        current_frame += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((15, 15, 25)) # Fondo azul oscuro
        
        TRACK_COLOR = (30, 30, 40) # Pista, color asfalto oscuro
        
        # Dibujar las líneas gruesas conectando los puntos
        pygame.draw.lines(screen, TRACK_COLOR, True, TRACK_POINTS, 120)
        
        # Dibujar círculos en cada punto para que las curvas sean redondas
        for p in TRACK_POINTS:
            pygame.draw.circle(screen, TRACK_COLOR, p, 60) # El radio es la mitad del grosor (60)

        # Lógica y evolución
        alive_count = 0
        best_distance = 0

        for car in cars:
            car.update(screen, TRACK_POINTS)
            if car.alive:
                alive_count += 1
            if car.distance > best_distance:
                best_distance = car.distance

        # Si todos mueren
        if alive_count == 0 or current_frame >= max_frames:
            print(f"Generación {generation} terminada. Evolucionando...")
            
            current_frame = 0
            max_frames += 20
            
            # 1. Extraemos los puntajes y cerebros de los carros muertos
            scores = [car.distance for car in cars]
            brains = [car.brain for car in cars]
            
            # 2. Cruce y mutación
            new_brains = next_generation(brains, scores)
            
            # 3. Nuevos carros con los cerebros evolucionados
            cars = []
            for brain in new_brains:
                new_car = Car(start_x, start_y)
                new_car.brain = brain
                cars.append(new_car)
                
            generation += 1

        # Carros
        for car in cars:
            car.draw(screen)

        # UI
        gen_text = font.render(f"Generation: {generation}", True, (255, 255, 255))
        alive_text = font.render(f"Alive: {alive_count} / {TOTAL_CARS}", True, (0, 255, 100))
        score_text = font.render(f"Best Score: {int(best_distance)}", True, (255, 200, 0))
        time_text = font.render(f"Time: {(current_frame / max_frames) * 100:.2f}%", True, (200, 200, 255))   
        
        screen.blit(gen_text, (20, 20))
        screen.blit(alive_text, (20, 50))
        screen.blit(score_text, (20, 80))
        screen.blit(time_text, (20, 110))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
