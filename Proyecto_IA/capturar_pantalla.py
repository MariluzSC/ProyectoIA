import cv2
import os 

if os.path.exists('captura_camara.png'):
    os.remove('captura_camara.png')
# Iniciar la captura de la cámara
cap = cv2.VideoCapture(0)  # El número 0 indica la cámara predeterminada (puedes probar con otros números si tienes varias cámaras)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Leer continuamente los fotogramas de la cámara
while True:
    ret, frame = cap.read()  # Leer un fotograma de la cámara

    if not ret:
        print("Error: No se puede recibir fotograma (quizás la cámara está desconectada?).")
        break

    # Mostrar el fotograma en una ventana
    cv2.imshow('Captura de cámara', frame)

    # Esperar a que se presione la tecla 'c' para capturar un fotograma
    if cv2.waitKey(1) & 0xFF == ord('c'):
        # Guardar la imagen capturada en un archivo
        cv2.imwrite('captura_camara.png', frame)
        print("Fotograma capturado y guardado como captura_camara.png.")
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
