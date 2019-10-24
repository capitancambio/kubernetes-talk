# Scripts
To be executed by dags in the kubernetes cluster

It can also be installed run locally for testing.

```
pipenv install
pipenv run scripts transform --help
```

To dockerise it and make the image available to minikube
```
eval $(minikube docker-env) # configure docker to use minikube deaemon
docker build -t scripts:latest .
# give it a go
docker run -it scripts:latest scripts transform --help
```
