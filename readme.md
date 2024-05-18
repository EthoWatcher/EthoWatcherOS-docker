# EthoWatcher-OS Docker
This repo can be used to construct a docker container that has all the library, dependecies constructed and aranged of the EthoWathcher OS suit.


## Clone all important repo
To run this applictation you will need to assemble all the versions of the library's of the EthoWatcher-os. Inside the "gestao_dados" folder open a powershell and clone the repos. If you don't have the git tooling for windows you will need to install to perfom this actions.

```powershell
# First command
git clone https://github.com/EthoWatcher/ethowatcher-server.git
```

```powershell
# Second command
git clone https://github.com/EthoWatcher/ethowatcher-smart
```

```powershell
# Third command
git clone https://github.com/EthoWatcher/gestao-dados
```

Create a folder called "analise_dados" inside this folder to contain all your analises.

## Create folder that has old mongo data files
Create a folder, recommend to be called "mongo_data", inside this repo. This folder will be use to mantain your mongodb data.

## Build.
After construct the folder structure with all ethowatcher libraries you will need to build the container in your machine. To perform this step you will need the Docker installed in your machine. If you don't have go install that first.
In the powershell 
```ps1
# 4 command
docker build . -t "ethowatcheros"
```
## After build you will be able to run the container

After build you will be able to run the container, in the example command you will need to found the complete path of the "mongo_data" in your computer. In my computer was in the "C:\doutorado\software\EthoWatcherOS-docker\"

```ps1
# 5 command
docker run -p 8888:8888 -p 27017:27017 -p 5000:5000 -v C:\doutorado\software\EthoWatcherOS-docker\mongo_data\:/data/db "ethowatcheros"

docker run -p 8888:8888 -p 27017:27017 -p 5000:5000 -v C:\mongo_data\:/data/db "ethowatcheros"
```


