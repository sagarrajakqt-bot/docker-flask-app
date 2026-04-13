
FROM python:3.9

WORKDIR E:\vsdevops\project\app.py

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
