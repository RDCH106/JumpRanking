#!/bin/bash 

####################################################################################
#Script Name	:build.sh
#Description	:Build the docker images needed in docker-compose example
#Args           :string to be used as tag
#Author       	:Maykel Alonso
#Email         	:malonso@stt-systems.com
####################################################################################


echo "\nBuilding jump-contest-service image and tagged as $1"
docker build ./service -t jump-contest-service:$1


echo "\n\nBuilding jump-contest-web image and tagged as $1"
docker build ./web -t jump-contest-web:$1 

