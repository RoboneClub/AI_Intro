FROM python:3.7

WORKDIR /mnist_classifier

COPY . /mnist_classifier/

RUN python -m pip install -r requirements.txt

CMD python mnist_classifier.py