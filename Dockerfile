FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

ENV TEXT="Hello hello hello!"

ENV PERSON="Chat bot"

COPY python_file.py /python_file.py

CMD ["python3", "/python_file.py"]