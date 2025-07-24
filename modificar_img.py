import cv2 as cv
import numpy as np

def dibujar_estrella_cruzada(imagen, color=(0, 255, 0), grosor=2, radio_factor=1/3):
    # Obtener las dimensiones de la imagen
    height, width, channels = imagen.shape

    # Definir el centro de la imagen
    center_x, center_y = width // 2, height // 2

    # Definir el radio del círculo invisible
    radius = min(width, height) * radio_factor

    # Definir los 5 puntos de la estrella
    points = []
    for i in range(5):
        angle = np.pi / 2 + i * 2 * np.pi / 5
        x = int(center_x + radius * np.cos(angle))
        y = int(center_y - radius * np.sin(angle))  # Invertir el signo de seno para la orientación correcta
        points.append((x, y))

    # Dibujar las líneas que conectan los puntos de la estrella, cruzando líneas
    for i in range(5):
        cv.line(imagen, points[i], points[(i + 2) % 5], color, grosor)

# Cargar la imagen
imagen = cv.imread('cpriko.jpg')

dibujar_estrella_cruzada(imagen)

# Mostrar la imagen
cv.imshow('Imagen con Estrella Cruzada', imagen)
cv.waitKey(0)
cv.destroyAllWindows()