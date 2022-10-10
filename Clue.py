#Librerias
from tkinter import *  
import random
#Crear ventana
root=Tk()
root.title("Clue")
root.geometry("1280x720")
root.resizable(0,0)
#Fondos
torre=PhotoImage(file="Torre.png")
ciudad=PhotoImage(file="Ciudad_Ensoñada.png")
europa=PhotoImage(file="Europa.png")
nessus=PhotoImage(file="Nessus.png")
luna=PhotoImage(file="Luna.png")
zme=PhotoImage(file="ZME.png")
#Protagonistas
crash=PhotoImage(file="CrashD.png")
ezio=PhotoImage(file="EzioD.png")
mario=PhotoImage(file="MarioD.png")
link=PhotoImage(file="LinkD.png")
kratos=PhotoImage(file="KratosD.png")
#Sospechosos
deadpool=PhotoImage(file="DeadpoolD.png")
falloutboy=PhotoImage(file="FalloutboyD.png")
hollow=PhotoImage(file="HollowD.png")
isaac=PhotoImage(file="IsaacD.png")
sans=PhotoImage(file="SansD.png")
#Lugar donde va el dialogo
BarraDialogo=PhotoImage(file="Dialogo.png")
#Listas
nombres=['Deadpool','Falloutboy','Hollow','Isaac','Sans']
imagenes=[deadpool,falloutboy,hollow,isaac,sans]
lugar=['Ciudad','Europa','Nessus','Luna','ZME']
arma=['Katana','Pistola','Espada plateada','Lagrimas','Bocina']
#Random del asesino
a=random.randint(0,4)
asesino=[nombres[a],lugar[random.randint(0,4)],arma[random.randint(0,4)],imagenes[a]]
#Creacion de mapa
Mapa=[] 
Conclusion=[]
AccionesCount=0
for z in range(5):
    a=random.randint(0,(len(nombres)-1))
    Mapa.append([nombres[a],lugar[random.randint(0,len(lugar)-1)],arma[random.randint(0,len(arma)-1)],imagenes[a]])
    nombres.remove(Mapa[z][0])
    lugar.remove(Mapa[z][1])
    arma.remove(Mapa[z][2])
    imagenes.remove(Mapa[z][3])
#Creacion del canvas
canvas=Canvas(root,width=1280,height=720)
canvas.pack(fill="both",expand=True)
canvas.pack()
canvas.create_image(0,0,image=torre,anchor="nw")
canvas.create_text(600,560,text="Selecciona un lugar para investigar",fill="Black",font=("Times New Roman",26)) 
canvas.create_text(600,600,text=f"Acciones restantes: {5-AccionesCount}", fill="Black",font=("Times New Roman",26)) 
#Cambiar a ciudad
def cambia_ciudad():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=ciudad,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Ciudad"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Cambiar a europa
def cambia_europa():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=europa,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Europa"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Cambiar a nessus
def cambia_nessus():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=nessus,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Nessus"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Cambiar a luna
def cambia_luna():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=luna,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Luna"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Cambiar a zme
def cambia_zme():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=zme,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="ZME"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Ocultar botones
def ocultar_botones():
    boton_luna.place_forget()
    boton_europa.place_forget()
    boton_ciudad.place_forget()
    boton_zme.place_forget()
    boton_nessus.place_forget()
    global EnLugar
    global DialogCount
    EnLugar=1
    DialogCount=0
#Mostrar botones    
def mostrar_botones():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_luna.place(x=1050,y=200)
    boton_europa.place(x=350,y=450)
    boton_ciudad.place(x=600,y=100)
    boton_zme.place(x=1050,y=450)
    boton_nessus.place(x=600,y=300)
#Mostrar opciones
def mostrar_opciones():
    boton_uno.place(x=600,y=280)
    boton_dos.place(x=600,y=320)
    boton_tres.place(x=600,y=360)
    boton_cuatro.place(x=600,y=400)
    boton_cinco.place(x=600,y=440)  
