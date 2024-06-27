FROM denoland/deno:latest

EXPOSE 80

USER deno

WORKDIR /app

COPY . .

RUN deno cache webserver.ts

CMD ["run", "--allow-net", "webserver.ts"]