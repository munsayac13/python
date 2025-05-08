FROM python:3.13

WORKDIR /pythonapp

COPY ./requirements.txt /pythonapp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /pythonapp/requirements.txt

COPY ./app /pythonapp/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]