#Destino
def destino(lugar):
    texto=["Crash\n\nVale, hemos llegado a "+lugar+ "\n Deberiamos buscar algo que nos conduzca al asesino de Kratos",
           "Ezio\n\nCreo que no somos los unicos aqui.\n*"+Mapa[zmapa][0]+" se hace presente*",
           "Crash\n\nQue será lo proximo que haremos?"]
    Imagen_texto=[crash,ezio,crash]
    global dialogo
    global Imagen
    if DialogCount>0 and DialogCount<len(texto):  
        canvas.itemconfig(Imagen,image=Imagen_texto[DialogCount])
        canvas.itemconfig(dialogo,text=texto[DialogCount])
        if DialogCount==2:
            boton_investigar.place(x=750,y=500)
            boton_preguntar.place(x=950,y=500)    
    elif DialogCount>=len(texto):
        boton_siguiente.place_forget()
    else:
        Imagen=canvas.create_image(0,0,image=crash,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=texto[DialogCount],anchor="nw",font=("Times New Roman",20))
#Funcion para interrogar       
def interrogar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global DialogCount
    global EnLugar
    global num_dialogo 
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=4
    DialogCount=0
    boton_menu.place_forget()
    num_dialogo=random.randint(0,2) 
    conversacion()
#Funcion para observar area
def observar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=1000,y=680)
    global AccionesCount
    global EnLugar
    global DialogCount
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=2
    DialogCount=0
    boton_menu.place_forget()
    encontrarpista()
