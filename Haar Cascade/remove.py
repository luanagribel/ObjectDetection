import numpy as np

import cv2

import os

igual = False

for file_type in ['negativas']:

    for img in os.listdir(file_type):

        for indisponivel in os.listdir('indisponiveis'):

            try:

                caminho_imagem = str(file_type)+'/'+str(img)

                indisponivel = cv2.imread('indisponiveis/'+str(indisponivel))

                pergunta = cv2.imread(caminho_imagem)

                if indisponivel.shape == pergunta.shape and not(np.bitwise_xor(indisponivel,pergunta).any()):

                    print('Apagando imagem indisponivel!')

                    print(caminho_imagem)

                    os.remove(caminho_imagem)

            except Exception as e:

                print(str(e))