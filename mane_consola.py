import os

def limpiar_terminal():    
    #funcion para limpiar la terminal
    os.system('cls' if os.name=='nt' else 'clear')
    
   
def prinsipal ():
        
    number=0
    while number<=50:
        letra=str(input("ingrese la letra n para empezar"))
        
        if letra=="n":
            limpiar_terminal()
            iterador=number
            while iterador <=50:
                print(iterador)
                iterador=iterador+1
            number=number+1 
        else:
            print("ingrese la tecla correcta")
    print("fin del bucle")        
                   
prinsipal()
        
    


            
        
        
        