#Funcion para conversar
def conversacion():
    global dialogo
    global Imagen
    lugar_random=random.randint(0,4)
    nombre_random=random.randint(0,4)
    if Mapa[nombre_random][0]==Mapa[zmapa][0] or Mapa[nombre_random][0]==asesino[0]:  
        nombre_random=random.randint(0,4)
    if lugar_random==zmapa:
        lugar_random=random.randint(0,4)
    dialogo1=[f"Ezio \n\nHola {Mapa[zmapa][0]}.",
             f"{Mapa[zmapa][0]} \n\nQue onda, que los trae por aquí muchachos?",
             f"Link \n\nKratos ha muerto, y ahora estamos buscando pistas acerca de su muerte\n y su asesino,de hecho, de hecho, nos preguntabamos donde has estado en las últimas\n horas que han tanscurrido.",
             f"{Mapa[zmapa][0]} \n\nPues me encontraba en {Mapa[lugar_random][1]},\ny ya que lo han mencionado, creo recordar el haber avistado a {Mapa[nombre_random][0]} deambulando por el \nlugar.Puede que encuentren algo útil...",
             f"Ezio \n\nHmmm,que interesante...de cualquier manera iremos a echar un vistazo, {Mapa[zmapa][0]}",
             f"{Mapa[zmapa][0]} \n\nNo hay problema, nos vemos luego muchachos."]
    image=[ezio,Mapa[zmapa][3],link,Mapa[zmapa][3],ezio,Mapa[zmapa][3]]
   
    dialogos=[[f"{Mapa[zmapa][0]} \n\nHola muchachos, por cierto, y su amigo Saitama?",
                 "Mario \n\nHa muerto, y ahora estamos buscando pistas sobre ello\nNos puedes decir en donde has estado en las últimas horas transcurridas?",
                 f"{Mapa[zmapa][0]} \n\nCarajo, pobre Kratos, realmente espero que puedan encontrar al responsable a la brevedad \nSolamente estuve en Europa entrenando un poco.",
                 "Mario \n\nEl no pudo haber estado ahí, Kratos solo visita Europa acompañado \nde nosotros, y dado que hoy los transbordadores no hacen viajes, eso es imposible",
                 "Crash \n\nDe todas formas, muchas gracias por la información que nos ha brindado",
                 f"{Mapa[zmapa][0]} \n\nMuchas gracias igualmente, y espero ustedes encuentren al culpable"],
            [f"Crash \n\nQue rollo, {Mapa[zmapa][0]}? \nVengan acá camaradas",
                 f"{Mapa[zmapa][0]} \n\nQue onda chicos, oigan, ¿donde esta Kratos?",
                 f"Ezio \n\nAlguien ha asesinado a Kratos, y teniendo en cuenta que ninguno de nosotros estaba con \nel,necesitamos que saber quien le ha privado de la vida. \nHablando de ello mismo, cuentanos donde estuviste estas últimas horas que han pasado..",
                 f"{Mapa[zmapa][0]} \n\nEstaba de visitando a un viejo amigo en la Ciudad Ensoñada\nLos motores de mi nave siguen calientes si es que no me creen.",
                 "Ezio \n\nNo te preocupes,contamos con que Kratos no estuvo en la Ciudad Ensoñada, puesto que\n odia el clima ahí,por ende es imposible que el estuviera en ese lugar",
                 f"{Mapa[zmapa][0]} \n\nMuy bien, nos vemos luego entonces, pues tengo algunos asuntos pendientes por atender. \nAnsío que encuentren al asesino lo mas pronto posbile."],
            [f"{Mapa[zmapa][0]} \n\nHola amigos, ¿les puedo ayudar con algo?",
                 f"Link \n\nHey!! {Mapa[zmapa   ][0]},de hecho creo que si,fijate que estamos buscando al bastardo que mató a nuestro amigo Kratos,\n  y dada la naturaleza de la situación, ¿dónde has estado las últimas horas?",
                 f"{Mapa[zmapa][0]} \n\nLa verdad es que no logro recordarlo del todo...",
                 f"{Mapa[zmapa][0]} \n\nYa lo recordé.Me encontraba con {Mapa[nombre_random][0]} esperando un transbordador en la Luna, \ny posteriormente me dirigí a la ZME",
                 f"Ezio \n\nEntiendo,muchas gracias de todos modos por responder la pregunta. {Mapa[zmapa][0]}"]]
    image2 =[[Mapa[zmapa][3],mario,Mapa[zmapa][3],mario,crash,Mapa[zmapa][3]],[crash,Mapa[zmapa][3],ezio,Mapa[zmapa][3],ezio,Mapa[zmapa][3]],[Mapa[zmapa][3],link,Mapa[zmapa][3],Mapa[zmapa][3],ezio]]
    if asesino[0]==Mapa[zmapa][0]:
        if DialogCount>0 and DialogCount<len(dialogo1): 
            canvas.itemconfig(Imagen,image=image[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):  
            volver_menu()
        else:             
            Imagen=canvas.create_image(0,0,image=image[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Times New Roman",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogos[num_dialogo]):  
            canvas.itemconfig(Imagen,image=image2[num_dialogo][DialogCount])
            canvas.itemconfig(dialogo,text=dialogos[num_dialogo][DialogCount])
        elif DialogCount>=len(dialogos[num_dialogo]): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=image2[num_dialogo][DialogCount],anchor = "nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogos[num_dialogo][DialogCount],anchor="nw",font=("Times New Roman",20))
#Encontrar objeto importante
def encontrarhacha():  
    global dialogo
    global Imagen
    dialogo1=["Mario \n\nHey , miren lo que he encontrado.Es nada mas y nada menos que el hacha de Kratos.\nParece que fue aquí donde lo mataron por lo visto.",  
            "Link \n\nMalditos!!!",
             "Mario \n\nNo me detendré hasta encontrar a este bastardo infeliz.",
             "Crash \n\nDescuida mi buen Ezio, te aseguro que lo encontraremos."]
    ImgTex1=[mario,link,mario,crash]
    
    dialogo2=["Ezio \n\nVaya vaya... que raro, parece ser que no hay nada por aqui, por lo que dudo que \nKratos haya estado cerca de esta área o de sus alrededores", 
             "Crash \n\nQuizá tengas razón y el no haya estado por aqui",
             "Mario \n\nDescuida Kratos, ten por seguro que te vengaré muy pronto..."]
    ImgTex2=[ezio,crash,mario]
    
    if asesino[1]==Mapa[zmapa][1]: 
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Times New Roman",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image=ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Times New Roman",20))
#encontrar pista en las areas
def encontrarpista():
    global dialogo
    global EnLugar
    global DialogCount
    global Imagen
    dialogo1=["Crash \n\nVale mis estimados, creo que lo mejor seria que nos dividamos y así tener mayores \nprobabilidades de encontrar cualquier cosa que nos pueda conducir hacia el asesino de\n Kratos.",
             "Ezio \n\nDemonios! Creo que cabo de encontrar algo...",
             "Ezio \n\nEncontre "+asesino[2]+",pero no creo estar seguro de quien es el dueño",
             "Link \n\nProbablemente el asesino de Kratos lo dejó caer de forma accidental y sin haberse dado\n cuenta de ello."]
    ImgTex1=[crash,ezio,ezio,link]
    
    dialogo2=["Crash \n\nMuy bien amigos mios, creo que lo mejor seria que nos dividamos y así tener mayores \nprobabilidades de encontrar cualquier cosa que nos pueda conducir hacia el asesino de\n Kratos.",
             "...",
             "Mario \n\nPor lo visto, no hay nada por aquí que nos pueda indicar que fue en\n este mismo lugar donde mataron a Kratos",
             "Ezio \n\nEntonces definitivamente tenemos que seguir buscando, quizá deberíamos intentar en\n otro lugar y probar suerte..."]
    ImgTex2=[crash,BarraDialogo,mario,ezio]
    
    if asesino[2]==Mapa[zmapa][2]:
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarhacha()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo1[DialogCount],anchor="nw",font=("Times New Roman",20))
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarhacha()
        else:             
            Imagen=canvas.create_image(0,0,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=dialogo2[DialogCount],anchor="nw",font=("Times New Roman",20))
