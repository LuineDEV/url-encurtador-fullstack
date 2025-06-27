# Estágio 1: Usar uma imagem Python moderna e leve.
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container.
WORKDIR /code

# Copia primeiro o arquivo de dependências para otimizar o cache do Docker.
COPY ./requirements.txt /code/requirements.txt

# Instala as dependências.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia o restante do código da aplicação.
COPY ./app /code/app

# Expõe a porta que a aplicação vai usar.
EXPOSE 8000

# Comando para iniciar a aplicação quando o container for executado.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]