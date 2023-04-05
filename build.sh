#!/bin/bash

USERNAME=shreyas-acharya
IMAGE=fastapi
VERSION=`cat ./App/VERSION`
echo "VERSION : $VERSION"

docker build -t ghcr.io/$USERNAME/$IMAGE:$VERSION .
docker tag ghcr.io/$USERNAME/$IMAGE:$VERSION ghcr.io/$USERNAME/$IMAGE:latest

docker push ghcr.io/$USERNAME/$IMAGE:$VERSION
docker push ghcr.io/$USERNAME/$IMAGE:latest