#Ubicar mapa
def ubicar_mapa(lugar): 
    for i in range(5):
        if lugar==Mapa[i][1]:
            return i       
#Volver al menu 
def volver_menu():
    global dialogo
    global DialogCount
    global EnLugar
    EnLugar=0
    if AccionesCount==5:
        canvas.delete(dialogo)
        DialogCount=0
        EnLugar=5
        resolvermisterio()
    else:
        canvas.pack(fill="both",expand=True) 
        canvas.pack() 
        canvas.create_image(0,0,image=torre,anchor="nw") 
        mostrar_botones()
        boton_menu.place(x=5,y=680)
        canvas.create_text(600,660,text="Selecciona un lugar para buscar",fill="Black",font=("Times New Roman",26)) 
        canvas.create_text(600,700,text=f"Movimientos restantes: {5-AccionesCount}",fill="Black",font=("Times New Roman",26)) 
#Funcion para continuar dialogo
def siguiente():
    global DialogCount
    global AnswerBien
    DialogCount+=1
    if EnLugar==1:
        destino(nombre_lugar)
    elif EnLugar==2: 
        encontrarpista()
    elif EnLugar==3: 
        encontrarhacha()
    elif EnLugar==4: 
        conversacion()
    elif EnLugar==5: 
        if DialogCount==1: 
            boton_siguiente.place_forget()
            mostrar_opciones()
        resolvermisterio()
    elif EnLugar==6: 
        Final(AnswerBien)
    elif EnLugar==7:
        root.destroy()
