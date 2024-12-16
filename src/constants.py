import os

def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))
current_dir = get_current_directory()

# Configuração inicial
IMAGE_SIZE = (100, 100)
BATCH_SIZE = 32
EPOCHS = 10
DATASET_PATH = os.path.join(current_dir, 'assets/Datasets/{caminho_do_dataset}') #Adicioane aqui o caminho do DS
MODEL_NAME = os.path.join(current_dir, 'assets/food_identifier_model_v3')
INDEX_JSON_NAME = os.path.join(current_dir, 'assets/class_indices_traduzidos')