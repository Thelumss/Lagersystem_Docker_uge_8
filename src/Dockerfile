# FROM tells the docker what base program to install in this case python:3.11 
FROM python:3.11

# WORDIR say that the directory that we will be working in, in this case that is the /app directory 
WORKDIR /app

# copy does what you would exspect here it copys the requirements.txt
COPY requirements.txt ./

# RUN runs a command in this case the pip install for all of the packages in requirements.txt to be installed into the docker container
RUN pip install --no-cache-dir -r requirements.txt

# here we first copy evreything in the file that the dockerfile lies in in to the /APP
COPY . .
# here we copy config.json
COPY ../config.json ./config.json


# we expose port 5000 meaning that the contatiner open up in port 5000 so other program can asses it via port 5000
EXPOSE 5000

# cmd is the end where we tell the docker that this the command you run. in this case it is to keep the api running
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]