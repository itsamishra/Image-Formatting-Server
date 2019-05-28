#!/bin/bash
echo "Starting docker container...";
docker run -p 5000:5000 -v /Users/ashutoshmishra/Documents/Image-Formatting-Server/src:/app hello-world1;
echo "Pruning containers and images...";
yes | docker container prune;
yes | docker image prune;
echo "Exiting...";