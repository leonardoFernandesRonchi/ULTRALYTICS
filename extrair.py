import cv2
import os

# Nome do vídeo que será utilizado.
# O arquivo gameplay.mp4 precisa estar na mesma pasta deste script.
video = "gameplay.mp4"

# Pasta onde os frames extraídos serão salvos.
output = "overwatch_frames"

# Cria a pasta caso ela ainda não exista.
# exist_ok=True evita erro caso a pasta já exista.
os.makedirs(output, exist_ok=True)

# Abre o vídeo usando o OpenCV.
cap = cv2.VideoCapture(video)

# Obtém a quantidade de frames por segundo (FPS) do vídeo.
# Por exemplo:
# 60 FPS -> 60 frames por segundo
# 30 FPS -> 30 frames por segundo
fps = cap.get(cv2.CAP_PROP_FPS)

# Contador que indica qual frame do vídeo estamos processando.
frame_number = 0

# Contador de imagens que já foram salvas.
saved = 0

# Loop que percorre todos os frames do vídeo.
while True:

    # Lê o próximo frame do vídeo.
    #
    # ret:
    #   True  -> conseguiu ler o frame
    #   False -> chegou ao final do vídeo ou ocorreu um erro
    #
    # frame:
    #   contém a imagem daquele momento do vídeo
    ret, frame = cap.read()

    # Se não conseguiu ler o frame, interrompe o loop.
    # Normalmente isso acontece quando chegamos ao final do vídeo.
    if not ret:
        break

    # Salva aproximadamente 1 frame a cada segundo.
    #
    # Exemplo com vídeo de 60 FPS:
    # frame 0   -> salva
    # frame 60  -> salva
    # frame 120 -> salva
    # frame 180 -> salva
    #
    # Assim não precisamos salvar todos os frames do vídeo.
    if frame_number % int(fps) == 0:

        # Salva o frame como uma imagem JPG.
        #
        # saved: número da imagem que estamos salvando.
        #
        # :04d significa que o número terá 4 dígitos:
        #
        # 1    -> 0001
        # 25   -> 0025
        # 100  -> 0100
        # 1000 -> 1000
        #
        # Portanto teremos:
        # frame_0000.jpg
        # frame_0001.jpg
        # frame_0002.jpg
        # ...
        cv2.imwrite(
            f"{output}/frame_{saved:04d}.jpg",
            frame
        )

        # Aumenta o contador de imagens salvas.
        saved += 1

    # Passa para o próximo frame do vídeo.
    frame_number += 1

# Libera o arquivo de vídeo.
# É importante fechar o recurso depois que terminamos de utilizá-lo.
cap.release()

# Mostra no terminal quantos frames foram extraídos.
print(f"{saved} frames extraídos.")