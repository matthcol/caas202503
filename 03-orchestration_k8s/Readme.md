## Minikube

### Install
https://minikube.sigs.k8s.io/docs/start

(see OS instruction specifics)

### Start and lifecycle
```
minikube start --driver=docker
```

Lifecycle: start|stop|status|pause

### Checkup
```
docker ps
docker image ls
docker volume ls

minikube kubectl get pods
```

alias kubectl='minikube kubectl --'

### Commands kubectl
#### default namespace
get pods
get pod
get po

#### all namespaces
get po -A

#### a specific namespace
get pod -n kube-system

#### other options
-o json|yaml|...
-L columns

-l selector by label
 --show-labels

## dashboard
minikube dashboard

## Tutorial minikube
### Deployment + Service
```
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```

```
kubectl create deployment hello-minikube2 --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube2 --type=NodePort --port=8080
```

### Lister
Tous les pods, services, deployments du namespace par défaut:
```
kubectl get po,svc,deployment
```

### Utiliser les labels
Filtrer par label:
```
kubectl get --show-labels po,svc,deployment
kubectl get -l app=hello-minikube po,svc,deployment
```

Voir les labels: --show-labels
```
kubectl get pods --show-labels -l app=hello-minikube
```

Ajout 1 label aux pods de l'application hello-minikube:
```
kubectl label pods -l app=hello-minikube  kind=validation
```

Modification d'1 label des pods de l'application hello-minikube:
```
kubectl label --overwrite pods -l app=hello-minikube  kind=test
```

Suppression d'1 label des pods de l'application hello-minikube:
```
kubectl label pods -l app=hello-minikube  kind-
```

### Replica Set et Load Balancer
3e deployment with load balancer

```
kubectl create deployment hello-minikube3 --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube3 --type=LoadBalancer --port=8080
```

Augmente ou réduit le nombre de replica:
```
kubectl scale --replicas=3 deployment/hello-minikube3 
kubectl scale --replicas=3 -l app=hello-minikube3 deployment

kubectl scale --replicas=2 deployment/hello-minikube3 
```

Vérifier:
```
kubectl get -l app=hello-minikube3 pods,rs,deployments,svc  
```