#funcion para resolver el misterio
def resolvermisterio():
    global dialogo
    global DialogCount
    global ans
    global AnswerBien
    global EnLugar
    global Imagen
    
    DialogFinal=["Luffy \n\nFabuloso, creo que finalmente es hora de encontrar al bastardo que ha asesinado a Kratos",
                "Luffy \n\nQuien ha sido el asesino?",
                "Luffy \n\nEn donde es que fué asesinado Kratos?",
                "Luffy \n\nPor último,pero no menos importante ,con que arma se perpetró el asesinato?"]
    if DialogCount>0 and DialogCount<len(DialogFinal):
        canvas.itemconfig(dialogo,text=DialogFinal[DialogCount])
        boton_uno.configure(text=Mapa[0][DialogCount-1])
        boton_dos.configure(text=Mapa[1][DialogCount-1])
        boton_tres.configure(text=Mapa[2][DialogCount-1])
        boton_cuatro.configure(text=Mapa[3][DialogCount-1])
        boton_cinco.configure(text=Mapa[4][DialogCount-1])
    elif DialogCount>=len(DialogFinal): 
        DialogCount=0
        EnLugar=6
        canvas.delete(dialogo)
        canvas.delete(Imagen)
        ans=0
        for a in 'Katana','Pistola','Espada plateada','Lagrimas','Bocina':
            if asesino[2]==a:
                break
            ans+=1
        AnswerBien=True
        for i in range(3):
            if asesino[i]!=Conclusion[i]:
                AnswerBien=False
        boton_uno.place_forget()
        boton_dos.place_forget()
        boton_tres.place_forget()
        boton_cuatro.place_forget()
        boton_cinco.place_forget()
        boton_siguiente.place(x=1000,y=680) 
        Final(AnswerBien)
    else:             
        canvas.create_image(0,0,image=torre,anchor="nw")
        Imagen=canvas.create_image(0,0,image=crash,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=DialogFinal[DialogCount],anchor="nw",font=("Times New Roman",20))
#Funcion para resultado   
def resultado(respuesta):
    global DialogCount
    global Conclusion
    Conclusion.append(respuesta)
    DialogCount+=1  
    resolvermisterio()
#dialogo final
def Final(r):
    global ans
    global DialogCount
    global dialogo
    global Imagen, EnLugar
    if r==True: 
        objetivos=[f"La {asesino[2]} que encontramos como indicio? \nPues esa katana le pertenece a Deadpool \nPsicopata asesino a sueldo.",
                  f"La {asesino[2]} que encontramos como indicio? \nPues esa pistola le pertenece a Falloutboy .",
                  f"La {asesino[2]} que encontramos como indicio? \nPues esa espada plateada le pertenece a Hollow Knight \nAsesino mudo.",
                  f"Las {asesino[2]} que encontramos como indicio? \nPues esas lagrimas son de Isaac \nVaya, y tan inocente que aparenta ser.",
                  f"La {asesino[2]} que encontramos como indicio? \nPues esa bocina es de Sans \nTiene la mania de moverse a ritmo de su musica."]
        
        Dialogo_Final=["Ezio \n\nMuy bien amigos, por fin hemos encontrado quien ha sido el asesino de Kratos, y\nha sido..",
                     f"Mario \n\nEn verdad fue {asesino[0]} ?!?!?",
                     f"Ezio \n\nCiertamente, {asesino[0]} mato a Kratos dado que es un semidios, y le tenia recelo por ello",
                     "Link \n\nMe parece algo razonable, teniendo en cuneta que cuando fuimos a hablar con el, evidentemente \nnos mintió e intentó culpar de su delito a otra persona",
                     "Crash \n\nFue asi como logro pasar desapercibido y al mismo tiempo dejara de \nparecer un posible sospechoso para poder así lograr su objetivo y salirse con la suya",
                     "Mario \n\n¿¿Porque diablos es que ese idiota querria asesinar a Kratos??",
                     f"Ezio \n\nRecuerdas {objetivos[ans]}",
                      "Mario \n\nGracias a ello fue que logramos dar contigo.Pero ahora que se me viene a la mente, donde carajos está su cuerpo??",
                      f"{asesino[0]} \n\nTendrán que encontrarlo por ustedes mismos JAJAJAJA!!!.",
                      "Kratos \n\nAmigos?",
                      "Crash \n\nKratos? ¿Como es posible que sigas vivo?",
                      f"Kratos \n\nLarga historia, pero para no hacerla larga, digamos que tiene que ver con que soy un semidios",
                      "Mario \n\nEntonces,¿eso significa que no hay forma alguna de matarte?",
                      "Kratos \n\nLo mas seguro es que si, ya que no soy del todo inmortal, sin embargo,\n se necesita de objetos muy especiales y poderosos para lograr mi muerte",
                      "Crash \n\nNo tienes idea de como me alegra el verte.",
                       f"{asesino[0]} \n\nSi tan solo hubiera sabido eso un poco antes,\nhubiera intentado otra forma de matarte, algo un poco más adecuado para un semidios..",
                      "Kratos \n\nTendrás que aprender a usar la cabeza antes que simplemente usar un arma"]
        ImgFinal=[ezio,mario,ezio,link,crash,mario,ezio,mario,asesino[3],
                 kratos,crash,kratos,mario,kratos,crash,asesino[3],kratos]
        
        if DialogCount>0 and DialogCount<len(Dialogo_Final):  
            canvas.itemconfig(Imagen,image=ImgFinal[DialogCount])
            canvas.itemconfig(dialogo,text=Dialogo_Final[DialogCount])
        elif DialogCount>=len(Dialogo_Final): 
            DialogCount=0
            EnLugar=0
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            boton_siguiente.place_forget()
            root.destroy()
        else:            
            Imagen=canvas.create_image(0,0,image=ImgFinal[DialogCount],anchor="nw")
            dialogo=canvas.create_text(200,440,fill="White",text=Dialogo_Final[DialogCount],anchor="nw",font=("Times New Roman",20))
    else:
        Imagen=canvas.create_image(0,0,image=crash,anchor="nw")
        dialogo=canvas.create_text(200,440,fill="White",text=f"Luffy \n\nTe falta investigar mejor.\nCulpable:{asesino[0]}\nLugar:{asesino[1]}\nArma:{asesino[2]}",anchor="nw",font=("Times New Roman",20)) 
        EnLugar=7
