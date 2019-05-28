# Installs python 3.6.8
FROM python:3.6.8

# Sets /app as the working directory in the Docker container
WORKDIR /app

# Copies src directory into WORKDIR
COPY ./src .

# Installs packages in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Exposes port 5000
EXPOSE 5000

CMD [ "python3", "main.py" ]
