import numpy as np
import random

class NeuralCar:
    def __init__(self, weights=None):
        if weights is None:
            # 5 sensores, 4 neuronas ocultas, 2 salidas (girar, acelerar)
            self.w1 = np.random.randn(5, 4)
            self.w2 = np.random.randn(4, 2)
        else:
            self.w1, self.w2 = weights

    def think(self, sensors):
        # Forward pass (Feedforward)
        hidden = np.tanh(sensors @ self.w1)
        output = np.tanh(hidden @ self.w2)
        
        steer = output[0]  # Valor entre -1 (izquierda) y 1 (derecha)
        gas = output[1]    # Valor para acelerar/frenar
        return steer, gas

    def mutate(self):
        # Mutaciones aleatorias para la evolución
        self.w1 += np.random.randn(5, 4) * 0.3
        self.w2 += np.random.randn(4, 2) * 0.3

def next_generation(cars, scores):
    # El top 20% sobrevive y se reproduce
    top = sorted(zip(scores, cars), key=lambda x: -x[0])[:max(1, len(cars)//5)]
    
    new_cars = []
    for _ in range(len(cars)):
        parent = random.choice(top)[1]
        # Crear un hijo copiando los pesos del padre
        child = NeuralCar((parent.w1.copy(), parent.w2.copy()))
        child.mutate()
        new_cars.append(child)
        
    return new_cars