import pygame
import sys
from car import Car
from neural_car import next_generation

WIDTH, HEIGHT = 1200, 800
FPS = 60
TOTAL_CARS = 50

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Neural Racing Simulator")
    clock = pygame.time.Clock()
    
    font = pygame.font.SysFont("Courier", 24, bold=True)
    
    start_x, start_y = 160, HEIGHT // 2
    
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
        pygame.draw.ellipse(screen, TRACK_COLOR, (100, 100, WIDTH-200, HEIGHT-200), 120)

        # Lógica y evolución
        alive_count = 0
        best_distance = 0

        for car in cars:
            car.update(screen)
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
        time_text = font.render(f"Time: {current_frame / max_frames}", True, (200, 200, 255))
        
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