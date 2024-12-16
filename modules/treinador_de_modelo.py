import os
import json

from keras._tf_keras.keras.layers import Dense
from keras._tf_keras.keras.applications import MobileNetV2
from keras._tf_keras.keras.layers import Dense, GlobalAveragePooling2D
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

from constants import IMAGE_SIZE, BATCH_SIZE, EPOCHS, DATASET_PATH, MODEL_NAME

# 1. Carregando o conjunto de dados
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, 'Training'),
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, 'Training'),
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# 2. Criando o modelo com MobileNetV2
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(100, 100, 3))
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
output = Dense(len(train_generator.class_indices), activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# Compilando o modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Treinando o modelo
history = model.fit(
    train_generator,
    epochs=EPOCHS,
    validation_data=validation_generator
)

# 4. Salvando o modelo
model.save(f'{MODEL_NAME}.h5')

# 5. Salvando os class_indices
class_indices = train_generator.class_indices
with open('class_indices.json', 'w') as json_file:
    json.dump(class_indices, json_file)

print("Treinamento concluído. Modelo e class_indices salvos.")