FROM nvidia/cuda:12.6.1-base-ubuntu24.04

# Instalar as dependências necessárias
RUN apt-get update
RUN apt-get install -y python3.8 python3.8-dev
RUN apt-get install -y ffmpeg

# Instalar o pip e outras dependências
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

# Copiar o arquivo requirements.txt
COPY requirements.txt /app/requirements.txt

# Instalar as dependências
RUN pip3 install -r /app/requirements.txt

# Copia o restante do código para o contêiner
COPY . /app

# Exponha a porta 8000 para o FastAPI
EXPOSE 8000

# Define o comando para rodar a aplicação usando o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

