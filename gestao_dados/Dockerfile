FROM node:hydrogen-alpine3.19
RUN apk update && apk add bash
RUN mkdir -p /app/app
WORKDIR /app/app
COPY ethowatcher-smart /app/app
RUN npm instal
RUN npx browserslist@latest --update-db

RUN npm run build
EXPOSE 8080

