FROM python:3.5-alpine

COPY app app
COPY main.py boot.sh ./
COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt
ENV FLASK_APP=main.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"] 


