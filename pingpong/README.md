# Ping-pong

A simple web server that responds to GET /pingpong with "pong N", where N is a counter that increases with every request. The counter is stored in memory and resets when the app restarts.

## Run locally

python app.py

The port can be set with the PORT environment variable (default 8000).

## Docker image

docker.io/mrshiiri/pingpong:1

## Kubernetes

kubectl apply -f manifests/