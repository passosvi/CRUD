# Imagem base
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt /app/requirements.txt

# Instalar dependências
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar o restante do código da aplicação
COPY . /app

# Comando para iniciar o aplicativo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
