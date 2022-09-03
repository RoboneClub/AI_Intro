FROM python:3.7

WORKDIR /cifar10_classifier

COPY . /cifar10_classifier/

RUN python -m pip install -r requirements.txt

CMD python cifar10_classifier.py