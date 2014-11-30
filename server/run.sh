#!/bin/bash

mongod >> mongo.log & 

sleep 3

cd Notifications

./run.sh & 


