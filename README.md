

<h1 align="center"> 🍓 Object Detection 🍓</h1>
<h3 align="center">  Em desenvolvimento  </h3>

<p align="center">Treinando e detectando objetos com Haar Cascade (Python + OpenCV)</p>

<p align="left">Neste projeto, está sendo implementado o método Haar Cascade para exemplificar a deteção de objetos proposta por Paul Viola e Michael Jones em seu artigo "Rapid Object Detection using a Boosted Cascade of Simple Features" em 2001. Esse artigo trata de uma abordagem baseada em Machine Learning, em que uma função cascade é treinada com o uso de muitas imagens positivas e negativas. </p>

## 🎯 Objetivo 🎯

A aplicação busca detectar e identificar "morangos" através de uma webcam.


## ⚒️ Ferramentas ⚒️
As seguintes ferramentas foram usadas na construção do projeto:

- [Python 2.7.18] - https://www.python.org/downloads/
- [Numpy (Numerical Python)] - https://numpy.org
- [VSCode] - https://code.visualstudio.com
- [OpenCV 3.4.4] - https://opencv.org


# 💻 Como utilizar? 💻

### Clone
- Clone este repositório na sua máquina local
```
$ git clone https://github.com/luanagribel/ObjectDetection.git
```

### Unzip files
- Descompacte as pastas "info.zip" e "negativas.zip" localizadas na pasta "Haar Cascade"
- OBS: As mesmas foram compactadas devido ao elevado número de imagens para treinamento

### Detection test
- Através do terminal, rode o script para a detecção dos morangos
```
python detecta.py
```
- Abra a imagem "morango.jpg" através de um smartphone e a posicione direcionada para a webcam

  <img src="https://i.ibb.co/T2XfJ8w/5193fa15-2317-4f6d-af56-0de52b685e5b.jpg" >
  
### Detecting new objects

- Caso tenha vontade de mudar o objeto a ser detectado, basta alterar a imagem positiva no diretório e posteriormente realizar o treinamento.
- Para utilizar imagens diferentes/adicionar novas para as negativas você pode acessar o site http://image-net.org/ e escolher diversos datasets! O download pode ser feito clicando em Download -> Image URLs e então na página que se abrirá haverá uma explicação de como chegar à página com a lista de URLs.
- OBS: Lembre-se de limpar a pasta info antes de realizar o treinamento, para que as novas imagens treinadas sejam inseridas na mesma.
- Comando para a criação das novas amostras:

```
opencv_createsamples -img NOME_DO_ARQUIVO.jpg -bg ARQUIVO_LISTA_DE_IMAGENS_NEGATIVAS.txt -info DIRETÓRIO_SAÍDA/ARQUIVO_LISTA.lst -pngoutput DIRETÓRIO_SAÍDA -maxxangle ÂNGULO_MÁXIMO_EIXO_X -maxyangle ÂNGULO_MÁXIMO_EIXO_Y -maxzangle ÂNGULO_MÁXIMO_EIXO_Z -num NÚMERO_DE_IMAGENS_NEGATIVAS

```

- Comando para a criação do vetor:

```
opencv_createsamples -info DIRETÓRIO/ARQUIVO_LISTA.lst -num NÚMERO_DE_IMAGENS_NEGATIVAS -w LARGURA_DA_AMOSTRA -h ALTURA_DA_AMOSTRA -vec ARQUIVO_VETORES

```

- Comando para realizar o treinamento:

```
opencv_traincascade -data PASTA_DESTINO -vec VETOR.vec -bg bg.txt -numPos (NÚMERO_DE_IMAGENS - 200) -numNeg METADE_DO_NUMPOS -numStages NÚMERO_DE_ESTAGIOS_DO_TREINO -w LARGURA_DA_AMOSTRA -h ALTURA_DA_AMOSTRA

```

  
