import os
import random
import shutil

# Pasta onde estão os 515 frames que extraímos do vídeo.
source = "overwatch_frames"



# Pastas onde as imagens serão colocadas.
train_dir = "overwatch_dataset/images/train"
val_dir = "overwatch_dataset/images/val"

# Cria as pastas caso elas ainda não existam.
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Pega todos os arquivos da pasta de frames.
images = [
    file
    for file in os.listdir(source)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Embaralha as imagens aleatoriamente.
random.shuffle(images)

# 80% para treinamento.
train_size = int(len(images) * 0.8)

train_images = images[:train_size]
val_images = images[train_size:]

# Copia as imagens para train.
for image in train_images:
    shutil.copy(
        os.path.join(source, image),
        os.path.join(train_dir, image)
    )

# Copia as imagens para val.
for image in val_images:
    shutil.copy(
        os.path.join(source, image),
        os.path.join(val_dir, image)
    )

print(f"Total de imagens: {len(images)}")
print(f"Imagens de treino: {len(train_images)}")
print(f"Imagens de validação: {len(val_images)}")