# Estágio 1: Build da aplicação React

FROM node:20-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Estágio 2: Servir os arquivos estáticos com um servidor Nginx leve

FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# Expõe a porta 80, que é a padrão do Nginx

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]