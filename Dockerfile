FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY sonar-client.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./sonar-client.py" ]