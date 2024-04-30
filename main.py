import cv2;

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

foto = cv2.imread("people.jpg")
foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

faces_detectadas = detector.detectMultiScale(foto_cinza, scaleFactor=1.05, maxSize=(78, 78), minSize=(54, 54))
for x, y, l, a in faces_detectadas:
    #arq_imagem, ponto_inicial, ponto_final, cor(BGR), espessura_retangulo_px
    foto = cv2.rectangle(foto, (x, y), (x+l, y+a), (0, 0, 255),2)

print(faces_detectadas)
cv2.imshow("abelzinho", foto)
cv2.waitKey()
