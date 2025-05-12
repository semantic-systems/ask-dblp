# Next.js Frontend Dockerfile (dblp-nli/dblp-nli-app/Dockerfile)
FROM node:18-alpine

ARG API_URL

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
