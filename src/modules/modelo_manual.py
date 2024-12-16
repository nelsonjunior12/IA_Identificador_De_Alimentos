import numpy as np
import json

from keras._tf_keras.keras.models import load_model
from keras._tf_keras.keras.utils import load_img, img_to_array

from constants import IMAGE_SIZE, MODEL_NAME, INDEX_JSON_NAME

class ManualModel:
    def __init__(self):
        # Carregar os class_indices
        with open(f'{INDEX_JSON_NAME}.json', 'r') as json_file:
            self.class_indices = json.load(json_file)

    # Função para prever a imagem
    def classify_food_image(self, image_path:str):
        # Carrega o modelo salvo
        model = load_model(f'{MODEL_NAME}.h5')

        # Carrega a imagem
        image = load_img(image_path, target_size=IMAGE_SIZE)
        image_array = img_to_array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Faz a previsão
        prediction = model.predict(image_array)
        class_idx = np.argmax(prediction)

        # Obtém o nome da classe
        class_name = list(self.class_indices.keys())[list(self.class_indices.values()).index(class_idx)]

        return class_name

