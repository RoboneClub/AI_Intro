FROM python:3.7

WORKDIR /TF_2.x

COPY . /TF_2.x/

RUN python -m pip install tensorflow
RUN python -m pip install numpy
RUN python -m pip install opencv-python-headless
RUN python -m pip install matplotlib

CMD python tensor_test.py