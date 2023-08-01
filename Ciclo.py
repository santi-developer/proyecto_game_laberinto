#se importa la libreria
import readchar
from readchar import readkey, key


while True:
    # funcion para leer la tecla que se ingresa por teclado
    tecla=readkey()
    
    # condicion en la que si se oprime flecha hacia arriba el bucle se acaba
    if tecla==key.UP:
        print("fin del bucle ")
        break
        
        # condicion para imprimir la tecla leida por teclado   
    else:
        print("la letra que usted oprimio fue: "+ tecla)
         
    
    


        
        
   
            


            
        

