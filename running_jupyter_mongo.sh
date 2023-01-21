#!/bin/bash
jupyter notebook --ip  0.0.0.0 --port 8888 --allow-root &
mongod --bind_ip_all &
python /home/ethowatcher/gestao_dados/ethowatcher-server/app.py