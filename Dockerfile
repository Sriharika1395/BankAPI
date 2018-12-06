FROM centos:7

RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask
RUN pip install flask_pymongo
RUN pip install datetime
RUN pip install python-bcrypt


COPY BankAPI.py /src/simpleapp.py

CMD ["python", "/src/simpleapp.py", "-p 7000"]