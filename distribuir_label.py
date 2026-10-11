import os
import shutil

# Onde estão os labels exportados pelo CVAT
cvat_labels = "overwatch/labels/train"

# Dataset que você já possui
train_images = "overwatch_dataset/images/train"
val_images = "overwatch_dataset/images/val"

train_labels = "overwatch_dataset/labels/train"
val_labels = "overwatch_dataset/labels/val"

# Cria as pastas caso não existam
os.makedirs(train_labels, exist_ok=True)
os.makedirs(val_labels, exist_ok=True)


def copiar_labels(images_dir, labels_dir):
    copied = 0
    missing = 0

    for image in os.listdir(images_dir):

        # Remove a extensão da imagem
        name = os.path.splitext(image)[0]

        # Label correspondente
        label = name + ".txt"

        origem = os.path.join(cvat_labels, label)
        destino = os.path.join(labels_dir, label)

        if os.path.exists(origem):
            shutil.copy2(origem, destino)
            copied += 1
        else:
            print(f"Label não encontrado: {label}")
            missing += 1

    return copied, missing


# Train
train_copied, train_missing = copiar_labels(
    train_images,
    train_labels
)

# Val
val_copied, val_missing = copiar_labels(
    val_images,
    val_labels
)


print("\nResultado:")
print(f"Train: {train_copied} labels copiados")
print(f"Train: {train_missing} labels ausentes")

print(f"Val: {val_copied} labels copiados")
print(f"Val: {val_missing} labels ausentes")