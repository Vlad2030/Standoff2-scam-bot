FROM python3:slim
WORKDIR /app-so2
COPY . /app-so2/
RUN sh setup.sh
CMD [ "sh", "start.sh" ]
