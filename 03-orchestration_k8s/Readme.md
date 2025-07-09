## Minikube

### Install
https://minikube.sigs.k8s.io/docs/start

(see OS instruction specifics)

### Start and lifecycle
```
minikube start --driver=docker
```

Lifecycle: start|stop|status|pause

Delete cluster:
```
minikube delete --all
```

### Checkup
```
docker ps
docker image ls
docker volume ls

minikube kubectl get pods
```

Define an alias for kubectl:
```
alias kubectl='minikube kubectl --'
function kubectl { minikube kubectl -- $args }
doskey kubectl=minikube kubectl $*
```
### Dind (Docker in Docker)
```
docker ps                               # => minikube
docker exec -it minikube docker ps -a   # containers used by minikube

docker image ls
docker exec -it minikube docker image ls

minikube docker-env
```
=> use with eval (linux) ou follow instruction in powershell
Ex: 
- `eval $(minikube docker-env)`
- `& minikube -p minikube docker-env --shell powershell | Invoke-Expression`

```
docker ps
docker image ls
```
### Commands kubectl
```
kubectl api-resources
```

#### default namespace
```
get pods
get pod
get po
```

#### all namespaces
```
get po -A
```

#### a specific namespace
```
get pod -n kube-system
```

#### other options
```
-o json|yaml|...
-L columns

-l selector by label
--show-labels
```

## dashboard
```
minikube dashboard
```
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

Reprise de l'exemple (3e jour)
```
kubectl create deployment balanced --image=kicbase/echo-server:1.0
kubectl expose deployment balanced --type=LoadBalancer --port=8080
```


Résistance aux pannes:
```
kubectl delete pod balanced-57c6cb5949-fz6rr
kubectl delete pod -l app=balanced
```

Mis en pause:
```
kubectl scale --replicas=0 deployment/balanced
```

Suppression des pods => supprimer le déploiement
```
kubectl delete deployment -l app=balanced
```

## Pod + Service
Alternative au déploiement (pas de replicat set, scaling, rollout, ...)

### Pod
```
kubectl run echosolo --image=kicbase/echo-server:1.0
```
NB: label par défaut run=... (deployment: app=...)
```
kubectl run echosolo2 -l app=echosolo2 --image=kicbase/echo-server:1.0
```

### Service
```
kubectl expose pod echosolo --type=NodePort --port=8080
```
=> obtain CLUSTER-IP : 10.108.102.108

## Utilisation de fichier yaml
```
kubectl apply -f .\echo.service.yml
kubectl get po,svc -l app=echosolo3
```
## Diagnostic
Logs:
```
kubectl logs echosolo4-54f4d856c8-d726n
```
Exec (à condition d'avoir bash ou sh)
```
kubectl exec -it echosolo4-54f4d856c8-d726n -- bash
```

