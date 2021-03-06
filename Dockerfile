FROM python:3.6.8

WORKDIR /usr/src/app

COPY ./src .

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]