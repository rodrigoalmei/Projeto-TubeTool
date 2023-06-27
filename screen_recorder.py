#Importação De Bibliotecas
import pyscreenrec

#Importação De Arquivos
import interface

#Cria uma variável que recebe a função de gravação da biblioteca "pyscreenrec"
recording = pyscreenrec.ScreenRecorder()

#Função que inicia a gravação
def startRec():
    path = interface.directoryVar.get()
    file = interface.fileName_Var.get()

    recording.start_recording(str(path + f"/{file}" + ".mp4"),7.5)

    #Desativa o botão (Gravar) e ativa os botões (Pausar e Parar)
    interface.buttonStart.config(state="disabled")
    interface.buttonPause.config(state="normal")
    interface.buttonStop.config(state="normal")

    #Exibe uma label com o status da gravação
    interface.statusVideo.set("Gravando...")
    interface.labelStatus.config(foreground="red")

#Função que resume a gravação
def resumeRec():
    recording.resume_recording()

    #Ativa o botão (Pausar) e desativa o botão (Resumir)
    interface.buttonPause.config(state="normal")
    interface.buttonResume.config(state="disabled")

    #Exibe uma label com o status da gravação
    interface.statusVideo.set("Gravando...")
    interface.labelStatus.config(foreground="red")

#Função que pausa a gravação
def pauseRec():
    recording.pause_recording()

    #Ativa o botão (Resumir) e desativa o botão (Pausar)
    interface.buttonResume.config(state="normal")
    interface.buttonPause.config(state="disabled")

    #Exibe uma label com o status da gravação
    interface.statusVideo.set("Pausado!")
    interface.labelStatus.config(foreground="black")

#Função que para a gravação
def stopRec():
    recording.stop_recording()

    #Ativa o botão (Gravar) e desativa os botões (Resumir, Pausar e Parar)
    interface.buttonStart.config(state="normal")
    interface.buttonResume.config(state="disabled")
    interface.buttonPause.config(state="disabled")
    interface.buttonStop.config(state="disabled")

    #Não exibe nada se o vídeo não está sendo gravado
    interface.statusVideo.set("")