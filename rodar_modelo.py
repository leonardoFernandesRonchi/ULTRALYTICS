
from ultralytics import YOLO

# Carrega o modelo treinado
model = YOLO(
    "runs/detect/overwatch_model-5/weights/best.pt"
)

# Detecta os personagens no gameplay e salva o vídeo
results = model.predict(
    source="gameplay.mp4",
    save=True,
    conf=0.5,
    stream=True
)

# Processa os resultados gradualmente
for result in results:
    pass

print("Processamento do vídeo concluído!")