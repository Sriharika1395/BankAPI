FROM alpine:3.1

RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask
RUN pip install flask_pymongo
RUN pip install datetime
docker run -t -i --rm -v $(pwd):/app -w /app node:slim sh -c 'apt-get update && apt-get install -y build-essential && apt-get install -y python && npm install'

COPY BankAPI.py /src/simpleapp.py

CMD ["python", "/src/simpleapp.py", "-p 7000"]