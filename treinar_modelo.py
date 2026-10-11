
from ultralytics import YOLO

# Carrega um modelo pré-treinado como ponto de partida
model = YOLO("yolo26n.pt")

# Treina o modelo com seu dataset do Overwatch
model.train(
    data="overwatch_dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=4,
    name="overwatch_model"
)