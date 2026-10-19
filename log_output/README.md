# Log output

Generates a random string on startup and prints it with a timestamp every 5 seconds. It also responds to GET / with the current timestamp and the random string.

## Run locally

python app.py

The port can be set with the PORT environment variable (default 8000).

## Docker image

docker.io/mrshiiri/log-output:2

## Kubernetes

kubectl apply -f manifests/