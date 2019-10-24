# Dockerfile and deployment script.

The docker file is necessary to install the python kubernetes client library in alongside with
airflow

The deployment script contains:
* Namespace 
* Persitent volume claim to download the dags
* Postgres configuration
* User configuration so airflow can create pods in this namespace
* Airflow deployment: airflow, posgres and sidecar.
* sftp deployment and service

## Running 

With minikube started:
```sh
eval $(minikube docker-env) # configure docker to use minikube deaemon
docker build -t airflow:latest .
kubectl apply -f deployment.yml
# portforward airflow to have access from localhost (can be done via service too)

kubectl port-forward $(kubectl get pods | grep "^airflow" | awk '{print $1}') 8080 &  

# port forward sftp to 2222
kubectl port-forward $(kubectl get pods | grep "^sftp" | awk '{print $1}') 2222:22 &  
```



