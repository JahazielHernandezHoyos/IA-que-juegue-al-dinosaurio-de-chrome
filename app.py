import cv2
import pyautogui
import numpy as np

codec = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("Grabacion.avi", codec , 60, (1366, 768)) 
cv2.namedWindow("Grabando", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Grabando", 480, 270)

while True:
    img = pyautogui.screenshot() 
    frame = np.array(img) 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    out.write(frame) 
    cv2.imshow('Grabando', frame) 
    #detectar el cumulo del color en la pantalla
    if cv2.waitKey(1) == ord('q'): 
        break

out.release() # cerrar el archivo de video
cv2.destroyAllWindows() # cerrar la ventana