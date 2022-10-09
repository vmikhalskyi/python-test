FROM ubuntu:20.04
RUN apt update -y && apt install python3 -y && apt install pip -y
RUN pip install Flask
COPY . /app
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["test.py"]
