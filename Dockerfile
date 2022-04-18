FROM python:3.9
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements_test.txt /app/requirements.txt
RUN pip install -r requirements_test.txt
COPY . /app

CMD python main.py

