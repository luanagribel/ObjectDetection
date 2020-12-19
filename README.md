

<h1 align="center"> 🍓 Object Detection 🍓</h1>
<p align="center">Treinando e detectando objetos com Haar Cascade (Python + OpenCV)</p>

<p align="left">Neste projeto, está sendo implementado o método Haar Cascade para exemplificar a deteção de objetos proposta por Paul Viola e Michael Jones em seu artigo "Rapid Object Detection using a Boosted Cascade of Simple Features" em 2001. Esse artigo trata de uma abordagem baseada em Machine Learning, em que uma função cascade é treinada com o uso de muitas imagens positivas e negativas. </p>

## 🎯 Objetivo 🎯

A aplicação busca detectar e identificar "morangos" através de uma webcam.


## ⚒️ Ferramentas ⚒️
As seguintes ferramentas foram usadas na construção do projeto:

- [Python 2.7.18]
- [Numpy (Numerical Python)]
- [VSCode]
- [OpenCV 3.4.4]


# 💻 Como utilizar? 💻

### Clone
- Clone este repositório na sua máquina local
```
$ git clone https://github.com/luanagribel/ObjectDetection.git
```

### Unzip files
- Descompacte as pastas "info.zip" e "negativas.zip" localizadas na pasta "Haar Cascade"
- OBS: As mesmas foram compactadas devido ao elevado número de imagens para treinamento
- OBS2: Caso queira utilizar imagens diferentes você pode acessar o site http://image-net.org/ e escolher diversos datasets :D

### Detect
- Através do terminal, rode o script para a detecção dos morangos
```
python detecta.py
```
- Abra a imagem "morango.jpg" através de um smartphone e a posicione direcionada para a webcam
