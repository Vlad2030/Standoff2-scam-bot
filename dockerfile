FROM python3:slim
WORKDIR /app-so2
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python3", "main.py" ]
