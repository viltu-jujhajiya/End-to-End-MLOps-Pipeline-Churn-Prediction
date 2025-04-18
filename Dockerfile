FROM python:3.10-slim


WORKDIR /app


COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt


EXPOSE 1234

CMD ["python3", "src/app.py", "--host", "0.0.0.0", "--port", "1234"]