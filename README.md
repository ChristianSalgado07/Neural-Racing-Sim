# Neural Racing Simulator (Python & Pygame)

Una simulación interactiva donde vehículos aprenden a conducir en una pista mediante **Neuroevolución**. Proyecto construido desde cero utilizando **Python**, **Pygame** para el motor físico y visual, y **NumPy** para el procesamiento matemático de la red neuronal. 

## Características

* **Red Neuronal Personalizada (MLP):** Implementación de un Perceptrón Multicapa desde cero para procesar los datos del entorno y controlar la aceleración y dirección de los vehículos.
* **Algoritmo Genético:** Sistema de evolución natural donde el top de los mejores autos sobrevive, transmitiendo y mutando sus "pesos neuronales" a la siguiente generación.
* **Raycasting (Visión Artifical):** Sistema de sensores que lanza rayos en 5 direcciones para calcular distancias exactas hacia los bordes de la pista.
* **Mecánicas de Fitness y Supervivencia:** Puntuación basada en la distancia real recorrida, con un sistema de tiempo límite (Timeout) para castigar comportamientos estáticos.
* **UI Estética Dark/Neon:** Interfaz moderna con visualización de los rayos en tiempo real y estadísticas en pantalla (Generación actual, Supervivientes, Mejor Puntaje y Tiempo).

## Tecnologías Usadas

* **Lenguaje:** Python 3.x
* **Librería Gráfica:** [Pygame](https://www.pygame.org/)
* **Librería Matemática:** [NumPy](https://numpy.org/)

## Controles e Interacción

A diferencia de un juego tradicional, este es un simulador de "Zero-Player". La interacción se basa en la observación del aprendizaje automático.

| Tecla / Acción | Descripción |
| :--- | :--- |
| **Simulación Automática** | La IA controla todos los vehículos. |
| **Cerrar Ventana** | Termina la simulación y el ciclo de Pygame. |

## Instalación y Ejecución

Para ejecutar este proyecto necesitas Python 3 instalado en tu Mac. Se recomienda usar un entorno virtual.

### Pasos en la terminal:
```bash
# 1. Clona este repositorio (si aplica) o entra a tu carpeta
cd neural-racing-sim

# 2. Crea y activa tu entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instala las dependencias necesarias
pip install pygame numpy

# 4. Corre la simulación
python main.py
```
## Créditos

Desarrollado por **Christian Salgado**.
