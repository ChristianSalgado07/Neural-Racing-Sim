import pygame
import math
from neural_car import NeuralCar

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0  # Apuntando hacia arriba para seguir la pista
        self.speed = 0
        self.alive = True
        self.distance = 0
        self.brain = NeuralCar()
        self.sensor_lines = [] # Para guardar y dibujar los rayos visuales
        self.current_checkpoint = 1  # Empieza buscando el segundo punto de la pista
        self.checkpoints_passed = 0  # Cuenta cuántos puntos ha tocado en total
        
    def get_sensors(self, screen):
        sensors = []
        self.sensor_lines = []
        # 5 sensores: -90, -45, 0 (frente), 45, 90
        angles = [-math.pi/2, -math.pi/4, 0, math.pi/4, math.pi/2]
        
        for angle_offset in angles:
            ray_angle = self.angle + angle_offset
            dist = 0
            max_dist = 150 # Distancia máxima de visión
            
            check_x, check_y = self.x, self.y
            
            while dist < max_dist:
                check_x = self.x + math.cos(ray_angle) * dist
                check_y = self.y - math.sin(ray_angle) * dist
                
                # Si el rayo sale de la ventana
                if check_x < 0 or check_x >= 1200 or check_y < 0 or check_y >= 800:
                    break
                
                # Detectar color del pixel
                try:
                    color = screen.get_at((int(check_x), int(check_y)))
                    if color[:3] != (30, 30, 40):
                        break
                except IndexError:
                    break
                
                dist += 4
                
            sensors.append(dist / max_dist)
            self.sensor_lines.append((int(check_x), int(check_y)))   
            
        return sensors            
        
    def update(self, screen, track_points):
        if not self.alive:
            return
        
        # Si carro toca límite, muere
        try:
            if screen.get_at((int(self.x), int(self.y)))[:3] != (30, 30, 40):
                self.alive = False
                return
        except IndexError:
            self.alive = False
            return
        
        real_sensors = self.get_sensors(screen)
        
        # Procesa sensores y decide
        steer, gas = self.brain.think(real_sensors)
        
        self.angle += steer * 0.1
        self.speed += gas * 0.5      
        self.speed = max(1, min(self.speed, 6)) # Limitar la velocidad
        
        # Mover carro
        self.x += math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed
        
        target_x, target_y = track_points[self.current_checkpoint]
        
        # Teorema de Pitágoras para saber la distancia exacta al siguiente punto
        dist_to_target = math.hypot(target_x - self.x, target_y - self.y)
        
        # Si el carro toca el checkpoint
        if dist_to_target < 80:
            self.current_checkpoint += 1
            self.checkpoints_passed += 1
            
            # Si llegó al final del arreglo, le da la vuelta al circuito y vuelve a buscar el 0
            if self.current_checkpoint >= len(track_points):
                self.current_checkpoint = 0
                
        # Ganan 1000 puntos por cada checkpoint que pasen y se premian por dar cada paso en la dirección correcta.
        self.distance = (self.checkpoints_passed * 1000) + (1000 - dist_to_target)
                
    def draw(self, screen):
        # Dibujar rayos de los sensores
        if self.alive:
            for pt in self.sensor_lines:
                pygame.draw.line(screen, (150, 150, 50), (int(self.x), int(self.y)), pt, 1) 
                # Punto en el contacto
                pygame.draw.circle(screen, (255, 100, 100), pt, 2) 

        # Dibujar el carro
        color = (0, 255, 100) if self.alive else (70, 70, 70)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 6)