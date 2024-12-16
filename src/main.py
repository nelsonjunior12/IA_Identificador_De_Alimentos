from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk
import pyttsx3

from modules.modelo_pre_treinado import PreTrainedModel
from modules.modelo_manual import ManualModel

class ClassifyFood:
    def __init__(self):
        self.pre_trained_model = PreTrainedModel()
        self.manual_model = ManualModel()
        self.predicted_food = None

    # Função para selecionar uma imagem e mostrar o resultado
    def classify_food_image_by_pretrained_model(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            # Exibir a imagem selecionada
            img = Image.open(file_path)
            img.thumbnail((250, 250))  # Reduz o tamanho para exibição
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk

            # Classificar a imagem
            self.predicted_food = self.pre_trained_model.classify_food_image(file_path)
            result_label.config(text=f"Alimento identificado: {self.predicted_food}")

            # Exibir o botão de TTS
            tts_button.pack(pady=10)

    # Função para selecionar uma imagem e mostrar o resultado
    def classify_food_image_by_manual_model(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if file_path:
            # Exibir a imagem selecionada
            img = Image.open(file_path)
            img.thumbnail((250, 250))  # Reduz o tamanho para exibição
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk

            # Classificar a imagem
            self.predicted_food = self.manual_model.classify_food_image(file_path)
            result_label.config(text=f"Alimento identificado: {self.predicted_food}")

            # Exibir o botão de TTS
            tts_button.pack(pady=10)

    # Função para realizar o TTS
    def perform_tts(self):
        if self.predicted_food:
            engine = pyttsx3.init()
            engine.say(f"O alimento identificado é {self.predicted_food}")
            engine.runAndWait()

# Instanciar a classe
classify_food = ClassifyFood()

# Criar a janela principal
root = Tk()
root.title("Classificador de Alimentos")

# Elementos da GUI
image_label = Label(root)
image_label.pack(pady=10)

result_label = Label(root, text="Selecione uma imagem para classificação.", font=("Arial", 14))
result_label.pack(pady=10)

select_button = Button(root, text="Utilizando Modelo Pre-Treinado (Comidas Gerais)", command=classify_food.classify_food_image_by_pretrained_model)
select_button.pack(pady=10)

select_button = Button(root, text="Utilizando Modelo Manual (Frutas)", command=classify_food.classify_food_image_by_manual_model)
select_button.pack(pady=10)

# Botão para TTS (inicialmente escondido)
tts_button = Button(root, text="Ouvir o nome do alimento", command=classify_food.perform_tts)

# Executar a aplicação
root.mainloop()
