# https://www.youtube.com/watch?v=Wx3SyNwZtsA&ab_channel=HashtagPrograma%C3%A7%C3%A3o
# Vai precisar das bibliotecas opencv e tesseract
# pip install opencv-python
# pip install pytesseract


# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# I see steps are scattered in different answers. Based on my recent experience with this pytesseract error on Windows, writing different steps in sequence to make it easier to resolve the error:

# 1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

# 2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

# 3. pip install pytesseract

# 4. Set the tesseract path in the script before calling image_to_string:

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'


import pytesseract
import cv2 # opencv é importado para o projeto como cv2


caminho_tesseract = r"C:\Program Files\Tesseract-OCR" # Local de instalação
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"

# Para tesseract ler em português
# https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata
# Faça o download do arquivo por.traineddata e salve na pasta tessdata dentro da pasta de instação do tesseract

# Passo 1: ler a imagem

imagem = cv2.imread("texto2.png")

# Passo 2: pedir para o tesseract extrair o texto da imagem
texto = pytesseract.image_to_string(imagem, lang="por")
print(texto)
