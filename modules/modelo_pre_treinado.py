from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch

class PreTrainedModel:
    def __init__(self):
        # Carregar o processador e o modelo pré-treinado
        self.processor = AutoImageProcessor.from_pretrained("nateraw/food")
        self.model = AutoModelForImageClassification.from_pretrained("nateraw/food")

    # Função para processar a imagem e obter a previsão
    def classify_food_image(self, image_path):
        # Abrir e pré-processar a imagem
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")

        # Realizar a previsão com o modelo
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class_idx = logits.argmax(-1).item()

        # Obter o rótulo correspondente
        predicted_label = self.model.config.id2label[predicted_class_idx]
        return predicted_label