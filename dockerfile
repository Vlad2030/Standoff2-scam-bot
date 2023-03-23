FROM python3:slim
WORKDIR /app-so2
COPY . .
RUN sh setup.sh
CMD [ "sh", "start.sh" ]
