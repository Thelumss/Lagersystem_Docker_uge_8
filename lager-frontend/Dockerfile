# FROM tells the docker what base program to install in this case node:20 
FROM node:20

# WORDIR say that the directory that we will be working in, in this case that is the /app directory 
WORKDIR /app

# copy does what you would exspect here it copys the package.json and package-lock.json
COPY package.json package-lock.json ./

# RUN runs a command in this case the npm install for all of the packages in package.json to be installed into the docker container
RUN npm install

# here we first copy evreything in the file that the dockerfile lies in in to the /APP
COPY . .

# we expose port 5173 meaning that the contatiner open up in port 5173 so other program can asses it via port 5173
EXPOSE 5173

# cmd is the end where we tell the docker that this the command you run. in this case it is to keep the frontend running
CMD ["npm", "run", "dev","--","--host", "0.0.0.0"]

