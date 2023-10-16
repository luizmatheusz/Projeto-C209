# bibliotecas necessárias
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pytesseract # OCR

# caminho da imagem
image_path = ''

# funcao para identificar caracteres em uma imagem
def extract_text(img):
    # identifica os caracteres
    texto = pytesseract.image_to_string(img, lang='por')  # 'por' para português
    linhas = []
    palavras_aux = []

    # organiza o texto encontrado, linha a linha
    for i in texto:
        if(i != '\n'):
            palavras_aux.append(i)

        else:
            if(len(palavras_aux) != 0):
                linhas.append(''.join(palavras_aux))
                palavras_aux = []

    # print linha a linha
    print("Texto extraído (linha a linha):")
    for i in linhas:
        print(i)


# Caminho para o executável do Tesseract (dependendo do seu sistema)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Abrir a imagem
imagem_rgb = np.array(Image.open(image_path))[:, :, :3]
l, c, p = imagem_rgb.shape

# Converter para escala de cinza - metodo average
imagem = np.zeros(shape=(l, c), dtype=np.uint8)
for i in range(l):
    for j in range(c):
        r = float(imagem_rgb[i, j, 0])
        g = float(imagem_rgb[i, j, 1])
        b = float(imagem_rgb[i, j, 2])
        
        imagem[i, j] = (r + g + b) / 3

# Binarização da imagem usando um limiar (threshold)
limiar = 150  # Valor do limiar (ajuste conforme necessário)
imagem_binarizada = np.where(imagem > limiar, 255, 0)  # Transforma pixels acima do limiar para branco (255) e abaixo para preto (0)

# Imagem binarizada usando o array NumPy
imagem_binarizada = Image.fromarray(imagem_binarizada.astype(np.uint8))

# Mostra as imagens na tela
plt.figure(figsize=(30, 16))
plt.subplot(1, 3, 1)
plt.imshow(imagem_rgb)
plt.subplot(1, 3, 2)
plt.imshow(imagem, cmap='gray')
plt.subplot(1, 3, 3)
plt.imshow(imagem_binarizada, cmap='gray')

# Fazer OCR na imagem
#texto1 = extract_text(imagem_rgb)
texto2 = extract_text(imagem)
#texto3 = extract_text(imagem_binarizada)