# YouTube Downloader & Screen Recorder  

Este é um programa desenvolvido em Python que permite baixar vídeos do YouTube em alta ou baixa qualidade, além de extrair apenas o áudio. Ele também inclui uma funcionalidade para gravação de tela.  

## 🚀 Funcionalidades  

- **Download de vídeos do YouTube**  
  - Alta Qualidade  
  - Baixa Qualidade  
  - Apenas Áudio (MP3)  
- **Gravação de Tela**  
  - Iniciar, Pausar, Continuar e Parar gravação  

## 📦 Instalação  

Antes de começar, certifique-se de ter o **Python 3.x** instalado no seu sistema.  

1. **Clone este repositório**  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
2. Crie um ambiente virtual (opcional, mas recomendado)
   python -m venv venv
  source venv/bin/activate  # Para Linux/Mac
  venv\Scripts\activate  # Para Windows
3.Instale as dependências
  pip install -r requirements.txt

Como Usar:
Execute o arquivo principal do programa:
  python interface.py
Escolha a funcionalidade desejada:

YouTube Downloader: Cole o link do vídeo, selecione o formato e a qualidade, e clique em "Download".

Screen Recorder: Escolha o diretório e nome do arquivo, clique em "Gravar" e use os botões para pausar, continuar ou parar a gravação.

📜 Dependências
O projeto utiliza as seguintes bibliotecas:
tkinter (interface gráfica),
pytube (download de vídeos do YouTube),
moviepy (conversão de vídeo para áudio),
pyscreenrec (gravação de tela),
clipboard (manipulação da área de transferência).

Caso precise instalar manualmente:
  pip install tkinter pytube moviepy pyscreenrec clipboard


