import cv2

def img2bits(imgPath):
    img = cv2.imread(imgPath, 2) # Abrir imagen
    
    ret, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # Convertir a binario
    
    # Para ver la imagen en blanco y negro
    '''
    cv2.imshow("Binary", bw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    cadena = ''
    for row in bw:
        for i in range(len(row)):
            if (row[i] == 255):
                cadena += '0'
            else:
                cadena += '1'
        # Para ver la imagen al hacer zoom out :D
        # cadena += '\n'
            

    return cadena

print(img2bits('p1.jpg'))