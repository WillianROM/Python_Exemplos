# https://www.youtube.com/watch?v=GMqFZ7f0dy4&list=PLmOO8X35BgB1rDGTZ1q4tzxCeK7RnFNqD&index=11&ab_channel=RonanVico

import cv2 #pip install opencv-python
import pytesseract  #pip install pytesseract

# Acesse https://github.com/UB-Mannheim/tesseract/wiki
# Faça download da última versão do tesseract....exe
# Daí execute para instalar

# Ler a imagem com opencv:
img = cv2.imread("imagemTeste.png") 

#Apontar onde está o executável do pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


config = r'--oem 3 --psm 6'


#Reconhecer as letras da imagem lido anteriormente
resultado = pytesseract.image_to_string(img,config=config)

print(resultado)
