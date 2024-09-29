FROM cgr.dev/chainguard/python:latest

WORKDIR /quotes-app

COPY . /quotes-app

#COPY app.py src/quotes.txt ./

ENTRYPOINT [ "python", "/quotes-app/app.py" ]