#boton luna
boton_luna=Button(canvas,text="Luna",bd='5',activebackground='Blue',width=12,command=cambia_luna)  
boton_luna.place(x=1050,y=50)
#boton ciudad
boton_ciudad=Button(canvas,text="Ciudad",bd='5',activebackground='Blue',width=12,command=cambia_ciudad)
boton_ciudad.place(x=600,y=100)
#boton europa
boton_europa=Button(canvas,text="Europa",bd='5',activebackground='Blue',width=12,command=cambia_europa)
boton_europa.place(x=250,y=250)
#boton zme
boton_zme=Button(canvas,text="ZME",bd='5',activebackground='Blue',width=12,command=cambia_zme)
boton_zme.place(x=150,y=550)
#boton nessus
boton_nessus=Button(canvas,text="Nessus",activebackground='Blue',bd='5',width=12,command=cambia_nessus)
boton_nessus.place(x=900,y=500)
#boton menu
boton_menu=Button(canvas,text="menu",activebackground='Blue',bd='5',width=12,command=volver_menu)
boton_menu.place(x=5,y=680)
#botn siguiente
boton_siguiente=Button(canvas, text="siguiente",activebackground='Blue',bd='5', width=12, command=siguiente)
boton_siguiente.place(x=1000,y=680)
#boton para checar lugares
boton_preguntar=Button(canvas,text="Interrogar a la persona",activebackground='Blue',bd='5',width="20",command=interrogar,font=("Helveltica",12))
boton_investigar=Button(canvas,text="Analizar el lugar",activebackground='Blue',bd='5',width="20",command=observar,font=("Helveltica",12))
#botones para las respuestas del asesinato
boton_uno=Button(canvas,text="",width="28",command= lambda:resultado(Mapa[0][DialogCount-1]),font=("Helveltica",12))
boton_dos=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[1][DialogCount-1]),font=("Helveltica",12))
boton_tres=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[2][DialogCount-1]),font=("Helveltica",12))
boton_cuatro=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[3][DialogCount-1]),font=("Helveltica",12))
boton_cinco=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[4][DialogCount-1]),font=("Helveltica",12))
root.mainloop() 