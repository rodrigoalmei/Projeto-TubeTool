#Importação De Bibliotecas
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import clipboard as clip

#Importação De Arquivos
import youtube_download as youtube
import screen_recorder as screenRec

#Função que executa a ação do botão de colar texto da área de transferência
def pasteLink():
    linkBox.delete(0, "end")
    linkBox.insert(0, clip.paste())

#Função que executa a ação do botão de escolher o diretório
def selectDirectory():
    wayDirectory = filedialog.askdirectory()
    directoryVar.set(wayDirectory)

#Gera a tela principal com suas especificações
screen = Tk()

screen.title("Projeto")
screen["background"] = "#ffffff"
screen.geometry("500x290+500+100")
screen.resizable(width=0, height=0)

#Cria dentro da screen o elemento notebook
notebook = ttk.Notebook(screen)
notebook.place(x=0, y=0, width=500, height=500)

#Criação de abas para cada funcionalidade do programa
aba1 = Frame(notebook)
notebook.add(aba1, text="YouTube Downloader")
aba2 = Frame(notebook)
notebook.add(aba2, text="Screen Recorder")

#Cria uma variável para receber o nome do diretório
directoryVar = StringVar()
directoryVar.set("Selecionar Diretório...")

### ABA 1 (YOUTUBE DOWNLOADER) ###

#Cria a Label e a TextBox para a inserção do link (Também há um Button para colar o link na TextBox)
labelLink = Label(aba1, text="Link Do Vídeo:")
labelLink.place(x=0, y=10, width=100, height=20)
linkBox = Entry(aba1)
linkBox.place(x=100, y=10, width=350, height=20)
buttonPaste = Button(aba1, text="☰", command=pasteLink)
buttonPaste.place(x=463, y=10, width=20, height=20)

#Cria um Button e uma Label para a especificação do caminho (diretório) para onde o vídeo será baixado
buttonDirectory = Button(aba1, text="Diretório...", command=selectDirectory)
buttonDirectory.place(x=10, y=40, width=80, height=20)
labelDirectory = Label(aba1, textvariable=directoryVar, foreground="#696969")
labelDirectory.place(x=100, y=40, width=382, height=20)

#CheckButtons para escolher o tipo e a qualidade de vídeo a ser baixado
vquality = IntVar()

HightQuality = Radiobutton(aba1, text="Alta Qualidade", value=1, variable=vquality)
HightQuality.place(x=9, y=90, width=100, height=20)
LowQuality = Radiobutton(aba1, text="Baixa Qualidade", value=2, variable=vquality)
LowQuality.place(x=194, y=90, width=110, height=20)
OnlyAudio = Radiobutton(aba1, text="Apenas Áudio", value=3, variable=vquality)
OnlyAudio.place(x=385, y=90, width=100, height=20)

#Button para executar o download do vídeo
buttonDownload = Button(aba1, text="Download", command=youtube.downloadFunction)
buttonDownload.place(x=204, y=140, width=90, height=20)

#Cria uma label para a visualização do título do vídeo a ser baixado
videoTitle = StringVar()
videoTitle.set("Copie um link do YouTube para fazer o download!")

labelTitle = Label(aba1, background="#ffffff", textvariable=videoTitle)
labelTitle.place(x=10, y=185, width=473, height=20)

#Cria uma ProgressBar para exibir ao usuário que o download está sendo executado
progressBar = ttk.Progressbar(aba1, maximum=100, mode="indeterminate")
progressBar.place(x=10, y=230, width=473, height=20)

### ABA 2 (SCREEN RECORDER) ###

#Cria uma label e uma textBox para a inserção do nome do arquivo
labelFileName = Label(aba2, text="Nome Do Arquivo:")
labelFileName.place(x=10, y=10, width=100, height=20)

fileName_Var = StringVar()
fileNameBox = Entry(aba2, textvariable=fileName_Var)
fileNameBox.place(x=120, y=10, width=360, height=20)

#Cria um Button e uma Label para a especificação do caminho (diretório) para onde o vídeo será enviado
buttonVideo_dir = Button(aba2, text="Diretório...", command=selectDirectory)
buttonVideo_dir.place(x=10, y=40, width=80, height=20)
labelVideo_dir = Label(aba2, textvariable=directoryVar, foreground="#696969")
labelVideo_dir.place(x=100, y=40, width=382, height=20)

#Cria buttons para o gerenciamento de: (Gravar, Pausar, Resumir e Parar) a gravação
buttonStart = Button(aba2, text="◉", font=("Arial", 35), border=4, foreground="red", command=screenRec.startRec, state=NORMAL)
buttonStart.place(x=10, y=205, width=50, height=50)
buttonResume = Button(aba2, text="▶", font=("Arial", 25), border=3, command=screenRec.resumeRec, state=DISABLED)
buttonResume.place(x=65, y=215, width=40, height=40)
buttonPause = Button(aba2, text="⏸︎", font=("Arial", 30), border=3, command=screenRec.pauseRec, state=DISABLED)
buttonPause.place(x=110, y=215, width=40, height=40)
buttonStop = Button(aba2, text="⏹︎", font=("Arial", 30), border=3, command=screenRec.stopRec, state=DISABLED)
buttonStop.place(x=155, y=215, width=40, height=40)

#Cria uma Label para exibir o status da gravação
statusVideo = StringVar()

labelStatus = Label(aba2, textvariable=statusVideo)
labelStatus.place(x=200, y=225, width=60, height=20)

screen.mainloop()