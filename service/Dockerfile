FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV PYTHONPATH "${PYTHONPATH}:/user/src/app"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "jumprankingAPI_main.py" ]

