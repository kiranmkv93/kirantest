FROM tensorflow/tensorflow:2.6.0

WORKDIR /opt/ml/code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SAGEMAKER_PROGRAM app.py
