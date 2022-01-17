FROM python:3

RUN mkdir -p /Users/Donco/desktop/Cours_LP-DIM/docker
WORKDIR /Users/Donco/desktop/Cours_LP-DIM/docker
RUN pip install discord

COPY . .

CMD ["python3", "crotal.py"]