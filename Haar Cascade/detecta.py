import cv2

# Define o numero da Webcam
NUM_WEBCAM = 0

# Inicializa o Classificador Cascade
XML_PATH = "/home/luana/Documents/c209/Haar Cascade/data/cascade.xml"

faceCascade = cv2.CascadeClassifier(XML_PATH)

# Inicializa a Webcam
vc = cv2.VideoCapture(NUM_WEBCAM)


while True:

# Define o frame que sera mostrado
    retval, frame = vc.read()
 

# Converte o frame para escalas de cinza e descarta os dados de cores
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

# Detecta objetos
    objetos = faceCascade.detectMultiScale(

    gray,

    scaleFactor=1.2,

    minNeighbors=20,

    minSize=(50, 50),

    flags=cv2.CASCADE_SCALE_IMAGE

    )

    # Desenha um retangulo em torno do objeto

    for (x, y, w, h) in objetos:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame,'Morango',(x,y-10),2,0.7,(0,0,255),2,cv2.LINE_AA)

    # Mostra o Frame ao usuario
    cv2.imshow("frame", frame)


    # Fecha o programa se o usuario apertar o botao ESC
    if cv2.waitKey(1) == 27:

        break

vc.release()
cv2.destroyAllWindows()