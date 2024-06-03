
# EthoWatcher-OS Docker

This repository provides a Docker container setup for the EthoWatcher OS Data Science platform. It includes all the necessary libraries and dependencies. To run this repository, you must have Docker installed on your machine.

## Related Repositories

This repository contains copies of all libraries required for running the EthoWatcher OS Data Science platform. For the latest versions of each library, clone the following repositories:

```powershell
# Clone EthoWatcher Server
git clone https://github.com/EthoWatcher/ethowatcher-server.git
```

```powershell
# Clone EthoWatcher Smart
git clone https://github.com/EthoWatcher/ethowatcher-smart.git
```

```powershell
# Clone Data Management
git clone https://github.com/EthoWatcher/gestao-dados.git
```

## Create MongoDB Data Folder

In order to the application runs correctly you will need to create one folder that will be used to save the data of MongoDb database. For example, it might be `C:\doutorado\software\EthoWatcherOS-docker\mongo_data\` or simply `C:\mongo_data\`. Coulde be an empty folder, if you are starting fresh, or dowloand the data from my theses.

## Build the Docker Container

Once the folder structure with all EthoWatcher libraries is set up, build the Docker container. Ensure Docker is installed on your machine.

Open a PowerShell terminal and run:

```powershell
# Build Docker Container
docker build . -t "ethowatcheros"
```

## Run the Docker Container

After building the container, you can run it. Find the complete path of the `mongo_data` folder on your computer. For example, it might be `C:\doutorado\software\EthoWatcherOS-docker\mongo_data\` or simply `C:\mongo_data\`.

Run the following command:

```powershell
# Run Docker Container
docker run -p 8888:8888 -p 27017:27017 -p 5000:5000 -v C:\doutorado\software\EthoWatcherOS-docker\mongo_data\:/data/db "ethowatcheros"
```

Alternatively:

```powershell
docker run -p 8888:8888 -p 27017:27017 -p 5000:5000 -v C:\mongo_data\:/data/db "ethowatcheros"
```

## Using Docker Compose

If you have Docker Compose installed, you can use it to set up and run the container. In the root folder of this repository, run:

```powershell
# Run Docker Compose
docker-compose up
```

